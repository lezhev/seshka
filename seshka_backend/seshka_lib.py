import pandas as pd
from typing import TypeVar
from dataclasses import dataclass
import os



# seller_sub_db: pd.DataFrame = pd.read_feather('databases/seller_subscription.feather')
# favorites_db: pd.DataFrame = pd.read_feather('databases/buyers_favorite.feather')
# buyer_sub_db: pd.DataFrame = pd.read_feather('databases/buyers_subscription.feather')
# directory = os.path.dirname(os.path.abspath(__file__))
# items_db = pd.DataFrame(columns = ['pic', 'seller_id', 'title',
#                                    'description', 'size', 'price',
#                                    'tags', 'ad_date'])
# items_db.to_feather(directory + '\databases\items.feather')

@dataclass
class Item:
    photo: str
    seller_id: int
    title: str
    description: str
    size: str
    price: int
    tags: dict
    ad_date: str

    def __str__(self):
        tag_list = []
        for key in self.tags.keys():
            if self.tags[key] == 1:
                tag_list.append(key)
        result = (f'# {self.title}\nРазмер: {self.size}\n'
                  f'{self.description}\n\n'
                  f'_{self.price}_\n{tag_list}')
        return result

class Seller:
    #Adding item to items.feather
    @staticmethod
    def set_item(item: Item) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        print(items_db)
        items_db.loc[len(items_db.index) + 1] = [item.photo, item.seller_id,
                           item.title, item.description,
                           item.size, item.price,
                           item.tags, item.ad_date]
        items_db.to_feather(directory + '\databases\items.feather')
        print(items_db)

    @staticmethod
    def get_item_from_index(item_index: int) -> str:
        pass


class Buyer:
    def __new__(cls, chat_id: int):
        pass

    def __init__(self, chat_id: int):
        pass

    def get_item(self, item: Item):
        pass
