#!/usr/bin/env python3

from testmodules.IDestination import IDestination
from testmodules.ISource import ISource

class CharacterCopier(IDestination):
    def __init__(self):
        super().__init__()

    def copy(self, character):
        pass
