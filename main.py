#!/usr/bin/env python3 

import testmodules.one_hundred_doors as doors

if __name__ == '__main__':
    my_doors = doors.OneHundredDoors()
    my_doors.run_100_doors(100)
