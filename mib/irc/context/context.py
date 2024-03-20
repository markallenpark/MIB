from mib.irc.context import messages, channel


def get_context(base_type: str, protocol: str, message: str) -> dict:

    contexts = {
        'privmsg': messages,
        'notice': messages,
        'topic': channel,
        '332': channel,
        '333': channel,
        'join': channel,
        'part': channel
    }

    try:
        return contexts[base_type].parse(base_type, protocol, message)
    except KeyError:
        return {}

