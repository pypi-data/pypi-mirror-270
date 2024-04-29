#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from typing import Iterable, Tuple, Mapping


def read_data(path: str) -> Iterable[str]:
    with open(path) as f:
        lines = f.readlines()
    return lines


def handle_line(line: str) -> (str, str, float):
    user_id, item_id, score = line.strip().split(",")
    return user_id.strip(), item_id.strip(), float(score.strip())


def pre_process(data: Iterable[str], handle_func=handle_line) -> Iterable[Tuple[str, str, float]]:
    return map(handle_func, data)


def sort_similar(similar: Mapping, similar_num: int):
    for key, item_score in similar.items():
        similar[key] = sorted(item_score.items(), key=lambda x: x[1], reverse=True)[:similar_num]
    return similar


def print_cost_time(task_content, start_time):
    print(f"{task_content}: {time.perf_counter()-start_time:.2f} seconds.")