#!/usr/bin/env python3 

class HeavyMetalBakeSale:
    def __init__(self):
        self.store = {}
        self.expected_change = 0.00

    def init_store(self):
        
        self.store = {
            'B': {
                'Item': 'Brownie',
                'Price': '0.75',
                'Quantity': '48',
                'Purchase Code': 'B'
            },
            'M': {
                'Item': 'Muffin',
                'Price': '1.00',
                'Quantity': '36',
                'Purchase Code': 'M'
            },
            'C': {
                'Item': 'Cake Pop',
                'Price': '1.35',
                'Quantity': '24',
                'Purchase Code': 'C'
            },
            'W': {
                'Item': 'Water',
                'Price': '1.50',
                'Quantity': '30',
                'Purchase Code': 'W'
            },

        }

    def purchase_items(self, items_list, payment=0.00):
        if not self.check_for_items_valid(items_list):
            return False
        
        quantity = self.reduce_amount(items_list)        
        total_price = self.get_total(items_list)        

        if payment < total_price:
            return False, 'Not enough money.'

        change = round(abs(payment - total_price), 2)

        return True, change

    def check_for_items_valid(self, items_list):
        for item in items_list:
            if item in self.store:
                continue
            else:
                return False

        return True

    def quantity_available(self, item):
        if int(self.store[item]['Quantity']) < 1:
            print('{0} is out of stock'.format(item))
            return False
        else:
            return True

    def reduce_amount(self, items_list):
        for item in items_list:
           self.store[item]['Quantity'] = int(self.store[item]['Quantity']) - 1
           self.store[item]['Quantity'] = str(self.store[item]['Quantity'])
        
    def get_total(self, items_list):
        total_price = 0.00
        for item in items_list:
           total_price = total_price + float(self.store[item]['Price'])
        
        return total_price 
