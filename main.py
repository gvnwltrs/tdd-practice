#!/usr/bin/env python3 

from testmodules.ip_validator import IPValidator

if __name__ == '__main__':
    ipv = IPValidator()

    ipv.valid_id_checker('192.168.1.1')