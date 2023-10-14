import unittest
import pandas as pd
from seshka_backend.seshka_lib import Seller, Buyer, Item

class SellerTest(unittest.TestCase):
    def test_set_item(self) -> None:
        item: Item = Item('1', 'a', 'b', 'c', 2, {'disco': 1, 'zombie': 1, 'game': 0})
        Seller.set_item(1, item)

    def test_get_item_text(self) -> None:
        print(Seller.get_item_text(3))

class ItemTest(unittest.TestCase):
    def test_str(self) -> None:
        item: Item = Item('1', 'a', 'b', 'c', 2, {'disco': 1, 'zombie': 1, 'game': 0})
        #print(item)



if __name__ == '__main__':
    unittest.main()
