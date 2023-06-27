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

    def test_for_bake_sale_items(self):
        self.hmb.init_store()
        expected_result = len(self.hmb.store)
        self.assertTrue(expected_result) 



if __name__ == '__main__':
   unittest.main() 
