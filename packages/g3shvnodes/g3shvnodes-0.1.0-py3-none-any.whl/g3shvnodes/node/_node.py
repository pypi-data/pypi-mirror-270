from __future__ import annotations

import enum
import time
import typing

import shv

from abc import ABC, abstractmethod


class ClientNotSetError(AttributeError):
    """Raised when the client object is not set for the SHV Node."""
    pass


class ClientNotConnectedError(AttributeError):
    """Raised when the client object is not connected to the server."""
    pass


class SHVNode:
    """
    A SHV Node representation.

    The class is a base for all SHV Node representations. It provides
    similar API to the `shv.SimpleClient` class, but it is centered around
    a single SHV Node in the SHV tree.
    """
    def __init__(self, path: str) -> None:
        """
        Initialize the SHV Node.

        Args:
            path (str): Path to the SHV Node in the SHV tree.
        """
        self._path = path
        """
        Path to the SHV Node in the SHV tree. Should be a read-only string.
        """
        self._client: shv.ValueClient | None = None
        """
        The `shv.ValueClient` instance associated with the SHV Node. May be
        `None` if the node is not connected to the server. May be created
        and set using the `connect` method, or set using the `set_client`
        method.
        """
        self._subs: list[shv.RpcSubscription] = []
        """
        A list of `shv.RpcSubscription` instances associated with the SHV Node.
        Created and set using the `subscribe` method. May be empty if the
        node is not subscribed to the server. Is used for the unsubscription.
        """
        self._dir_exists_cache: dict[str, bool] = {}
        """
        Cache for the `dir_exists` method results. Is also updated when
        a method is successfully called using the `call` method.
        """

    def __str__(self) -> str:
        return self._path

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(path="{self._path}")'

    def _children(self) -> typing.Iterable[SHVNode]:
        """
        Overwrite this method to add a custom logic of the child nodes'
        collection.

        The method is called within the `children` method to collect the child
        nodes within the node's composition. It should return an iterable of
        `SHVNode` instances that are considered children of the current node.

        Returns:
            typing.Iterable[SHVNode]: An iterable of child nodes.
        """
        return tuple()

    def children(
        self, validate_path: bool = False, recursive: bool = False
    ) -> typing.Iterator[SHVNode]:
        """
        Iterate over all child nodes within the node's composition.

        The term "child node" refers to any `SHVNode` instance that is
        a direct attribute value of this `SHVNode` instance or is present
        in any of the mappings of this `SHVNode` instance. The nodes returned
        from the `_children` method are considered children. The iteration
        can be restricted to the actual children of the node, as they appear
        in the SHV tree, by setting the `validate_path` argument to `True`.
        It is also possible to collect children recursively (i.e. children
        of children) by setting the `recursive` argument to `True`.

        Args:
            validate_path (bool, optional): Restrict the node collection to\
                actual children of the current node, as they appear in the SHV\
                tree, by comparing their paths. Defaults to False.
            recursive (bool, optional): Collect children recursively\
                (i.e. children of children). Defaults to False.

        Returns:
            typing.Iterator[SHVNode]: An iterator over collected child nodes.
        """
        def yield_node(
            node: SHVNode, validate_path: bool, recursive: bool
        ) -> typing.Iterator[SHVNode]:
            if not validate_path or node.path.startswith(self.path):
                yield node
            if recursive:
                yield from yield_children(
                    node=node,
                    validate_path=validate_path,
                    recursive=recursive
                    )

        def yield_children(
            node: SHVNode, validate_path: bool, recursive: bool
        ) -> typing.Iterator[SHVNode]:
            for attr_value in vars(node).values():
                if isinstance(attr_value, SHVNode):
                    yield from yield_node(
                        node=attr_value,
                        validate_path=validate_path,
                        recursive=recursive
                        )
                elif isinstance(attr_value, typing.Mapping):
                    for value in attr_value.values():
                        if isinstance(value, SHVNode):
                            yield from yield_node(
                                node=value,
                                validate_path=validate_path,
                                recursive=recursive
                                )
            for node in node._children():
                if isinstance(node, SHVNode):
                    yield from yield_node(
                        node=node,
                        validate_path=validate_path,
                        recursive=recursive
                        )

        yield from yield_children(self, validate_path, recursive)

    @property
    def path(self) -> str:
        """Path to the SHV Node in the SHV tree."""
        return self._path

    @property
    def client(self) -> shv.ValueClient | None:
        """The `shv.ValueClient` instance associated with the SHV Node."""
        return self._client

    def _validate_client(self, client: typing.Any) -> None:
        """
        Validate the client object.

        Args:
            client (typing.Any): The client object to be validated.

        Raises:
            TypeError: If the client object is not an instance of\
                `shv.ValueClient`.
        """
        if client is None or isinstance(client, shv.ValueClient):
            return
        raise TypeError(
            f'Expected a "shv.ValueClient" object, got type '
            f'"{(type(client).__name__)}".'
            )

    def _assert_client_connected(
        self, client: shv.ValueClient | None
    ) -> typing.TypeGuard[shv.ValueClient]:
        """
        Assert that the client object is set and connected to the server.

        Args:
            client (shv.ValueClient | None): The client object to be validated.

        Raises:
            ClientNotSetError: If the node has no client set.
            ClientNotConnectedError: If the node client is not connected to
            the server.

        Returns:
            typing.TypeGuard[shv.ValueClient]: Returns `True` if the client is
            set and connected to the server. Validates the client object type.
        """
        if client is None:
            raise ClientNotSetError(
                f'Node "{self._path}" has no client set.'
                )
        if client.client.connected is False:
            raise ClientNotConnectedError(
                f'Node "{self._path}" is not connected to the server.'
                )
        return True

    def _set_client(self, client: shv.ValueClient | None) -> None:
        """
        Set the client object for the SHV Node and all its children
        recursively without validating the client object or disconnecting
        the current client.

        Args:
            client (shv.ValueClient | None): The client object to be set.
        """
        if self._client != client:
            self._client = client
        for child in self.children(validate_path=False, recursive=True):
            child._set_client(client)

    async def _set_client_ensure_disconnect(
        self, client: shv.ValueClient | None
    ) -> None:
        """
        Set the client object for the SHV Node and all its children
        recursively. Disconnect the current client if it is connected.

        Args:
            client (shv.ValueClient | None): The client object to be set.
        """
        if self._client != client:
            if self.is_connected:
                assert self._client is not None
                await self._client.disconnect()
            self._client = client
        for child in self.children(validate_path=False, recursive=True):
            await child._set_client_ensure_disconnect(client)

    def set_client_unsafe(self, client: shv.ValueClient | None) -> None:
        """
        Set the client object for the SHV Node and all its children.
        The client is validated, but the current client is not disconnected.

        The method is synchronous, which allows for setting the client
        object without the need for a running event loop, but may lead to
        potential issues if the previous client is not disconnected properly.

        Args:
            client (shv.ValueClient | None): The client object to be set.
        """
        self._validate_client(client)
        self._set_client(client)

    async def set_client(self, client: shv.ValueClient | None) -> None:
        """
        Set the client object for the SHV Node and all its children.
        The client is validated and the current client is disconnected.

        Args:
            client (shv.ValueClient | None): The client object to be set.
        """
        self._validate_client(client)
        await self._set_client_ensure_disconnect(client)

    @property
    def is_connected(self) -> bool:
        """The connection status of the client object."""
        try:
            return self._assert_client_connected(self._client)
        except (ClientNotSetError, ClientNotConnectedError):
            return False

    async def connect(self, url: str | shv.RpcUrl, *args, **kwargs) -> None:
        """
        Connect the SHV Node to the server using the given URL.

        The method acts similarly to the `set_client` method, but it creates
        a new `shv.ValueClient` instance utilizing the `SimpleClient`'s
        `connect` method. The client object is then set as the client for
        the SHV Node.

        Args:
            url (shv.RpcUrl): The URL of the server to connect to.
        """
        if isinstance(url, str):
            url = shv.RpcUrl.parse(url)
        client = await shv.ValueClient.connect(url, *args, **kwargs)
        await self.set_client(client)

    async def disconnect(self) -> None:
        """Disconnect the SHV Node from the server."""
        await self._set_client_ensure_disconnect(None)

    @property
    def is_subscribed(self) -> bool:
        """The subscription status of the SHV Node."""
        if self._client is None:
            return False
        return self._client.is_subscribed(self._path)

    async def subscribe(
        self,
        on_change_callback: typing.Optional[
            typing.Callable[[shv.ValueClient, str, shv.SHVType], None]
            ] = None
    ) -> bool:
        """
        Subscribe to the signals on SHV Node's path.

        The method wraps the `shv.ValueClient.subscribe` method and optionally
        the `shv.ValueClient.on_change` method to set a callback handler. See
        the methods' documentation for more details.

        Args:
            on_change_callback (Callable[[shv.ValueClient, str, shv.SHVType],\
            None], optional): A callback handler to be invoked when a signal\
                on the SHV Node's path is issued. Defaults to None.

        Returns:
            bool: Returns `True` if the subscription was successful,
            otherwise `False`.
        """
        assert self._assert_client_connected(self._client)
        if on_change_callback is not None:
            self._client.on_change(self._path, on_change_callback)
        if self._client.is_subscribed(self._path):
            return True
        sub_self = shv.RpcSubscription(self._path)
        sub_self_resp = await self._client.subscribe(sub_self)
        self._subs.append(sub_self)
        sub_children = shv.RpcSubscription(f'{self._path}/**')
        sub_children_resp = await self._client.subscribe(sub_children)
        self._subs.append(sub_children)
        return sub_self_resp and sub_children_resp

    async def unsubscribe(self) -> bool:
        """
        Unsubscribe from the signals on SHV Node's path.

        The method wraps the `shv.ValueClient.unsubscribe` method and
        optionally the `shv.ValueClient.on_change` method to remove
        the callback handler. See the methods' documentation for more details.

        Returns:
            bool: Returns `True` if the unsubscription was successful,
            otherwise `False`.
        """
        assert self._assert_client_connected(self._client)
        try:
            self._client.on_change(self._path, None)
        except KeyError:
            pass
        if self._client.is_subscribed(self._path) and self._subs:
            resps = []
            for sub in self._subs:
                resps.append(await self._client.unsubscribe(sub))
            self._subs.clear()
            return all(resps)
        return True

    async def call(
        self,
        method: str,
        param: shv.SHVType = None,
        call_attempts: int | None = None,
        call_timeout: float | None = None,
        user_id: str | None = None
    ) -> shv.SHVType:
        """
        Call a method on the SHV Node with the given parameters.

        The method wraps the `shv.ValueClient.call` method. See the method's
        documentation for more details.

        Args:
            method (str): The name of the method to call.
            param (shv.SHVType, optional): Parameter passed to the called\
                method. Defaults to None.
            call_attempts (int | None, optional): Amount of attempts to call\
                the method if it fails. Defaults to None (no retries).
            call_timeout (float | None, optional): Timeout for the method\
                call. Defaults to None (no timeout).
            user_id (str | None, optional): UserID added to the method call\
                request. Defaults to None.

        Returns:
            shv.SHVType: The response from the method call.
        """
        assert self._assert_client_connected(self._client)
        resp = await self._client.call(
            path=self._path,
            method=method,
            param=param,
            call_attempts=call_attempts,
            call_timeout=call_timeout,
            user_id=user_id
            )
        if method not in self._dir_exists_cache:
            self._dir_exists_cache[method] = True
        return resp

    async def ls(self) -> list[str]:
        """
        List child nodes of the SHV Node.

        The method wraps the `shv.ValueClient.ls` method. See the method's
        documentation for more details.

        Returns:
            list[str]: A list of child nodes' paths.
        """
        assert self._assert_client_connected(self._client)
        return await self._client.ls(self._path)

    async def dir(self, details: bool = False) -> list[shv.RpcMethodDesc]:
        """
        List available methods of the SHV Node.

        The method wraps the `shv.ValueClient.dir` method. See the method's
        documentation for more details.

        Args:
            details (bool, optional): If True, returns detailed information\
                about the methods. Defaults to False.

        Returns:
            list[shv.RpcMethodDesc]: A list of node's method descriptions.
        """
        assert self._assert_client_connected(self._client)
        return await self._client.dir(self._path, details)

    async def dir_exists(self, method: str) -> bool:
        """
        Check if the method exists on the SHV Node.

        Args:
            method (str): The name of the method to check.

        Returns:
            bool: Returns `True` if the method exists, otherwise `False`.
        """
        assert self._assert_client_connected(self._client)
        if method not in self._dir_exists_cache:
            exists = await self._client.dir_exists(self._path, method)
            self._dir_exists_cache[method] = exists
            return exists
        return self._dir_exists_cache[method]


