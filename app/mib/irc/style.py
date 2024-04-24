""" Handle IRC Formatting """

import re

def remove(text: str) -> str:
    """ Strip formatting from irc messages """

    attributes = [
        '\x0f',
        '\x02',
        '\x1d',
        '\x1f'
    ]

    for attribute in attributes:
        # Remove simple formatting attributes
        text = text.replace(attribute, '')

    # Remove color attributes
    text = re.sub(r'\x03(?P<fg>\d{2})(,(?P<bg>\d{2}))?', '', text)

    return text

def style(
        text: str,
        fg_color: int | str | None = None,
        bg_color: int | str | None = None,
        bold: bool = False,
        italics: bool = False,
        underline: bool = False,
        reset: bool = True
) -> str:
    """ Add formatting to IRC text """

    # Color Name -> Color ID
    color_to_id: dict[str, int] = {
        'white': 0,
        'black': 1,
        'blue': 2,
        'green': 3,
        'red': 4,
        'brown': 5,
        'purple': 6,
        'orange': 7,
        'yellow': 8,
        'lime': 9,
        'teal': 10,
        'aqua': 11,
        'royal': 12,
        'pink': 13,
        'grey': 14,
        'silver': 15,
    }

    # Attribute Name -> Control Code
    attributes: dict[str, str] = {
        'normal': '\x0f',
        'bold': '\x02',
        'italics': '\x1d',
        'underline': '\x1f',
        'color': '\x03'
    }

    prefix = ''

    if bold:
        prefix += attributes['bold']

    if italics:
        prefix += attributes['italics']

    if underline:
        prefix += attributes['underline']

    if fg_color is not None or bg_color is not None:
        prefix = f'{attributes['color']}'

        if fg_color is not None:
            if isinstance(fg_color, str):
                fg_color = color_to_id[str(fg_color)]
            prefix += str(fg_color)

        if bg_color is not None:
            if isinstance(bg_color, str):
                bg_color = color_to_id[str(bg_color)]
            prefix += f',{str(bg_color)}'

    suffix = ''
    if reset:
        suffix += attributes['normal']

    return f'{prefix}{text}{suffix}'
