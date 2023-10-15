import pandas as pd
from typing import TypeVar
from dataclasses import dataclass
import os
import datetime

#
# seller_sub_db: pd.DataFrame = pd.read_feather('databases/seller_names.feather')
# seller_sub_db = pd.DataFrame(columns=['seller_id'])
# favorites_db: pd.DataFrame = pd.read_feather('databases/buyers_favorites.feather')

# directory = os.path.dirname(os.path.abspath(__file__))
# items_db = pd.DataFrame(columns = ['pic', 'seller_id', 'title',
#                                    'description', 'size', 'price',
#                                    'tags', 'ad_date'])
# items_db.to_feather(directory + '\databases\items.feather')


# directory = os.path.dirname(os.path.abspath(__file__))
# shops_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
# shops_db = pd.DataFrame(columns=['buyer_id', 'seller_id'])
# shops_db.to_feather(directory + r'\databases\buyers_subscription.feather')

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
    def set_seller_name(seller_id: int, seller_name: str, seller_link: str) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        # sellers_db: pd.DataFrame = pd.read_feather(directory + r'\databases\seller_names.feather')
        sellers_db = pd.DataFrame(columns=['seller_id', 'seller_name', 'seller_link'])
        if sellers_db['seller_id'].eq(seller_id).any():
            sellers_db.loc[(sellers_db.seller_id == seller_id), 'seller_name'] = seller_name
            sellers_db.loc[(sellers_db.seller_id == seller_id), 'seller_link'] = seller_link
            sellers_db.to_feather(directory + r'\databases\seller_names.feather')
            return
        sellers_db.loc[len(sellers_db.index) + 1] = [seller_id, seller_name, seller_link]
        sellers_db.to_feather(directory + r'\databases\seller_names.feather')
        print(sellers_db)

    @staticmethod
    def get_seller_name(seller_id: int) -> str:
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + r'\databases\seller_names.feather')
        if not sellers_db['seller_id'].eq(seller_id).any():
            return ''
        y = sellers_db[sellers_db['seller_id'].isin([seller_id])]
        return y.iloc[0].seller_name

    @staticmethod
    def get_seller_link():
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + r'\databases\seller_names.feather')
        if not sellers_db['seller_id'].eq(seller_id).any():
            return ''
        y = sellers_db[sellers_db['seller_id'].isin([seller_id])]
        return y.iloc[0].seller_link

    @staticmethod
    def del_seller_name(seller_id: int):
        directory = os.path.dirname(os.path.abspath(__file__))
        sellers_db: pd.DataFrame = pd.read_feather(directory + r'\databases\seller_names.feather')
        sellers_db = sellers_db[sellers_db.seller_id != seller_id]
        sellers_db = sellers_db.reset_index(drop=True)
        print(sellers_db)
        sellers_db.to_feather(directory + r'\databases\seller_names.feather')

    # Adding item to items.feather
    @staticmethod
    def set_item(seller_id: int, item: Item) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        current_date = datetime.date.today().isoformat()
        items_db.loc[len(items_db.index) + 1] = [item.photo, seller_id,
                                                 item.title, item.description,
                                                 item.size, item.price,
                                                 item.tags, current_date]
        items_db.to_feather(directory + r'\databases\items.feather')
        # print(items_db)

    @staticmethod
    def get_item_text(index: int) -> Item:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        item_list = items_db.iloc[index]
        print(item_list)
        item: Item = Item(title=item_list.title, description=item_list.description,
                          photo=item_list.pic, size=item_list.size,  # type: ignore
                          price=item_list.price, tags=item_list.tags)
        return item

    @staticmethod
    def get_seller_items(chat_id: int) -> tuple[list[Item], list[int]]:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        indexes = items_db[items_db['seller_id'] == chat_id].index
        list_of_items: list[Item] = []
        list_of_id: list[int] = []
        for i in indexes-1:
            item: Item = Item(title=items_db.iloc[i].title, description=items_db.iloc[i].description,
                              photo=items_db.iloc[i].pic, size=items_db.iloc[i].size,
                              price=items_db.iloc[i].price, tags=items_db.iloc[i].tags)
            list_of_items.append(item)
            list_of_id.append(i)
        return list_of_items, list_of_id

    @staticmethod
    def del_seller_items(index: int):
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        if index in items_db:
            items_db.drop(index, axis=0, inplace=True)
        print(items_db)
        items_db.to_feather(directory + r'\databases\items.feather')

    @staticmethod
    def print_database() -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        sellers_db: pd.DataFrame = pd.read_feather(directory + r'\databases\seller_names.feather')
        print(f'Items:\n{items_db}\nSellers\n{sellers_db}')


