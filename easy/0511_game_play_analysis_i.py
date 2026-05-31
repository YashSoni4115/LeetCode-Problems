"""
------------------------------------------------------------
LeetCode 511, Game Play Analysis I, difficulty easy, language python
Saved at 2026-05-31 12:03:05
------------------------------------------------------------
"""

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values("event_date", ascending=True, inplace=True)
    activity.drop_duplicates(subset=["player_id"], keep="first", inplace=True)
    activity.rename(columns={"event_date":"first_login"},inplace=True)
    activity.sort_values("player_id", ascending=True, inplace=True)
    return activity[["player_id", "first_login"]]
