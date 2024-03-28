from time import monotonic_ns


def monotonic_ms() -> int:
    return round(monotonic_ns() / 1000000)
