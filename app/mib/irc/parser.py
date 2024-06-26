"""
Parse IRC API Strings
"""

from datetime import datetime
from typing import Any
from mib.irc.context import chat

def parse(api: str) -> dict[str, Any]:
    """
    Parse IRC API Strings

    api: str    - API string from server
    """

    timestamp: str = datetime.now().isoformat()
    components: dict[str, str] = get_components(api)
    source: dict[str, str] = get_source(components['protocol'])
    protocol_type: str = get_type(components['protocol'])

    return {
        'timestamp': timestamp,
        'api': components['api'],
        'type': protocol_type,
        'protocol': components['protocol'],
        'message': components['message'],
        'source': source,
        'context': get_context(
            protocol_type,
            components['protocol'],
            components['message'])
    }

def get_components(api: str) -> dict[str, str]:
    """
    Convert IRC API string into protocol and message components

    api: str    - raw api string
    """

    components = api.split(':', 2)

    # Prevent buffer bleedover
    #
    # Changed to a while, just in case-- but it should only need to run through
    # once
    while components[0] != '' and components[0][-1] != ' ':
        print(f"[ERROR] Detected bleed in line: {api}")
        api = api.replace(components[0], '')
        print(f"[INFO] Bleed correction attempt : {api}")
        components = api.split(':', 2)

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

def get_source(protocol: str) -> dict[str, str]:
    """
    Get source of API call
    """
    if ' ' not in protocol:
        return {
            'type': 'network',
        }

    source = protocol.split()[1]

    if '@' not in source:
        return {
            'type': 'server',
            'host': source
        }

    mask = source.split('@')
    usermask = mask[0].split('!')
    hostmask = mask[1]

    return {
        'type': 'user',
        'nickname': usermask[0],
        'username': usermask[1],
        'host': hostmask
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
    parsers: dict = {
        'privmsg': chat.privmsg,
        'notice': chat.notice
    }

    try:
        return parsers[base_type](protocol, message)
    except KeyError:
        return {}