class Buyer:
    @staticmethod
    def get_subs(chat_id: int) -> list[int]:
        directory = os.path.dirname(os.path.abspath(__file__))
        subs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
        indexes = subs_db[subs_db['buyer_id'] == chat_id].index
        shop_ids: list[int] = []
        for i in indexes:
            shop_ids.append(i + 1)
        print(shop_ids)
        return shop_ids

    @staticmethod
    def is_sub(chat_id: int, seller_id: int) -> bool:
        directory = os.path.dirname(os.path.abspath(__file__))
        subs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
        subs_db = subs_db[subs_db.buyer_id == chat_id]
        if subs_db.seller_id.eq(seller_id).any():
            return True
        return False

    @staticmethod
    def add_sub(chat_id: int, seller_id: int) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        subs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
        subs_db_test = subs_db[subs_db.buyer_id == chat_id]
        if subs_db_test.seller_id.eq(seller_id).any():
            return
        subs_db.loc[len(subs_db.index) + 1] = [chat_id, seller_id]
        print(subs_db)
        subs_db.to_feather(directory + r'\databases\buyers_subscription.feather')

    @staticmethod
    def remove_sub(chat_id: int, seller_id: int) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        subs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
        subs_db = subs_db.drop(subs_db[(subs_db['buyer_id'] == chat_id) & (subs_db['seller_id'] == seller_id)].index)
        print(subs_db)
        subs_db.to_feather(directory + r'\databases\buyers_subscription.feather')

    @staticmethod
    def get_fav(chat_id: int) -> list[int]:
        directory = os.path.dirname(os.path.abspath(__file__))
        fav_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_favorite.feather')
        indexes = fav_db[fav_db['buyer_id'] == chat_id].index
        shop_ids: list[int] = []
        for i in indexes:
            shop_ids.append(i + 1)
        print(shop_ids)
        return shop_ids

    @staticmethod
    def is_fav(chat_id: int, item_id: int) -> bool:
        directory = os.path.dirname(os.path.abspath(__file__))
        fav_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_favorite.feather')
        fav_db = fav_db[fav_db.buyer_id == chat_id]
        if fav_db.item_id.eq(item_id).any():
            return True
        return False

    @staticmethod
    def add_fav(chat_id: int, seller_id: int) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        fav_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_favorite.feather')
        subs_db_test = fav_db[fav_db.buyer_id == chat_id]
        if subs_db_test.seller_id.eq(seller_id).any():
            return
        fav_db.loc[len(fav_db.index) + 1] = [chat_id, seller_id]
        print(fav_db)
        fav_db.to_feather(directory + r'\databases\buyers_favorite.feather')

    @staticmethod
    def remove_fav(chat_id: int, seller_id: int) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        fav_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_favorite.feather')
        fav_db = fav_db.drop(fav_db[(fav_db['buyer_id'] == chat_id) & (fav_db['seller_id'] == seller_id)].index)
        print(fav_db)
        fav_db.to_feather(directory + r'\databases\buyers_favorite.feather')

    @staticmethod
    def get_all_items() -> tuple[list[Item], list[int]]:
        directory = os.path.dirname(os.path.abspath(__file__))
        items_db: pd.DataFrame = pd.read_feather(directory + r'\databases\items.feather')
        indexes = items_db.index
        list_of_items: list[Item] = []
        list_of_id: list[int] = []
        for i in indexes-1:
            item: Item = Item(title=items_db.iloc[i].title, description=items_db.iloc[i].description,
                              photo=items_db.iloc[i].pic, size=items_db.iloc[i].size,
                              price=items_db.iloc[i].price, tags=items_db.iloc[i].tags)
            list_of_items.append(item)
            list_of_id.append(i)
        list_of_items.reverse()
        list_of_id.reverse()
        return list_of_items, list_of_id


    @staticmethod
    def print_database() -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        subs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_subscription.feather')
        favs_db: pd.DataFrame = pd.read_feather(directory + r'\databases\buyers_favorites.feather')
        print(f'Subs:\n{subs_db}\nFavs\n{favs_db}')



