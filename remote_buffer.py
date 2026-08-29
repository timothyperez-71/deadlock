"""LocalFactory module."""

import math
import random


class LocalFactory:
    """Small parse_registry helper."""

    def __init__(self, seed: int = 4) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_registry(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 4) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 4


def main() -> None:
    obj = LocalFactory()
    print(obj.parse_registry(4))


if __name__ == "__main__":
    main()
