import pandas as pd
from typing import TypeVar
from dataclasses import dataclass
import os
import datetime


# seller_sub_db: pd.DataFrame = pd.read_feather('databases/seller_names.feather')
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
                  f'Описание: {self.description}\n'
                  f'Цена: _{self.price} руб._\nТэги: {tag_str}')
        return result


class Seller:
    @staticmethod
    def set_seller_name(seller_id: int, seller_name: str) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + '\databases\seller_names.feather')
        #sellers_db = pd.DataFrame(columns=['seller_id', 'seller_name'])
        if sellers_db['seller_id'].eq(seller_id).any():
            sellers_db.loc[(sellers_db.seller_id == seller_id), 'seller_name'] = seller_name
            sellers_db.to_feather(directory + '\databases\seller_names.feather')
            return
        sellers_db.loc[len(sellers_db.index) + 1] = [seller_id, seller_name]
        sellers_db.to_feather(directory + '\databases\seller_names.feather')
        print(sellers_db)

    @staticmethod
    def get_seller_name(seller_id: int) -> str:
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + '\databases\seller_names.feather')
        if not sellers_db['seller_id'].eq(seller_id).any():
            return ''
        y = sellers_db[sellers_db['seller_id'].isin([seller_id])]
        return y.iloc[0].seller_name

    @staticmethod
    def del_seller_name(seller_id: int):
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + '\databases\seller_names.feather')
        sellers_db = sellers_db[sellers_db.seller_id != seller_id]
        sellers_db = sellers_db.reset_index(drop=True)
        print(sellers_db)
        sellers_db.to_feather(directory + '\databases\seller_names.feather')

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
                          photo=item_list.pic, size=item_list.size,  # type: ignore
                          price=item_list.price, tags=item_list.tags)
        return item

    @staticmethod
    def get_seller_items(chat_id: int) -> tuple[list[Item], list[int]]:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        indexes = items_db[items_db['seller_id'] == chat_id].index
        list_of_items: list[Item] = []
        list_of_id: list[int] = []
        for i in indexes:
            item: Item = Item(title=items_db.iloc[i].title, description=items_db.iloc[i].description,
                              photo=items_db.iloc[i].pic, size=items_db.iloc[i].size,
                              price=items_db.iloc[i].price, tags=items_db.iloc[i].tags)
            list_of_items.append(item)
            list_of_id.append(i)
        return list_of_items, list_of_id

    @staticmethod
    def del_seller_items(index: int):
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        if index in items_db:
            items_db.drop(index, axis=0, inplace=True)
        items_db = items_db.reset_index(drop=True)
        print(items_db)
        items_db.to_feather(directory + '\databases\items.feather')

    @staticmethod
    def print_database() -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + '\databases\items.feather')
        sellers_db: pd.DataFrame = pd.read_feather(directory + '\databases\seller_names.feather')
        print(f'Items:\n{items_db}\nSellers\n{sellers_db}')


class Buyer:
    def __new__(cls, chat_id: int):
        pass

    def __init__(self, chat_id: int):
        pass

    def get_item(self, item: Item):
        pass
