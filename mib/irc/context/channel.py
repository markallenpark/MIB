from mib.irc import style
from datetime import datetime


def parse(base_type: str, protocol: str, message: str) -> dict:
    match base_type:
        case 'topic':
            return new_topic(protocol, message)
        case '332':
            return topic_current(protocol, message)
        case '333':
            return topic_created_by(protocol)
        case 'join':
            return join(protocol, message)
        case 'part':
            return part(protocol, message)
        case _:
            return {}


def get_source(hostmask: str) -> dict:
    source = hostmask.split('@')
    user = source[0].split('!')

    return {
        'nickname': user[0],
        'username': user[1],
        'hostmask': source[1]
    }


def new_topic(protocol: str, message: str) -> dict:
    args = protocol.split()
    source = get_source(args[0])
    channel = args[2]
    topic = style.remove(message)


def topic_created_by(protocol: str) -> dict:
    args = protocol.split()
    source = get_source(args[4])
    channel = args[3]
    created = datetime.fromisoformat(args[5]).isoformat()

    return {
        'created': created,
        'source': source,
        'channel': channel
    }


def topic_current(protocol: str, message: str) -> dict:
    args = protocol.split()
    source = get_source(args[0])
    channel = args[2]
    channel_topic = style.remove(message)

    return {
        'source': source,
        'channel': channel,
        'topic': channel_topic
    }


def join(protocol: str, message: str) -> dict:
    args = protocol.split()
    source = get_source(args[0])
    channel = message.strip()

    return {
        'source': source,
        'channel': channel
    }


def part(protocol: str, message: str) -> dict:
    args = protocol.split()
    source = get_source(args[0])
    channel = args[2]
    reason = style.remove(message).strip()

    return {
        'source': source,
        'channel': channel,
        'reason': reason
    }
