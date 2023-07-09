#!/usr/bin/env python3 

class HeavyMetalBakeSale:
    def __init__(self):
        self.store = {}
        self.expected_change = 0.00

    def init_store(self):
        
        self.store = {
            'B': {
                'Brownie': '0.75',
                'Quantity': '48',
                'Purchase Code': 'B'
            },
            'M': {
                'Muffin': '1.00',
                'Quantity': '36',
                'Purchase Code': 'M'
            },
            'C': {
                'Cake Pop': '1.35',
                'Quantity': '24',
                'Purchase Code': 'C'
            },
            'W': {
                'Water': '1.50',
                'Quantity': '30',
                'Purchase Code': 'W'
            },

        }

    def purchase_items(self, items_list):
        if not self.check_for_items_valid(items_list):
            return False

        self.reduce_amount(items_list)        

        return True

    def check_for_items_valid(self, items_list):
        for item in items_list:
            if item in self.store:
                continue
            else:
                return False

        return True

    def quantity_available(self, item):
        if int(self.store[item]['Quantity']) < 1:
            return False
        else:
            return True

    def reduce_amount(self, items_list):
        for item in items_list:
           self.store[item]['Quantity'] = int(self.store[item]['Quantity']) - 1
           self.store[item]['Quantity'] = str(self.store[item]['Quantity'])
        
    def get_total(self, items_list):
        for item in items_list:
            pass

