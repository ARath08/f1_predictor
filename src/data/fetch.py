import fastf1
from pathlib import Path
import pandas as pd

def get_race_data(year: int, event: str, session: str) -> pd.DataFrame:
    """Fetch and cache race data."""
    session = fastf1.get_session(year, event, session)
    session.load()
    return session.laps.pick_quicklaps()