"""
ANSI Module

Handles ANSI escape codes for terminal formatting and manipulation
"""

def style(
        text: str,
        fgColor: str = None,
        fgBright: bool = False,
        bgColor: str = None,
        bgBright: bool = False
):
    """
    Colorize terminal output
    """
    color: dict[str, str] {
        'black': '0',
        'red': '1',
        'green': '2',
        'yellow': '3',
        'blue': '4',
        'magenta': '5',
        'cyan': '6',
        'white': '7',
    }

    fgCode = '3'
    bgCode = '4'
    reset = '\u001b[0m'

    formatted = ''

    if fgColor is not None:
        try:
            fg = color[fgColor.lower()]
        except KeyError:
            raise Exception(f'Foreground color specified not valid: {fgColor}')

        formatted += '\u001b[{fgCode}{fg}m'

        if fgBright:
            formatted += ',1m'

    if bgColor is not None:
        try:
            bg = color[bgColor.lower()]
        except KeyError:
            raise Exception(f'Background color specified not valid: {bgColor}')

        formatted += '\u001b[{bgCode}{bg}m'

        if bgBright:
            formatted += ',1m'

    formatted += f'{text}{reset}'

    return formatted
