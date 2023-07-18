#!/usr/bin/env python3 

class IPValidator:

    def __init__(self, ip_address='192.168.1.1'):
        self.ip_addr = ip_address.split('.')
        self.ValidateIpv4Address()

    def ValidateIpv4Address(self): 
        return self.valid_id_checker()

    def valid_id_checker(self):
        return self.valid_octet() and self.valid_num_octets()

    def valid_num_octets(self):
        if len(self.ip_addr) > 4 or len(self.ip_addr) < 4:
            return False
        return True

    def valid_octet(self):
        for octet in self.ip_addr:
            if int(octet) < 0 and int(octet) > 255:
                return False
        return True