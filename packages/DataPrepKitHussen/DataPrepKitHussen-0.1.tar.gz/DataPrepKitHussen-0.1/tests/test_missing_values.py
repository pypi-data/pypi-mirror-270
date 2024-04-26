import pytest
import pandas as pd
from src.data_prep_kit.missing_values import remove_missing, impute_missing

def test_remove_missing():
    df = pd.DataFrame({'A': [1, None, 3]})
    result = remove_missing(df)
    assert result.isnull().sum().sum() == 0

def test_impute_missing():
    df = pd.DataFrame({'A': [1, None, 3]})
    impute_missing(df, 'A', 'mean')
    assert df.isnull().sum().sum() == 0 and df.loc[1, 'A'] == 2
