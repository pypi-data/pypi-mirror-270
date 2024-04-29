#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""coll filter"""

import os
import math
from enum import Enum
from typing import Iterable, Tuple, List, Mapping, Collection, Generic, TypeVar

U = TypeVar('U')
T = TypeVar('T')


class CFType(Enum):
    UCF = 'ucf'
    ICF = 'icf'


def default_similar_func(items: List, other: List) -> float:
    """两个item并集数

    以用户相似度为例，遍历item_users，每行用户间拥有共同的item，避免遍历userTtems大量用户间没有共同的item：
    item1: user1, user2, user3

    user1和user2共同有item1:
    user1: item1, item2, item3
    user2: item1, item4, item5

    传入此方法的参数为:
    items: [item1, item2, item3]
    other: [item1, item4, item5]
    """
    return 1.0 / float(len(set(items + other)))


def sqrt_similar_func(items: List, other: List) -> float:
    """两个item数相乘开根"""
    return 1.0 / math.sqrt(len(items) * len(other))


class CollFilter(Generic[U, T]):

    def __init__(self, data: Iterable[Tuple[U, T, float]], parallel_num=2 * os.cpu_count(), similar_fn=default_similar_func):
        if parallel_num > 1:
            from cf.pooling import PoolCollFilter
            self.coll_filter = PoolCollFilter(data, parallel_num, similar_fn)
        else:
            from cf.base import BaseCollFilter
            self.coll_filter = BaseCollFilter(data, similar_fn)

    def user_cf(self,
                recall_num=64,
                similar_num=256,
                user_ids: Collection[U] = None,
                user_similar: Mapping[U, Mapping[U, float]] = None,
                similar_fn=None
                ) -> Mapping[U, List[Tuple[T, float]]]:
        """
        基于用户的协同过滤
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个用户最大相似用户个数
        @param user_ids  要推荐的用户列表
        @param user_similar  用户相似矩阵
        @param similar_fn  相似度计算函数
        @return {user_id: [(item_id, score),],}
        """
        assert recall_num > 0, "'recall_num' should be a positive number."
        return self.coll_filter.user_cf(recall_num, similar_num, user_ids, user_similar, similar_fn)

    def item_cf(self,
                recall_num=64,
                similar_num=256,
                user_ids: Collection[U] = None,
                item_similar: Mapping[T, Mapping[T, float]] = None,
                similar_fn=None
                ) -> Mapping[U, List[Tuple[T, float]]]:
        """
        基于物品的协同过滤
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个物品最大相似物品个数
        @param user_ids  要推荐的用户列表
        @param item_similar  物品相似矩阵
        @param similar_fn  相似度计算函数
        @return {user_id: [(item_id, score),],}
        """
        assert recall_num > 0, "'recall_num' should be a positive number."
        return self.coll_filter.item_cf(recall_num, similar_num, user_ids, item_similar, similar_fn)

    def recommend(self, user_id: U, recall_num=64, similar_num=8, similar_fn=None) -> List[Tuple[T, float]]:
        """
        给一个用户推荐
        @param user_id  要推荐的用户
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个物品最大相似物品个数
        @param similar_fn  相似度计算函数
        @return [(item_id, score),]
        """
        icf = self.item_cf(recall_num, similar_num, [user_id], None, similar_fn)
        items = icf[user_id]
        if recall_num == 1:
            if items:
                return items
            else:
                return self.user_cf(recall_num, similar_num, [user_id], None, similar_fn)[user_id]
        else:
            half = round(recall_num / 2)
            ucf_items = self.user_cf(recall_num, similar_num, [user_id], None, similar_fn)[user_id]
            if len(items) > half and len(ucf_items) > (recall_num - half):
                tmp = items[:half]
                tmp.extend(ucf_items[:(recall_num - half)])
                return tmp
            elif len(items) < half:
                items.extend(ucf_items[:(recall_num - half)])
                return items
            elif len(ucf_items) < (1-half):
                tmp = items[:(recall_num - len(ucf_items))]
                tmp.extend(ucf_items)
                return tmp

            return items

    def recommends(self,
                   user_ids: Collection[U],
                   recall_num=64,
                   similar_num=8,
                   similar_fn=None
                   ) -> Mapping[U, List[Tuple[T, float]]]:
        """
        给一批用户推荐
        @param user_ids  要推荐的用户列表
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个物品最大相似物品个数
        @param similar_fn  相似度计算函数
        @return {user_id: [(item_id, score),],}
        """
        icf = self.item_cf(recall_num, similar_num, user_ids, None, similar_fn)
        if recall_num == 1:
            user_similar = self.get_user_similar(similar_num, similar_fn)
            for user_id, items in icf.items():
                if not items:
                    items = self.user_cf(recall_num, similar_num, [user_id], user_similar, similar_fn)[user_id]
        else:
            half = round(recall_num / 2)
            ucf = self.user_cf(recall_num, similar_num, user_ids, None, similar_fn)
            for user_id, items in icf.items():
                ucf_items = ucf[user_id]
                if len(items) >= half and len(ucf_items) >= (recall_num - half):
                    tmp = items[:half]
                    tmp.extend(ucf_items[:(recall_num - half)])
                    items = tmp
                elif len(items) < half:
                    items.extend(ucf_items[:(recall_num - half)])
                elif len(ucf_items) < (1-half):
                    tmp = items[:(recall_num - len(ucf_items))]
                    tmp.extend(ucf_items)
                    items = tmp

        return icf

    def get_user_similar(self, similar_num=256, similar_fn=None) -> Mapping[U, Mapping[U, float]]:
        """
        用户相似矩阵
        """
        return self.coll_filter.cal_similar(CFType.UCF, similar_num, similar_fn)

    def get_item_similar(self, similar_num=256, similar_fn=None) -> Mapping[T, Mapping[T, float]]:
        """
        物品相似矩阵
        """
        return self.coll_filter.cal_similar(CFType.ICF, similar_num, similar_fn)

    def release(self):
        self.coll_filter.release()