class SHVPropertyNode(SHVNode):
    """
    A SHV Property Node representation.

    The class is a base for all SHV Property Node representations (a node
    is considered a property node if it has a value associated with it).
    It provides a similar API to the `shv.ValueClient` class, but
    it is centered around a single SHV Node in the SHV tree.
    """

    @property
    def cached_value(self) -> shv.SHVType:
        """
        The cached value of the node. May be `None` if
        the node is not connected or is not subscribed for the updates.
        """
        if self._client is None or self._path not in self._client:
            return None
        return self._client[self._path]

    async def get(self, max_age: float = 0) -> shv.SHVType:
        """
        Get the value associated with the property node from the server.

        The method wraps the `shv.ValueClient.prop_get` method.
        See the method's documentation for more details.

        Args:
            max_age (float, optional): Maximum age of the cached value\
                in seconds. If the cached value is older than the specified\
                age, the value is fetched from the server. Defaults to 0.

        Returns:
            shv.SHVType: The value associated with the node.
        """
        assert self._assert_client_connected(self._client)
        return await self._client.prop_get(self._path, max_age)

    async def value_change_wait(
        self,
        value: shv.SHVType = None,
        timeout: float | int | None = 5,
        get_period: float = 1.0
    ) -> shv.SHVType:
        """
        Wait for the value of the node to change.

        The method wraps the `shv.ValueClient.prop_change_wait` method. See
        the method's documentation for more details.

        Args:
            value (shv.SHVType, optional): The intial value to compare\
                against. If None, the method waits for any value change.
            timeout (float | int | None, optional): The maximum time in seconds
                to wait for the value to change. If None, the method will wait\
                Indefinitely until the value changes. Defaults to 5 seconds.
            get_period (float, optional): The interval in seconds to wait\
                between checks of the value. Defaults to 1 second.

        Returns:
            shv.SHVType: The value at the moment the value changes.

        Raises:
            TimeoutError: If the value does not change within the specified\
                timeout.
        """
        assert self._assert_client_connected(self._client)
        return await self._client.prop_change_wait(
            path=self._path,
            value=value,
            timeout=timeout,
            get_period=get_period
            )

    async def value_fetch_forever(self, get_period: float) -> None:
        """
        Continuously fetch the node's value. The value is fetched either
        upon an issued signal or when if the max update interval is reached.

        The method wraps the `shv.ValueClient.prop_change_wait` method.

        Args:
            get_period (float): Maximum interval (in seconds) to wait\
                for a signal before explicitly checking the value.
        """
        assert self._assert_client_connected(self._client)
        while True:
            await self._client.prop_change_wait(
                path=self._path,
                value=None,
                timeout=None,
                get_period=get_period
                )


