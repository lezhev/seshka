import pandas as pd
from typing import TypeVar
from dataclasses import dataclass
import os



# seller_sub_db: pd.DataFrame = pd.read_feather('databases/seller_subscription.feather')
# favorites_db: pd.DataFrame = pd.read_feather('databases/buyers_favorite.feather')
# buyer_sub_db: pd.DataFrame = pd.read_feather('databases/buyers_subscription.feather')

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
    @staticmethod
    def set_item(item: Item) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        items_db.loc[len(items_db.index) + 1] = [item.photo, item.seller_id,
                           item.title, item.description,
                           item.size, item.price,
                           item.tags, item.ad_date]
        items_db.to_feather(directory + '\databases\items.feather')
        print(items_db)

class Buyer:
    def __new__(cls, chat_id: int):
        pass

    def __init__(self, chat_id: int):
        pass

    def get_item(self, item: Item):
        pass
