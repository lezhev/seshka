import pandas as pd
from typing import TypeVar
from dataclasses import dataclass
import os
import datetime


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
    title: str
    photo: str
    price: int
    description: str
    size: str
    tags: dict

    def __str__(self) -> str:
        tag_list = []
        for key in self.tags.keys():
            if self.tags[key] == 1:
                tag_list.append(key)
        tag_str: str = ', '.join(tag_list)
        result = (f'*Имя: {self.title}*\nРазмер: {self.size}\n'
                  f'Описание: {self.description}\n\n'
                  f'Цена: _{self.price}_\nТэги: {tag_str}')
        return result


class Seller:
    # Adding item to items.feather
    @staticmethod
    def set_item(seller_id: int, item: Item) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        current_date = datetime.date.today().isoformat()
        items_db.loc[len(items_db.index) + 1] = [item.photo, seller_id,
                                                 item.title, item.description,
                                                 item.size, item.price,
                                                 item.tags, current_date]
        items_db.to_feather(directory + '\databases\items.feather')
        # print(items_db)

    @staticmethod
    def get_item_text(index: int) -> Item:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        item_list = items_db.iloc[index]
        print(item_list)
        item: Item = Item(title=item_list.title, description=item_list.description,
                          photo=item_list.pic, size=item_list.size,
                          price=item_list.price, tags=item_list.tags)
        return item

    @staticmethod
    def get_seller_items(chat_id: int) -> list[Item]:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        indexes = items_db[items_db['seller_id'] == chat_id].index
        list_of_items: list[Item] = []
        for i in indexes - 1:
            item: Item = Item(title=items_db.iloc[i].title, description=items_db.iloc[i].description,
                              photo=items_db.iloc[i].pic, size=items_db.iloc[i].size,
                              price=items_db.iloc[i].price, tags=items_db.iloc[i].tags)
            list_of_items.append(item)
        return list_of_items

    @staticmethod
    def print_database() -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        print(items_db)


class Buyer:
    def __new__(cls, chat_id: int):
        pass

    def __init__(self, chat_id: int):
        pass

    def get_item(self, item: Item):
        pass
