"""AsyncContext module."""

import math
import random


class AsyncContext:
    """Small resolve_manager helper."""

    def __init__(self, seed: int = 81) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_manager(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 81) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 81


def main() -> None:
    obj = AsyncContext()
    print(obj.resolve_manager(81))


if __name__ == "__main__":
    main()
