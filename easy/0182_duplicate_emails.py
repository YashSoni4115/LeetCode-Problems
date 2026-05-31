"""
------------------------------------------------------------
LeetCode 182, Duplicate Emails, difficulty easy, language python
Saved at 2026-05-31 11:59:50
------------------------------------------------------------
"""

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    count = person.groupby("email").size().reset_index(name="count")
    return count[count["count"]>1].rename(columns={"email":"Email"}).drop(columns=["count"])
