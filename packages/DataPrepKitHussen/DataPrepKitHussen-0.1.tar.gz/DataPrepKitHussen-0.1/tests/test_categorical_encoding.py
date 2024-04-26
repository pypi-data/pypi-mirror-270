import pytest
import pandas as pd
from src.data_prep_kit.categorical_encoding import encode_categories

def test_encode_categories_one_hot():
    df = pd.DataFrame({'fruit': ['apple', 'banana', 'apple']})
    encoded_df = encode_categories(df, 'fruit', 'one_hot')
    assert 'fruit_apple' in encoded_df.columns

def test_encode_categories_label():
    df = pd.DataFrame({'fruit': ['apple', 'banana', 'apple']})
    encoded_df = encode_categories(df, 'fruit', 'label')
    assert 'fruit' in encoded_df.columns and encoded_df['fruit'].dtype == 'int'