class SHVPropertySetterNode(SHVPropertyNode):
    """
    A SHV Property Setter Node representation.

    The class is a base for all SHV Property Setter Node representations
    (a node is considered a property setter node if it has a value associated
    with it and allows for setting the value). It provides a similar API to
    the `shv.ValueClient` class, but it is centered around a single SHV Node
    in the SHV tree.
    """

    async def set(self, value: shv.SHVType, update: bool = False) -> None:
        """
        Set the given value associated to the node on the server.

        The method wraps the `shv.ValueClient.prop_set` method.
        See the method's documentation for more details.

        Args:
            value (shv.SHVType): The value to be set on the node.
            update (bool, optional): Update the cached value with\
                the new value. Defaults to False.
        """
        assert self._assert_client_connected(self._client)
        await self._client.prop_set(self._path, value, update)


class SHVStatusNode(SHVPropertyNode, ABC):
    """
    A base SHV System G3 Device Status Node representation. A status node is
    similar to a property node. Its value is a 32-bit integer that represents
    the device's status. It provides a similar API to the `shv.ValueClient`
    class, but it is centered around a single SHV Node in the SHV tree.
    It also implements additional methods for status inspection and waiting
    for specific status conditions.

    Every SHVStatusNode implementation should provide a `BitAlias` and
    `BitMask` enum classes that define the status bits and masks. The
    `inspect` method should be implemented to parse the status integer
    into a dictionary with the `BitAlias` enum members as keys and boolean
    flags as values.
    """

    @enum.unique
    class BitAlias(enum.IntFlag):
        pass

    @enum.unique
    class BitMask(enum.IntFlag):
        pass

    async def get(self, max_age: float = 0) -> shv.SHVUInt:
        """
        Get the status value associated with the property node from the server.

        The method wraps the `shv.ValueClient.prop_get` method.
        See the method's documentation for more details.

        Args:
            max_age (float, optional): Maximum age of the cached value\
                in seconds. If the cached value is older than the specified\
                age, the value is fetched from the server. Defaults to 0.

        Returns:
            shv.SHVUInt: The status value associated with the node.
        """
        value = await super().get(max_age)
        assert isinstance(value, shv.SHVUInt), value
        return value

    @property
    def cached_value(self) -> shv.SHVUInt | None:
        """
        The cached value of the node. The value is expected to be a 32-bit
        unsigned integer. The value may be `None` if
        the node is not connected or is not subscribed for the updates.
        """
        value = super().cached_value
        assert value is None or isinstance(value, shv.SHVUInt), value
        return value

    @staticmethod
    def is_status_equal(
        status: int, equal_to: int, mask: int | None = None
    ) -> bool:
        """
        Check if the status is equal to the provided value.

        Args:
            status (int): The status value to be checked.
            equal_to (int): The value to compare the status to.
            mask (int | None, optional): The mask to apply to the status\
                value before comparison. Defaults to None.

        Raises:
            TypeError: If the provided status masking fails.

        Returns:
            bool: Returns `True` if the status is equal to the provided value,\
                otherwise `False`.
        """
        if mask is None:
            return status == equal_to
        try:
            return (status & mask) == equal_to
        except TypeError as err:
            err.add_note(
                f'Failed to mask status "{status}" '
                f'(type "{type(status).__name__}") with '
                f'mask "{mask}" (type "{type(mask).__name__}").'
                )
            raise err

    @classmethod
    @abstractmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:
        """
        Parse the status integer into a dictionary with the `BitAlias` enum
        members as keys and boolean flags of whether specific states within
        the status are set or not as values.

        Args:
            status (int): The status integer to be parsed.

        Returns:
            dict[BitAlias, bool]: A dictionary with the parsed status data.
        """
        return {}

    @classmethod
    def _validate_state(
        cls,
        state: int,
        inspected_status_keys: typing.Collection[BitAlias]
    ) -> BitAlias:
        """
        Validate a given state against the current status.

        This method checks if the given state is a valid `BitAlias` enum member
        for this status `SHVNode` implementation and if it is present in
        the dictionary returned by the `inspect` method.

        Args:
            state: The state to be validated. It should correspond to a member\
                of the `BitAlias` enum.
            inspected_status: The current parsed status dictionary with\
                `BitAlias` members as keys and boolean flags as values.

        Raises:
            ValueError: If the state does not correspond to a valid `BitAlias`\
                enum member or if it is not present in the status dictionary.

        Returns:
            BitAlias: The validated state as the `BitAlias` enum member.
        """
        try:
            state = cls.BitAlias(state)
        except ValueError as err:
            err.add_note(
                f'State "{state}" in not listed among the '
                f'{cls.__name__}\'s BitAlias enum membres.'
                )
            raise err
        if state not in inspected_status_keys:
            raise ValueError(
                f'Cannot inspect for the state "{state}" '
                f'(parsing for "{state}" is not implemented in '
                f'{cls.__name__}\'s "inspect" method).'
                )
        return state

    @classmethod
    def _validate_states(
        cls,
        states: typing.Iterable[int] | None,
        inspected_status_keys: typing.Collection[BitAlias]
    ) -> list[BitAlias]:
        """
        Format and validate a list of states.

        This method takes an iterable of states and validates each state. It
        checks if each state corresponds to a valid `BitAlias` enum member and
        if it is present in the dictionary returned by the `inspect` method.
        If no states are provided, it returns an empty list.

        Args:
            states: The states to be formatted. Each state should correspond\
                to a member of the `BitAlias` enum.
            status: The current status dictionary.

        Returns:
            list[BitAlias]: A list of validated states. If no states\
                are provided, an empty list is returned.
        """
        if not states:
            return []
        return [
            cls._validate_state(state, inspected_status_keys)
            for state in states
            ]

    def _check_if_any_state_set(
        self,
        states: typing.Iterable[BitAlias],
        inspected_status: typing.Mapping[BitAlias, bool],
    ) -> bool:
        """
        Check if any of the provided states is set.

        Args:
            states: An iterable of states to be checked.
            inspected_status: The current parsed status dictionary with\
                `BitAlias` members as keys and boolean flags as values.

        Returns:
            bool: Returns `True` if any of the provided states is set,\
                otherwise `False`.
        """
        if not states:
            return True
        return any(inspected_status[state] for state in states)

    @staticmethod
    def _check_if_states_set(
        states_any_true: list[BitAlias],
        states_any_false: list[BitAlias],
        states_all_true: list[BitAlias],
        states_all_false: list[BitAlias],
        inspected_status: typing.Mapping[BitAlias, bool],
    ) -> bool:
        """
        Check if all of the provided states are set to the expected values.

        Args:
            states_any_true: An iterable of states, from which at least one\
                should be set to `True`.
            states_any_false: An iterable of states, from which at least one\
                should be set to `False`.
            states_all_true: An iterable of states, all of which should be\
                set to `True`.
            states_all_false: An iterable of states, all of which should be\
                set to `False`.
            inspected_status: The current parsed status dictionary with\
                `BitAlias` members as keys and boolean flags as values\
                describingwhether the state is set or not.

        Returns:
            bool: Returns `True` if all of the provided states are (not) set,\
                otherwise `False`.
        """
        if (
            states_any_true and
            all(inspected_status[state] is False for state in states_any_true)
        ):
            return False
        if (
            states_any_false and
            all(inspected_status[state] is True for state in states_any_false)
        ):
            return False
        if (
            states_all_true and
            any(inspected_status[state] is False for state in states_all_true)
        ):
            return False
        if (
            states_all_false and
            any(inspected_status[state] is True for state in states_all_false)
        ):
            return False
        return True

    @classmethod
    def is_status_set_to(
        cls,
        status: int,
        any_true: typing.Iterable[int | BitAlias] | None = None,
        any_false: typing.Iterable[int | BitAlias] | None = None,
        all_true: typing.Iterable[int | BitAlias] | None = None,
        all_false: typing.Iterable[int | BitAlias] | None = None
    ) -> bool:
        """
        Check if specified status conditions are met for a given status value.

        The method checks if specific status bits are set according to
        the provided conditions.

        The checks are performed by utilizing a node-specific `BitAlias` enum
        and `inspect` method implementations. Provided state conditions are
        validated and checked against the parsed status bits dictionary.
        If no conditions are provided, it returns `True`.

        Args:
            status: The status value to check.
            any_true: States that should be `True` for at least one of them.\
                If None, this condition is ignored. Default is None.
            any_false: States that should be `False` for at least one of them.\
                If None, this condition is ignored. Default is None.
            all_true: States that should all be `True`.\
                If None, this condition is ignored. Default is None.
            all_false: States that should all be `False`.\
                If None, this condition is ignored. Default is None.

        Returns:
            bool: Returns `True` if all specified conditions are met or\
                if no conditions are provided, otherwise `False`.
        """
        inspected = cls.inspect(status=status)
        inspected_keys = inspected.keys()
        return cls._check_if_states_set(
            states_any_true=cls._validate_states(any_true, inspected_keys),
            states_any_false=cls._validate_states(any_false, inspected_keys),
            states_all_true=cls._validate_states(all_true, inspected_keys),
            states_all_false=cls._validate_states(all_false, inspected_keys),
            inspected_status=inspected
            )

    async def status_change_wait(
        self,
        status: int | None = None,
        any_true: typing.Iterable[int | BitAlias] | None = None,
        any_false: typing.Iterable[int | BitAlias] | None = None,
        all_true: typing.Iterable[int | BitAlias] | None = None,
        all_false: typing.Iterable[int | BitAlias] | None = None,
        timeout: float | int | None = 5,
        get_period: float = 1
    ) -> shv.SHVUInt:
        """
        Wait for specified status conditions to be met within a given timeout.

        The method periodically checks if specific status bits are set
        according to the provided conditions. If no conditions are provided,
        the method waits for the status to change to any value.

        The checks are performed by utilizing a node-specific `BitAlias` enum
        and `inspect` method implementations. Provided state conditions are
        validated and checked against the parsed status bits dictionary.

        Args:
            status: The initial status value to start checking from. If None,\
                the first status value update is awaited. Default is None.
            any_true: States that should be `True` for at least one of them.\
                If None, this condition is ignored. Default is None.
            any_false: States that should be `False` for at least one of them.\
                If None, this condition is ignored. Default is None.
            all_true: States that should all be `True`.\
                If None, this condition is ignored. Default is None.
            all_false: States that should all be `False`.\
                If None, this condition is ignored. Default is None.
            timeout: The maximum time in seconds to wait for the status\
                to match the specified conditions. Default is 5 seconds.\
                If None, the method will wait indefinitely until\
                the conditions are met.
            get_period: The interval in seconds to wait between checks\
                of the status conditions. Default is 1 second.

        Raises:
            TimeoutError: If the conditions are not met within\
                the specified timeout.

        Returns:
            shv.SHVUInt: The status\
                at the moment all specified conditions are met.
        """
        assert self._assert_client_connected(self._client)
        # validate the provided states
        inspected = self.inspect(status=0)
        states_any_true = self._validate_states(any_true, inspected.keys())
        states_any_false = self._validate_states(any_false, inspected.keys())
        states_all_true = self._validate_states(all_true, inspected.keys())
        states_all_false = self._validate_states(all_false, inspected.keys())
        # start polling the status
        start_time = time.monotonic()
        while True:
            # wait for the status to change
            status = await self.value_change_wait(  # type: ignore
                value=status,
                timeout=timeout,
                get_period=get_period
                )
            # check if the status matches the expected states
            assert isinstance(status, shv.SHVUInt)
            inspected = self.inspect(status=status)
            if self._check_if_states_set(
                states_any_true,
                states_any_false,
                states_all_true,
                states_all_false,
                inspected
            ):
                return status
            # adjust the timeout for the next wait iteration
            if timeout is not None and timeout != float('inf'):
                timeout = timeout - (time.monotonic() - start_time)


