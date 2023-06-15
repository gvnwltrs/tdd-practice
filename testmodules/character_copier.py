#!/usr/bin/env python3

import testmodules.IDestination as IDestination
import testmodules.ISource as ISource

class CharacterCopier(ISource, IDestination):
    def __init__(self):
        pass

    def copy(self, character):
        pass
