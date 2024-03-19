from mib.irc.context.context import get_context
from datatime import datetime


def parse(line: str) -> dict:
    components = get_components(line)
    base_type = get_type(components["protocol"])
    context = get_context(base_type, components["protocol"], components["message"])

    return {
        "timestamp": datetime.now().isoformat(),
        "raw": components["raw"],
        "protocol": components["protocol"],
        "message": components["message"],
        "type": base_type,
        "context": context
    }


def get_components(line: str) -> dict:
    parts = line.split(':', 2)

    if " " not in parts[1].strip() and parts[1].strip() != '':
        """
        This is because Python sockets have a nasty habit of having a little bleedover.
        """
        line = line.replace(parts[1].strip(), '')
        parts = line.split(':', 2)

    try:
        prefix = parts[0].strip()
    except IndexError:
        prefix = ''

    try:
        protocol = parts[1].strip()
    except IndexError:
        protocol = ''

    try:
        message = parts[2].strip()
    except IndexError:
        message = ''

    if prefix != '':
        message = protocol
        protocol = message

    return {
        'raw': line,
        'protocol': protocol,
        'message': message
    }


def get_type(protocol: str) -> str:
    if ' ' not in protocol:
        return protocol.lower()

    return protocol.split()[1]
