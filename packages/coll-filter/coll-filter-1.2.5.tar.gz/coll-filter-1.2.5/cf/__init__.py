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

    def __init__(self, data: Iterable[Tuple[U, T, float]], parallel_num=2 * os.cpu_count(),
                 similar_fn=default_similar_func, cache_similar=False):
        if parallel_num > 1:
            from cf.pooling import PoolCollFilter
            self._coll_filter = PoolCollFilter(data, parallel_num, similar_fn, cache_similar)
        else:
            from cf.base import BaseCollFilter
            self._coll_filter = BaseCollFilter(data, similar_fn, cache_similar)

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
        return self._coll_filter.user_cf(recall_num, similar_num, user_ids, user_similar, similar_fn)

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
        return self._coll_filter.item_cf(recall_num, similar_num, user_ids, item_similar, similar_fn)

    def recommend(self, user_id: U, recall_num=64, similar_num=8, similar_fn=None, ratio=0.5) -> List[Tuple[T, float]]:
        """
        给一个用户推荐
        @param user_id  要推荐的用户
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个物品最大相似物品个数
        @param similar_fn  相似度计算函数
        @param ratio  推荐结果中item_cf所占比例
        @return [(item_id, score),]
        """
        icf = self.item_cf(recall_num, similar_num, [user_id], None, similar_fn)
        icf_items = icf[user_id]
        if recall_num == 1:
            if icf_items:
                return icf_items
            else:
                return self.user_cf(recall_num, similar_num, [user_id], None, similar_fn)[user_id]
        else:
            ucf_items = self.user_cf(recall_num, similar_num, [user_id], None, similar_fn)[user_id]
            return self._fusion(icf_items, ucf_items, recall_num, ratio)

    def recommends(self,
                   user_ids: Collection[U],
                   recall_num=64,
                   similar_num=8,
                   similar_fn=None,
                   ratio=0.5
                   ) -> Mapping[U, List[Tuple[T, float]]]:
        """
        给一批用户推荐
        @param user_ids  要推荐的用户列表
        @param recall_num  每个用户最大召回个数
        @param similar_num  每个物品最大相似物品个数
        @param similar_fn  相似度计算函数
        @param ratio  推荐结果中item_cf所占比例
        @return {user_id: [(item_id, score),],}
        """
        icf = self.item_cf(recall_num, similar_num, user_ids, None, similar_fn)
        if recall_num == 1:
            user_similar = self.get_user_similar(similar_num, similar_fn)
            for user_id, items in icf.items():
                if not items:
                    icf[user_id] = self.user_cf(recall_num, similar_num, [user_id], user_similar, similar_fn)[user_id]
        else:
            ucf = self.user_cf(recall_num, similar_num, user_ids, None, similar_fn)
            for user_id, icf_items in icf.items():
                ucf_items = ucf[user_id]
                icf[user_id] = self._fusion(icf_items, ucf_items, recall_num, ratio)

        return icf

    def get_user_similar(self, similar_num=256, similar_fn=None) -> Mapping[U, Mapping[U, float]]:
        """
        用户相似矩阵
        """
        return self._coll_filter.cal_similar(CFType.UCF, similar_num, similar_fn)

    def get_item_similar(self, similar_num=256, similar_fn=None) -> Mapping[T, Mapping[T, float]]:
        """
        物品相似矩阵
        """
        return self._coll_filter.cal_similar(CFType.ICF, similar_num, similar_fn)

    def release(self):
        self._coll_filter.release()

    @staticmethod
    def _fusion(icf_items, ucf_items, recall_num, ratio):
        ucf_items_dict = dict(ucf_items)
        # item_cf和user_cf共同出现的先放进result_items里
        result_items = [(item[0], item[1] + ucf_items_dict[item[0]]) for item in icf_items if item[0] in ucf_items_dict]
        result_items_len = len(result_items)
        if result_items_len >= recall_num:
            return result_items[:recall_num]

        leave_num = recall_num - result_items_len
        half = round(leave_num * ratio + 0.01)  # 加0.01避免*.5是四舍五入向下取整
        result_item_ids = [item[0] for item in result_items]
        leave_icf_items = [item for item in icf_items if item[0] not in result_item_ids]
        leave_ucf_items = [item for item in ucf_items if item[0] not in result_item_ids]
        if len(leave_icf_items) > half and len(leave_ucf_items) > (leave_num - half):
            result_items.extend(icf_items[:half])
            result_items.extend(leave_ucf_items[:(leave_num - half)])
            return result_items
        elif len(leave_icf_items) < half:
            result_items.extend(leave_icf_items)
            result_items.extend(leave_ucf_items[:(leave_num - half)])
            return result_items
        elif len(leave_ucf_items) < (leave_num - half):
            result_items.extend(leave_icf_items[:(leave_num - len(leave_ucf_items))])
            result_items.extend(leave_ucf_items)
            return result_items

        result_items.extend(leave_icf_items[:leave_num])
        leave_num = recall_num - len(result_items)
        if leave_num > 0:
            result_items.extend(leave_ucf_items[:leave_num])
        return result_items
