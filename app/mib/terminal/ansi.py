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
) -> str:
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

    formatted = ''

    if fgColor is not None:
        try:
            fg = color[fgColor.lower()]
        except KeyError:
            raise Exception(f'Foreground color specified not valid: {fgColor}')

        formatted += '\u001b[3{fg}m'

        if fgBright:
            formatted += ',1m'

    if bgColor is not None:
        try:
            bg = color[bgColor.lower()]
        except KeyError:
            raise Exception(f'Background color specified not valid: {bgColor}')

        formatted += '\u001b[4{bg}m'

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

def unstyle(text: str) -> str:
    """
    Remove ANSI styles from text
    """

    # Strip colors
    i = 0
    while i < 8:
        text = text.replace(f'\u001b3{i}m,1m', '')
        text = text.replace(f'\u001b4{i}m,1m', '')
        text = text.replace(f'\u001b3{i}m', '')
        text = text.replace(f'\u001b4{i}m', '')

    # strip decorations (bold, underline, reverse)
    text = text.replace('\u001b[1m', '')
    text = text.replace('\u001b[4m', '')
    text = text.replace('\u001b[7m', '')

    # Remove reset
    text = text.replace('\u001b[0m', '')

    return text
