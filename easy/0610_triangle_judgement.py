"""
------------------------------------------------------------
LeetCode 610, Triangle Judgement, difficulty easy, language python
Saved at 2026-05-31 12:04:32
------------------------------------------------------------
"""

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(
        lambda row: "Yes" if row["x"]+row["y"]+row["z"]>2*max(row["x"],row["y"],row["z"]) else "No", 
        axis = 1
    )
    return triangle
