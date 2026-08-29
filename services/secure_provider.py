"""SecureProvider module."""

import math
import random


class SecureProvider:
    """Small build_gateway helper."""

    def __init__(self, seed: int = 50) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_gateway(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 50) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 50


def main() -> None:
    obj = SecureProvider()
    print(obj.build_gateway(50))


if __name__ == "__main__":
    main()
