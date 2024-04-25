"""
Message module
"""
from mib.irc import style

def privmsg(protocol: str, message: str) -> dict:
    """
    Handle PRIVMSG API strings
    """

    if message.startswith(chr(1)+'ACTION'):
        message = message.replace(chr(1)+'ACTION', '')
        message = message.strip(chr(1))
        message_type = 'action'
    elif message.startswith(chr(1)):
        message = message.strip(chr(1))
        message_type = 'ctcp'
    else:
        message_type = 'message'

    message = style.remove(message)

    return {
        'type': message_type,
        'message': message,
        'args': message.split(),
        'target': get_target(protocol)
    }

def notice(protocol: str, message: str) -> dict:
    """
    Handle NOTICE API strrings
    """

    if message.startswith(chr(1)):
        message = message.strip(chr(1))
        message_type = 'ctcp-reply'
    else:
        message_type = 'notice'

    message = style.remove(message)

    return {
        'type': message_type,
        'message': message,
        'args': message.split(),
        'target': get_target(protocol)
    }

def get_target(protocol: str) -> dict[str, str]:
    """
    Get message target
    """
    target = protocol.split()[2]

    if target[0].isalpha():
        target_type = 'nickname'
    else:
        target_type = 'channel'

    return {
        'type': target_type,
        'target': target
    }
