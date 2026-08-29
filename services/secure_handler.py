"""CoreAdapter module."""

import math
import random


class CoreAdapter:
    """Small collect_parser helper."""

    def __init__(self, seed: int = 4) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_parser(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 4) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 4


def main() -> None:
    obj = CoreAdapter()
    print(obj.collect_parser(4))


if __name__ == "__main__":
    main()
