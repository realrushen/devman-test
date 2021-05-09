from copy import deepcopy

import pandas as pd
from collections import defaultdict
from pprint import pprint
from pandas import DataFrame


def load_wines(sheet_path: str, sheet_name: str) -> dict:
    """load wines data from example.xlsx file"""
    wines_from_exel: DataFrame = pd.read_excel(sheet_path, sheet_name=sheet_name)
    wines = wines_from_exel.fillna(value='').to_dict(orient='record')

    wines_dict = defaultdict(list)
    for wine in wines:
        category_name = wine.pop('category')
        wines_dict[category_name].append(wine)
    return wines_dict


if __name__ == '__main__':
    wines = load_wines('wine3.xlsx', 'Лист1')
    pprint(wines)