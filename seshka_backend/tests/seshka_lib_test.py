import unittest
import pandas as pd
from seshka_backend.seshka_lib import Seller, Buyer, Item


class SellerTest(unittest.TestCase):
    def test_set_seller_name(self) -> None:
        Seller.set_seller_name(2, 'Gosha')

    def test_set_item(self) -> None:
        item: Item = Item('1', 'a', 5, 'c', 'a', {'disco': 1, 'zombie': 1, 'game': 0})
        Seller.set_item(1, item)

    def test_get_item_text(self) -> None:
        print(Seller.get_item_text(0))

    def test_get_seller_items(self) -> None:
        print(Seller.get_seller_items(1))

class ItemTest(unittest.TestCase):
    def test_str(self) -> None:
        item: Item = Item('1', 'a', 5, 'c', 'a', {'disco': 1, 'zombie': 1, 'game': 0})
        print(item)

    def test_print_db(self) -> None:
        Seller.print_database()



if __name__ == '__main__':
    unittest.main()
