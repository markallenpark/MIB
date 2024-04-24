"""
Parse IRC API Strings
"""

from datetime import datetime
from typing import Any

def parse(api: str) -> dict[str, Any]:
    """
    Parse IRC API Strings

    api: str    - API string from server
    """

    timestamp: str = datetime.now().isoformat()
    components: dict[str, str] = get_components(api)
    protocol_type: str = get_type(components['protocol'])

    return {
        'timestamp': timestamp,
        'api': components['api'],
        'type': protocol_type,
        'protocol': components['protocol'],
        'message': components['message'],
        'context': get_context(
            components['type'],
            components['protocol'],
            components['message'])
    }

def get_components(api: str) -> dict[str, str]:
    """
    Convert IRC API string into protocol and message components

    api: str    - raw api string
    """

    components = api.split(':', 2)

    try:
        # Catch any buffer bleed
        if ' ' not in components[1].strip() and components[1].strip() != '':
            api = api.replace(components[1], '')
            components = api.split(':', 2)
    except IndexError:
        pass

    try:
        prefix = components[0].strip()
    except IndexError:
        prefix = ''

    try:
        protocol = components[1].strip()
    except IndexError:
        protocol = ''

    try:
        message = components[2].strip()
    except IndexError:
        message = ''

    if prefix != '':
        message = protocol
        protocol = prefix

    return {
        "api": api,
        "protocol": protocol,
        "message": message
    }

def get_type(protocol: str) -> str:
    """
    Retrieve IRC Protocol type

    protocol: str   - Protocol portion of IRC API
    """
    if ' ' not in protocol:
        return protocol.lower()

    return protocol.split()[1].lower()

def get_context(base_type: str, protocol: str, message: str) -> dict:
    """
    Process events through specialized parsers
    """
    parsers: dict = {}

    try:
        return parsers[base_type](protocol, message)
    except KeyError:
        return {}
