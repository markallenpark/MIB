from mib.irc import style


def parse(base_type: str, protocol: str, message: str) -> dict:
    match base_type:
        case 'privmsg':
            return privmsg(protocol, message)
        case 'notice':
            return notice(protocol, message)
        case _:
            return {}


def privmsg(protocol: str, message: str) -> dict:
    source = get_source(protocol)
    target = get_target(protocol)
    message_type = 'message'  # sensible default value

    if message.startswith(chr(1) + "ACTION "):
        message_type = 'emote'
        message = message.strip(chr(1) + "ACTION ")
        message = message.strip(chr(1))
    elif message.startswith(chr(1)):
        message_type = 'ctcp'
        message = message.strip(chr(1))

    message = style.remove(message)
    args = message.split()

    return {
        'type': message_type,
        'source': source,
        'target': target,
        'message': message,
        'arguments': args
    }


def notice(protocol: str, message: str) -> dict:
    source = get_source(protocol)
    target = get_target(protocol)
    notice_type = 'notice'

    if message.startswith(chr(1)):
        notice_type = 'ctcp_reply'
        message = message.strip(chr(1))

    message = style.remove(message)
    args = message.split()

    return {
        'type': notice_type,
        'source': source,
        'target': target,
        'notice': message,
        'arguments': args
    }


def get_source(protocol: str) -> dict:
    source = protocol.split()[0]

    if '@' not in source:
        return {
            'type': 'server',
            'hostname': source
        }

    source = source.split('@')
    user = source[0].split('!')
    host = source[1]

    nickname = user[0]
    username = user[1]

    return {
        'type': 'user',
        'nickname': nickname,
        'username': username,
        'hostname': host
    }


def get_target(protocol: str) -> dict:
    target = protocol.split()[2]

    if target.startswith('#'):
        target_type = "channel"
    else:
        target_type = "user"

    return {
        'type': target_type,
        'target': target
    }
