"""Synthetic normalized labels and integer arithmetic, not production code."""


def display_label(value: str) -> str:
    return value.strip()


def total_cents(amounts: list[int]) -> int:
    return sum(amounts)
