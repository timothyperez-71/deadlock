"""AtomicSession module."""

import math
import random


class AtomicSession:
    """Small encode_engine helper."""

    def __init__(self, seed: int = 73) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_engine(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 73) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 73


def main() -> None:
    obj = AtomicSession()
    print(obj.encode_engine(73))


if __name__ == "__main__":
    main()
