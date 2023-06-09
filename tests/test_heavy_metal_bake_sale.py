#!/usr/bin/env python3
# It is 1999 and a local metal band is looking to have a bake sale to raise funds for their new album. They have promised you a free CD if you make software to help run the sale; they are musicians not mathematicians after all.
#
# There are four items they would like to sell on this sale with specific prices and quantities of each:
#
# Item	Price	Quantity	Purchase Code
# Brownie	$0.75	48	B
# Muffin	$1.00	36	M
# Cake Pop	$1.35	24	C
# Water	$1.50	30	W
#
# The application must calculate the correct change to give a person if they overpay.
# If you do not have stock of an item, you cannot make the sale. Purchases are input as a comma delimited string.
# The Purchase Code from above will be used in the string to indicates which items are in the transaction.
#
# If all items are in stock - respond with a total amount.
# If an item is out of stock, respond with "X is out of stock" where X is the item out of stock.
# After the total, prompt for amount paid.
# If the amount is equal to or greater than the amount due display change due.
# If the amount is less than the amount due it responds with “Not enough money.”

import unittest

import testmodules.heavy_metal_bake_sale as HeavyMetalBakeSale 

class TestHeavyMetalBakeSale(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        cls.hmb.init_store()

    def tearDown(self):
        self.hmb = None 

    def test_for_inventory(self):
        expected_result = len(self.hmb.store)
        self.assertTrue(expected_result) 

    def test_for_brownie(self):
        expected_result = {'Item': 'Brownie', 'Price': '0.75', 'Quantity': '48', 'Purchase Code': 'B'}
        self.assertEqual(expected_result, self.hmb.store['B'])
        
    def test_for_muffin(self):
        expected_result = {'Item': 'Muffin', 'Price': '1.00', 'Quantity': '36', 'Purchase Code': 'M'}
        self.assertEqual(expected_result, self.hmb.store['M'])

    def test_for_cake_pop(self):
        expected_result = {'Item': 'Cake Pop', 'Price': '1.35', 'Quantity': '24', 'Purchase Code': 'C'}
        self.assertEqual(expected_result, self.hmb.store['C'])

    def test_for_water(self):
        expected_result = {'Item': 'Water', 'Price': '1.50', 'Quantity': '30', 'Purchase Code': 'W'}
        self.assertEqual(expected_result, self.hmb.store['W'])

    def test_for_purchase_made(self):
        items_list = ['B', 'B', 'W']
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        hmb.reduce_amount(items_list)
        purchase_made = hmb.purchase_items(items_list)
        self.assertTrue(purchase_made)

    def test_for_valid_purchase_item(self):
        items_list = ['B', 'B', 'W']
        items_valid = self.hmb.check_for_items_valid(items_list)
        self.assertTrue(items_valid)

    def test_for_quantity_available(self):
        item = 'B'
        item_available = self.hmb.quantity_available(item)
        self.assertTrue(item_available)

    def test_for_quantity_not_available(self):
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        item = 'B'
        hmb.store['B']['Quantity'] = '0'
        item_available = hmb.quantity_available(item)
        self.assertFalse(item_available)
    
    def test_for_reduced_quantity_for_purchase(self):
        items = ['B', 'B', 'B']
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        hmb.reduce_amount(items)
        expected_value = '45' 
        self.assertEqual(expected_value, hmb.store['B']['Quantity'])

    def test_for_get_total(self):
        items = ['B', 'M', 'C', 'W']
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        total_amt = hmb.get_total(items)
        expected_value = 4.60 
        self.assertEqual(expected_value, total_amt) 

    def test_for_get_correct_change(self):
        items = ['B', 'M', 'C', 'W']
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        _, change = hmb.purchase_items(items, 4.70)
        expected_value = 0.10 
        self.assertEqual(expected_value, change) 

    def test_for_get_not_enough_payment(self):
        items = ['B', 'M', 'C', 'W']
        hmb = HeavyMetalBakeSale.HeavyMetalBakeSale()
        hmb.init_store()
        _, output = hmb.purchase_items(items, 4.00)
        expected_value = 'Not enough money.' 
        self.assertEqual(expected_value, output) 

if __name__ == '__main__':
   unittest.main() 
