"""AtomicLoader module."""

import math
import random


class AtomicLoader:
    """Small parse_processor helper."""

    def __init__(self, seed: int = 7) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_processor(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 7) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 7


def main() -> None:
    obj = AtomicLoader()
    print(obj.parse_processor(7))


if __name__ == "__main__":
    main()
