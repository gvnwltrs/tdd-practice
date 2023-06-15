from typing import TypeVar, Generic

T = TypeVar('T')

class IDestination(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

