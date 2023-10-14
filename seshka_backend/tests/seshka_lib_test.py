import unittest
import pandas as pd
from seshka_backend.seshka_lib import Seller, Buyer, Item

class SellerTest(unittest.TestCase):
    def test_set_item(self) -> None:
        item: Item = Item('1', 1, 'a', 'b', 'c', 2, {'disco': 1}, '123')
        Seller.set_item(item)

class ItemTest(unittest.TestCase):
    def test_str(self) -> None:
        item: Item = Item('1', 1, 'a', 'b', 'c', 2, {'disco': 1}, '123')
        print(item)



if __name__ == '__main__':
    unittest.main()
