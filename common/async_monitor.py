"""SecureMonitor module."""

import math
import random


class SecureMonitor:
    """Small collect_resolver helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_resolver(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 54) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = SecureMonitor()
    print(obj.collect_resolver(54))


if __name__ == "__main__":
    main()
