"""SmartCollector module."""

import math
import random


class SmartCollector:
    """Small run_provider helper."""

    def __init__(self, seed: int = 81) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_provider(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 81) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 81


def main() -> None:
    obj = SmartCollector()
    print(obj.run_provider(81))


if __name__ == "__main__":
    main()
