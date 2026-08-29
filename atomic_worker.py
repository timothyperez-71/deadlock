"""SecureRegistry module."""

import math
import random


class SecureRegistry:
    """Small flush_scheduler helper."""

    def __init__(self, seed: int = 31) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_scheduler(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 31) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 31


def main() -> None:
    obj = SecureRegistry()
    print(obj.flush_scheduler(31))


if __name__ == "__main__":
    main()
