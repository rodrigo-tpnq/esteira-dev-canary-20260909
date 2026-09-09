"""Synthetic normalized labels and formatted integer cents, not production code."""


def display_label(value: str) -> str:
    return value.strip()


def total_cents(amounts: list[int]) -> int:
    return sum(amounts)


def format_cents(amount: int) -> str:
    sign = "-" if amount < 0 else ""
    units, fraction = divmod(abs(amount), 100)
    return f"{sign}{units}.{fraction:02d}"
