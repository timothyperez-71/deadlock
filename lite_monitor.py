"""DynamicContext module."""

import math
import random


class DynamicContext:
    """Small run_factory helper."""

    def __init__(self, seed: int = 6) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_factory(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 6) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 6


def main() -> None:
    obj = DynamicContext()
    print(obj.run_factory(6))


if __name__ == "__main__":
    main()
