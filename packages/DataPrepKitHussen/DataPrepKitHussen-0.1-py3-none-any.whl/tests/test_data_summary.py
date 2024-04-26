import pytest
import pandas as pd
from src.data_prep_kit.data_summary import summary_statistics, frequency

def test_summary_statistics():
    df = pd.DataFrame({'numbers': range(10)})
    summary = summary_statistics(df)
    assert 'numbers' in summary.columns

def test_frequency():
    df = pd.DataFrame({'category': ['apple']*3 + ['banana']*2})
    freq = frequency(df, 'category')
    assert freq['apple'] == 3 and freq['banana'] == 2
