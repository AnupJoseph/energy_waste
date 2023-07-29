from dataclasses import dataclass
from typing import List

import pandas as pd
import numpy as np

biomass = pd.read_csv("./dataset/Biomass_History.csv")
dist = pd.read_parquet("./dataset/distance_matrix.parquet")

basic_subset = biomass.loc[:, ["Index", "2017"]]

# print(f"{dist=}")


def next_lowest(arr):
    sorted_indices = np.argsort(arr)
    sorted_values = arr[sorted_indices]
    prev_value = None

    for index, value in zip(sorted_indices, sorted_values):
        if prev_value is None:
            prev_value = value
            continue

        if value > prev_value:
            yield (index, value)
            prev_value = value


@dataclass
class Solution:
    n_depos: int = 2
    n_refineries: int = 2
    depos: List[int] = None
    refineries: List[int] = None


def create_cost_function(sol: Solution):
    num_depos, num_refineries = sol.n_depos, sol.n_refineries
    depos, refineries = sol.depos, sol.refineries

    depo_collection = []
    cost = 0
    for depo in depos:
        depo_capacity = 20000
        distances = dist.iloc[depo, :]
        _, _ = next(next_lowest(distances))
        index, val = next(next_lowest(distances))
        collection = 0
        bioval = 0
        while depo_capacity > val and collection + bioval <= 20000:
            collection += bioval
            depo_capacity -= bioval
            curr_cost = val * bioval

            cost += curr_cost
            (
                index,
                val,
            ) = next(next_lowest(distances))
            bioval = basic_subset.iloc[index, 1]

        depo_collection.append(collection)

    print(f"{depo_collection=}")


create_cost_function(Solution(n_depos=5, n_refineries=3, depos=[4, 78, 90, 480, 1789]))
