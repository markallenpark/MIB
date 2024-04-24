"""
Time module
"""

from time import monotonic_ns

def monotonic_ms() -> int:
    """
    Convert monotonic_ns to milliseconds
    """

    return round(monotonic_ns() / 1000000)