class SHVDigitalInputTestNode(SHVNode):
    """
    A SHV Digital Input Test Node representation. The node implements
    a digital test input API: a `value` property.
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.value = SHVPropertyNode(f'{path}/value')
        """[BOOL] Value of the digital input."""


class SHVDigitalOutputTestNode(SHVNode):
    """
    A SHV Digital Output Test Node representation. The node implements
    a digital test output API: a `value` property and `setTrue`, `setFalse`,
    `setPulse`, and `reset` methods.
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.value = SHVPropertyNode(f'{path}/value')
        """[BOOL] Value of the digital output."""

    async def set_true(self, **kwargs) -> shv.SHVType:
        """Set the output to TRUE (logical 1)."""
        return await self.call('setTrue', **kwargs)

    async def set_false(self, **kwargs) -> shv.SHVType:
        """Set the output to FALSE (logical 0)."""
        return await self.call('setFalse', **kwargs)

    async def set_pulse(self, **kwargs) -> shv.SHVType:
        """Set pulse of logical 1 to the output for duration of 100ms."""
        return await self.call('setPulse', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset output to default state (FALSE, logical 0)."""
        return await self.call('reset', **kwargs)


class SHVDigitalOutputComplTestNode(SHVNode):
    """
    A SHV Digital Complementary Output Test Node representation. The node
    implements a digital test complementary output API: a `value` property and
    `setTrue`, `setFalse`, `setPulse`, and `reset` methods.
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.value = SHVPropertyNode(f'{path}/value')
        """[BOOL] Value of the digital output."""

    async def set_true(self, **kwargs) -> shv.SHVType:
        """Set output to TRUE (NO = 1, NC = 0)."""
        return await self.call('setTrue', **kwargs)

    async def set_false(self, **kwargs) -> shv.SHVType:
        """Set output to FALSE (NO = 0, NC = 1)."""
        return await self.call('setFalse', **kwargs)

    async def set_pulse(self, **kwargs) -> shv.SHVType:
        """
        Set pulse of logical 1 (NO = 1, NC = 0) to the output
        for duration of 100ms.
        """
        return await self.call('setPulse', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset output to default state (FALSE, NO = 0, NC = 1)."""
        return await self.call('reset', **kwargs)

    async def set_error_compl(self, **kwargs) -> shv.SHVType:
        """Set both outputs to TRUE (NO = 1, NC = 1)."""
        return await self.call('setErrorCompl', **kwargs)


class SHVAnalogInputTestNode(SHVNode):
    """
    A SHV Analog Input Test Node representation. The node implements
    an analog test input API: a `value` property.
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.value = SHVPropertyNode(f'{path}/value')
        """[REAL] Value of the analog input."""


class SHVAnalogOutputTestNode(SHVNode):
    """
    A SHV Analog Output Test Node representation. The node implements
    an analog test output API: a `value` property and `reset` method.
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.value = SHVPropertyNode(f'{path}/value')
        """[REAL] Value of the analog output."""

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset output to default state (value = 0.00)."""
        return await self.call('reset', **kwargs)
