"""SharedLoader module."""

import math
import random


class SharedLoader:
    """Small parse_handler helper."""

    def __init__(self, seed: int = 35) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_handler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 35) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 35


def main() -> None:
    obj = SharedLoader()
    print(obj.parse_handler(35))


if __name__ == "__main__":
    main()
