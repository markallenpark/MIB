from mib.irc import command


def handle(event: dict) -> dict:
    match event['type']:
        case '001':
            return welcome()
        case 'ping':
            return pong(event['message'])
        case _:
            return {}


def welcome():
    return {
        "states": {
            "registered": True
        }
    }


def pong(message: str) -> dict:
    return {
        "commands": command.send_pong(message)
    }
