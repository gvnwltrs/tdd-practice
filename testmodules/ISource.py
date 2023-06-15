#!/usr/bin/env python3

from typing import TypeVar, Generic

T = TypeVar('T')

class ISource(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value
