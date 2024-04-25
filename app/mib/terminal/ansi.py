"""
ANSI Module

Handles ANSI escape codes for terminal formatting and manipulation
"""

def style(
        text: str,
        fgColor: str = None,
        fgBright: bool = False,
        bgColor: str = None,
        bgBright: bool = False,
        bold: bool = False,
        underline: bool = False,
        reverse: bool = False
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

    if bold:
        formatted += '\u001b[1m'
    if underline:
        formatted += '\u001b[4m'
    if reverse:
        formatted += '\u001b[7m'

    formatted += f'{text}\u001b[0m'

    return formatted
