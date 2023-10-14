import unittest
import pandas as pd
from seshka_backend.seshka_lib import Seller, Buyer, Item

class MyTestCase(unittest.TestCase):
    def test_set_item(self) -> None:
        item: Item = Item(1, 1, 'a', 'b', 'c', 2, [0, 0], '123')
        Seller.set_item(item)



if __name__ == '__main__':
    unittest.main()
