"""SmartLoader module."""

import math
import random


class SmartLoader:
    """Small flush_router helper."""

    def __init__(self, seed: int = 47) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_router(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 47) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 47


def main() -> None:
    obj = SmartLoader()
    print(obj.flush_router(47))


if __name__ == "__main__":
    main()
