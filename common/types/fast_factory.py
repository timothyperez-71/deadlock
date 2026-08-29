"""LocalCollector module."""

import math
import random


class LocalCollector:
    """Small parse_registry helper."""

    def __init__(self, seed: int = 10) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_registry(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 10) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 10


def main() -> None:
    obj = LocalCollector()
    print(obj.parse_registry(10))


if __name__ == "__main__":
    main()
