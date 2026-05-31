"""
------------------------------------------------------------
LeetCode 183, Customers Who Never Order, difficulty easy, language python
Saved at 2026-05-31 12:00:51
------------------------------------------------------------
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders["customerId"])].drop(columns=["id"]).rename(columns={"name":"Customers"})
