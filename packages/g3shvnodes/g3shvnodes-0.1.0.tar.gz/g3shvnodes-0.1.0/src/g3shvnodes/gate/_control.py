import enum
import itertools
import json
import shv

from ..node._node import (
    SHVNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


class SHVGateStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        FULL_MEMORY_ENABLED = 0
        """
        Request memory is enabled. Route requests that cannot be executed
        immediately are stored in the memory.
        """
        MEMORY_DISABLED = 90
        """
        Request memory is disabled. Route requests that cannot be executed
        immediately are discarded.
        """
        FOLLOW_UP_DISABLED = 91
        """
        Follow-up route requests are discarded (a follow-up request is
        a request for a route in the same direction as the route from
        the previous request).
        """
        ONLY_REQUESTABLE_ROUTES = 92
        """
        Request memory is enabled, but a request is stored in memory only
        if the corresponding route can be requested (i.e., the route is free
        and is not blocked externally).
        """
        SPAD = 1 << 24
        """
        Tram entry to the zone has been evaluated as potentially dangerous
        (SPAD - Signal Passed At Danger). For example, the tram passed the
        gate without a route in READY state (driver ignored the STOP signal).
        """
        ERROR_AT_GATE = 1 << 30
        """
        Any route starting at the gate is in the ERROR state or
        SPAD has been detected and has not been solved.
        """

    class BitMask(enum.IntFlag):
        MEMORY_MODE = 0xFF  # bits 0-7
        """
        Current mode of the gate request memory.
        """
        SPAD = 1 << 24
        """
        Tram entry to the zone has been evaluated as potentially dangerous
        (SPAD - Signal Passed At Danger). For example, the tram passed the
        gate without a route in READY state (driver ignored the STOP signal).
        """
        ERROR_AT_GATE = 1 << 30
        """
        Any route starting at the gate is in the ERROR state or
        SPAD has been detected and has not been solved.
        """

    @classmethod
    def is_full_memory_enabled(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FULL_MEMORY_ENABLED,
            mask=cls.BitMask.MEMORY_MODE
            )

    @classmethod
    def is_memory_disabled(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MEMORY_DISABLED,
            mask=cls.BitMask.MEMORY_MODE
            )

    @classmethod
    def is_follow_up_disabled(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FOLLOW_UP_DISABLED,
            mask=cls.BitMask.MEMORY_MODE
            )

    @classmethod
    def is_only_requestable_routes(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ONLY_REQUESTABLE_ROUTES,
            mask=cls.BitMask.MEMORY_MODE
            )

    @classmethod
    def is_spad(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SPAD,
            mask=cls.BitMask.SPAD
            )

    @classmethod
    def is_error_at_gate(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_AT_GATE,
            mask=cls.BitMask.ERROR_AT_GATE
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.FULL_MEMORY_ENABLED:
                cls.is_full_memory_enabled(status),
            cls.BitAlias.MEMORY_DISABLED:
                cls.is_memory_disabled(status),
            cls.BitAlias.FOLLOW_UP_DISABLED:
                cls.is_follow_up_disabled(status),
            cls.BitAlias.ONLY_REQUESTABLE_ROUTES:
                cls.is_only_requestable_routes(status),
            cls.BitAlias.SPAD:
                cls.is_spad(status),
            cls.BitAlias.ERROR_AT_GATE:
                cls.is_error_at_gate(status),
            }


class SHVGateControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVGateStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Gate status."""
        self.request_memory = SHVPropertySetterNode(
            path=f'{path}/requestMemory'
            )
        """
        [STRING] Gate request memory
        (all requests on the gate waiting to be processed).
        """
        self._counter = itertools.count(1)

    def generate_route_request(
        self,
        route: str,
        row_number: int | None = None,
        vehicle_id: str | None = None,
        line_number: str | None = None,
        request_id: str | None = None
    ) -> str:
        """Generate a JSON string for a route request.

        This method takes in parameters for a route request and returns a
        JSON string that represents the request sent to the gate memory. Note
        that this method cannot generate requests to delete a route record
        from the memory (such as '{"rowNumber":1, null}').

        Examples:

        >>> generate_route_request_string("R1")
        '{"rowNumber":1,"record":{"route":"R1"}}'

        >>> generate_route_request_string("R1", 2)
        '{"rowNumber":2,"record":{"route":"R1"}}'

        >>> generate_route_request_string("R1", 2, "V1", "L1")
        '{"rowNumber":2,"record":\
        {"route":"R1", "vehicleId":"V1","lineNumber":"L1"}}'

        >>> generate_route_request_string("R1", 2, "V1", "L1", "Req1")
        '{"rowNumber":2,"requestId":"Req1","record":\
        {"route":"R1", "vehicleId":"V1", "lineNumber":"L1"}}'

        Args:
            route (str): The name of the route.
            row_number (int | None, optional): The number of the row to be\
                inserted or replaced. If None, the next available row number\
                is used (maximum is 999). Defaults to None.
            vehicle_id (str | None, optional): The ID of the vehicle.\
                Defaults to None.
            line_number (str | None, optional): The ID of the tram line.\
                Defaults to None.
            request_id (str | None, optional): The ID of the request.\
                Defaults to None.

        Raises:
            ValueError: If the provided row_number is invalid\
                (nagative or more than 999).

        Returns:
            str: A JSON string representing the route request.
        """
        if row_number is None:
            row_number = next(self._counter)
            if row_number > 998:  # is 999
                self._counter = itertools.count(0)
        elif row_number < 0:
            raise ValueError("Gate memory row number cannot be negative.")
        elif row_number > 999:
            raise ValueError("Gate memory row number cannot exceed 999.")
        record = {}
        if route is not None:
            record["route"] = route
        if vehicle_id is not None:
            record["vehicleId"] = vehicle_id
        if line_number is not None:
            record["lineNumber"] = line_number
        result = {
            "rowNumber": row_number,
            "record": record,
            }
        if request_id is not None:
            result["requestId"] = request_id
        return json.dumps(result)

    def generate_row_deletion_request(self, row_number: int) -> str:
        """Generate a JSON string for a gate memory row deletion request.

        This method takes in a row number and returns a JSON string that
        represents a request to delete the route record from the memory.

        Examples:

        >>> generate_row_deletion_request(1)
        '{"rowNumber":1, "record":"null"}'

        Args:
            row_number (int): The number of the row to be deleted.

        Returns:
            str: A JSON string representing the route deletion request.
        """
        return json.dumps({"rowNumber": row_number, "record": "null"})

    async def reset_gate(self, **kwargs) -> shv.SHVType:
        """Reset the gate memory and cancel the currently active route."""
        return await self.call('resetGate', **kwargs)

    async def clear_memory(self, **kwargs) -> shv.SHVType:
        """Clear the gate memory."""
        return await self.call('clearMemory', **kwargs)

    async def enable_full_memory(self, **kwargs) -> shv.SHVType:
        """Enable the gate memory (remove all memory restrictions)."""
        return await self.call('enableFullMemory', **kwargs)

    async def disable_memory(self, **kwargs) -> shv.SHVType:
        """Disable the gate memory."""
        return await self.call('disableMemory', **kwargs)

    async def disable_follow_up(self, **kwargs) -> shv.SHVType:
        """Disable storing follow-up requests in the gate memory."""
        return await self.call('disableFollowup', **kwargs)

    async def insert_route(self, request: str, **kwargs) -> shv.SHVType:
        """Insert a new route request record into the gate memory.

        This method sends a request for a new route to the gate memory.
        Depending on the row number, it can either insert the route at
        a specific position (which will shift the memory content),
        or append the route at the end of the memory. If the row number
        is set to 0, the command will cancel all currently created routes.

        Args:
            request (str): A string with the route request data (vehicle ID,\
                route name, line number, request ID  row number, route name).

        Returns:
            shv.SHVType: The result of the gate memory request.
        """
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('insertRoute', param=request, **kwargs)

    async def change_route(self, request: str, **kwargs) -> shv.SHVType:
        """Change an existing route record in the gate memory.

        This method sends a request to change an existing route record to
        the gate memory. It requires both row number and request ID to be
        present in the request string to successfully change a route.
        If the request is not matched to any  memory row does not exist,
        the command is discarded. If the row number is set to 0, the command
        will cancel all currently created routes. If the row record is set to
        "null", e.g., '{"rowNumber":1, "record":"null"}', the specified row is
        deleted, and the memory content is shifted.

        Args:
            request (str): A string with the updated route record data\
                (vehicle ID, route name, line number, request ID  row number,\
                route name).

        Returns:
            shv.SHVType: The result of the gate memory request.
        """
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('changeRoute', param=request, **kwargs)
