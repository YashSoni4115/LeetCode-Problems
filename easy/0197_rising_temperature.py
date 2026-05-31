"""
------------------------------------------------------------
LeetCode 197, Rising Temperature, difficulty easy, language python
Saved at 2026-05-31 12:01:50
------------------------------------------------------------
"""

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["day_plus_1"] = weather["recordDate"] - pd.Timedelta(days=1)
    result = pd.merge(
        weather, 
        weather, 
        left_on=["recordDate"], 
        right_on=["day_plus_1"], 
        suffixes=("_yesterday", "_today")
    )

    result = result[result["temperature_today"] > result["temperature_yesterday"]]
    result = result[["id_today"]].rename(columns={"id_today":"id"})
    
    return result
