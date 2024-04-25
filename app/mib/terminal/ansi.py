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
    color: dict[str, str] = {
        'black': '0',
        'red': '1',
        'green': '2',
        'yellow': '3',
        'blue': '4',
        'magenta': '5',
        'cyan': '6',
        'white': '7'
    }

    esc = '\u001b'

    formatted = ''

    if fgColor is not None:
        try:
            fg = color[fgColor.lower()]
        except KeyError as exc:
            raise TypeError(f'Foreground color specified not valid: {fgColor}') from exc

        formatted += f'{esc}[3{fg}m'

        if fgBright:
            formatted += ',1m'

    if bgColor is not None:
        try:
            bg = color[bgColor.lower()]
        except KeyError as exc:
            raise TypeError(f'Background color specified not valid: {bgColor}') from exc

        formatted += '{esc}[4{bg}m'

        if bgBright:
            formatted += ',1m'

    if bold:
        formatted += f'{esc}[1m'
    if underline:
        formatted += f'{esc}[4m'
    if reverse:
        formatted += f'{esc}[7m'

    formatted += f'{text}{esc}[0m'

    return formatted

def unstyle(text: str) -> str:
    """
    Remove ANSI styles from text
    """

    esc = '\u001b'

    # Strip colors
    i = 0
    while i < 8:
        text = text.replace(f'{esc}3{i}m,1m', '')
        text = text.replace(f'{esc}4{i}m,1m', '')
        text = text.replace(f'{esc}3{i}m', '')
        text = text.replace(f'{esc}4{i}m', '')

    # strip decorations (bold, underline, reverse)
    text = text.replace(f'{esc}[1m', '')
    text = text.replace(f'{esc}[4m', '')
    text = text.replace(f'{esc}[7m', '')

    # Remove reset
    text = text.replace(f'{esc}[0m', '')

    return text
