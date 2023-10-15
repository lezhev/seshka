import unittest
import pandas as pd
from seshka_backend.seshka_lib import Seller, Buyer, Item


class SellerTest(unittest.TestCase):
    def test_set_seller_name(self) -> None:
        Seller.set_seller_name(4, 'Grigorya', 'tg.com/Huy')

    def test_set_item(self) -> None:
        item: Item = Item('1', 'a', 5, 'c', 'a', {'disco': 1, 'zombie': 1, 'game': 0})
        Seller.set_item(1, item)

    def test_get_seller_name(self) -> None:
        Seller.get_seller_name(2)

    def test_get_item_text(self) -> None:
        print(Seller.get_item_text(0))

    def test_get_seller_items(self) -> None:
        print(Seller.get_seller_items(1))

    def test_del_seller_name(self) -> None:
        Seller.del_seller_name(4)

    def test_del_item(self) -> None:
        Seller.del_seller_items(16)


class BuyTest(unittest.TestCase):
    def test_get_subs(self) -> None:
        Buyer.get_subs(1)

    def test_get_sub(self) -> None:
        print(Buyer.get_sub(1, 2))

    def test_add_sub(self) -> None:
        Buyer.add_sub(1, 4)

    def test_db(self) -> None:
        Buyer.print_database()

    def test_remove_sub(self):
        Buyer.remove_sub(1, 2)

    def test_get_favourite(self) -> None:
        Buyer.get_favourite(1)


class ItemTest(unittest.TestCase):
    def test_str(self) -> None:
        item: Item = Item('1', 'a', 5, 'c', 'a', {'disco': 1, 'zombie': 1, 'game': 0})
        print(item)

    def test_print_db(self) -> None:
        Seller.print_database()





if __name__ == '__main__':
    unittest.main()
