import re


def remove(text: str) -> str:
    attributes = [
        '\x0f',
        '\x02',
        '\x1d',
        '\x1f'
    ]

    for attribute in attributes:
        """
        Remove simple formatting attributes
        """
        text = text.replace(attribute, '')

    """
    Remove color attributes
    """
    text = re.sub(r'\x03(?P<fg>\d{2})(,(?P<bg>\d{2}))?', '', text)

    return text
