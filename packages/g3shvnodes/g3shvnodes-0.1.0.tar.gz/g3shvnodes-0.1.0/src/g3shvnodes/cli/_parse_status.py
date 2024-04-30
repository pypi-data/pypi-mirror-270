import argparse
import typing

try:
    from rich.console import Console
    from rich.table import Table, box
    from rich.text import Text
except (ModuleNotFoundError, ImportError) as err:
    err.add_note(
        "Please install the 'rich' library to run the CLI script with "
        "'python -m pip install rich'."
        )
    raise err

from .. import all as g3shvnodes_all


def get_status_node_cls_name(device: str) -> str:
    return f'shv{device.strip().lower()}statusnode'


def get_device_name(status_node_cls_name: str) -> str:
    formatted = status_node_cls_name.strip().lower()
    return formatted.removeprefix('shv').removesuffix('statusnode')


def collect_status_node_clss() -> dict[str, type]:
    status_node_clss = {}
    for name, cls in vars(g3shvnodes_all).items():
        name_lower = name.lower()
        if name_lower.endswith('statusnode'):
            status_node_clss[get_device_name(name_lower)] = cls
    status_node_clss.pop('', None)  # SHVStatusNode is a generic class
    return status_node_clss


def uint(value: str) -> int:
    if value.endswith('u'):  # cpon uint suffix
        value = value.removesuffix('u')
    try:
        base = {'0b': 2, '0o': 8, '0x': 16}.get(value[:2], 10)
        return int(value, base=base)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f'"{value}" is not a valid integer of base {base}.'
            )
    except Exception as e:
        raise argparse.ArgumentTypeError(f'"{value}": {e}')


def parse_args(device_names: typing.Iterable[str]) -> argparse.Namespace:
    names = ', '.join(device_names)
    parser = argparse.ArgumentParser(
        description=(
            'description: inspect a System G3 device status value using '
            'the status node class of the device.'
            ),
        epilog=f"supported device names: {names}."
        )
    parser.add_argument(
        'device',
        type=str,
        help=(
            'Name of the device (case insensitive, no spaces, e.g. "gate", '
            '"SignalSymbol"). See supported device names below.'
            )
        )
    parser.add_argument(
        'status',
        type=uint,
        help=(
            'Status value (a positive 32-bit unsigned integer) to inspect. '
            'Supports decimal (e.g., "13"), binary (e.g., "0b1101"), octal '
            '(e.g., "0o15"), hexadecimal (e.g., "0xD") formats as well as '
            'cpon uint format with suffix "u" (e.g., "13u").'
            )
        )
    return parser.parse_args()


def build_analysis_table(status: int, inspected: dict) -> Table:
    # create and style table contents
    status_decimal_str, status_binary_str = f'{status}', f'{status:032b}'
    status_binary_text = Text()
    status_bits_set = []
    for i, bit in enumerate(status_binary_str):
        if bit == '1':
            status_bits_set.append(31 - i)  # bit positions from MSB = 0
            style = "green"
        else:
            style = "default"
        status_binary_text.append(bit, style=style)
        if (i + 1) % 8 == 0 and i + 1 != 32:  # add space every 8 bits
            status_binary_text.append(" ")
    bits_set_str = ', '.join(map(str, reversed(status_bits_set)))
    fields_text = Text()
    for field_name, field_value in inspected.items():
        field_text_str = f'{field_name.name} ({field_name.value})\n'
        style = "green" if field_value else "red"
        field_text = Text(field_text_str, style=style)
        fields_text.append_text(field_text)
    fields_text.remove_suffix('\n')
    # construct the table
    table = Table(box=box.ASCII2, show_header=False)
    table.add_column("Description", style="bold cyan")
    table.add_column("Value", style="default")
    # fill in the table
    table.add_row("Status (decimal)", status_decimal_str, end_section=True)
    table.add_row("Status (binary)", status_binary_text, end_section=True)
    table.add_row("Bits set", bits_set_str, end_section=True)
    table.add_row("Fields set", fields_text)
    return table


def main():
    console = Console()
    status_node_clss = collect_status_node_clss()
    args = parse_args(status_node_clss.keys())
    args.device = args.device.strip().lower()
    if args.device not in status_node_clss:
        console.print(
            f'Device "{args.device}" was not found in supported devices. '
            f'Please choose from: {", ".join(status_node_clss.keys())}.'
            )
        exit(1)
    if args.status < 0:
        console.print("Status value must be a positive 32-bit integer.")
        exit(1)
    status_node_cls = status_node_clss[args.device]
    try:
        inspected = status_node_cls.inspect(args.status)
    except AttributeError:
        cls_name = status_node_cls.__name__
        console.print(
            f'Failed to parse status value "{args.status}": '
            f'class "{cls_name}"" does not implement the "inspect" method.'
            )
        exit(1)
    except Exception as e:
        console.print(f'Failed to parse status value "{args.status}": {e}')
        exit(1)
    table = build_analysis_table(args.status, inspected)
    console.print(table)


if __name__ == '__main__':
    main()
