import pandas as pd
from typing import TypeVar
from dataclasses import dataclass


items_db: pd.DataFrame = pd.read_feather('databases/items.feather')
seller_sub_db: pd.DataFrame = pd.read_feather('databases/seller_subscription.feather')
favorites_db: pd.DataFrame = pd.read_feather('databases/buyers_favorite.feather')
buyer_sub_db: pd.DataFrame = pd.read_feather('databases/buyers_subscription.feather')

@dataclass
class Item:
    photo: int
    seller_id: int
    title: str
    description: str
    size: str
    price: int
    tags: list[int]
    ad_date: str

class Seller:
    def __new__(cls, id: int):
        pass

    def __init__(self, id: int):
        pass

    def set_item(self, item: Item):
        pass

class Buyer:
    def __new__(cls, id: int):
        pass

    def __init__(self, id: int):
        pass

    def get_item(self, item: Item):
        pass