from mib.irc.context import messages


def get_context(base_type: str, protocol: str, message: str) -> dict:

    match base_type:
        case 'privmsg' | 'notice':
            return messages.parse(base_type, protocol, message)
        case _:
            """ Default to empty context """
            return {}
