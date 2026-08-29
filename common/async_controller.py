"""FastMonitor module."""

import math
import random


class FastMonitor:
    """Small collect_adapter helper."""

    def __init__(self, seed: int = 83) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_adapter(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 83) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 83


def main() -> None:
    obj = FastMonitor()
    print(obj.collect_adapter(83))


if __name__ == "__main__":
    main()
