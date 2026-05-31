"""
------------------------------------------------------------
LeetCode 181, Employees Earning More Than Their Managers, difficulty easy, language python
Saved at 2026-05-31 11:59:08
------------------------------------------------------------
"""

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager = employee.merge(
        employee,
        left_on="managerId",
        right_on="id",
        how="left"
    )
    return manager[manager["salary_x"] > manager["salary_y"]][["name_x"]].rename(columns={"name_x":"Employee"})
