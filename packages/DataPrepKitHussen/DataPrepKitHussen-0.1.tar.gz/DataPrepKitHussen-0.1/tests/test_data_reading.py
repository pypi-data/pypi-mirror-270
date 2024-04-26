import pytest
from src.data_prep_kit.data_reading import read_csv, read_excel, read_json

def test_read_csv():
    assert not read_csv('test.csv').empty

def test_read_excel():
    assert not read_excel('test.xlsx').empty

def test_read_json():
    assert not read_json('test.json').empty
