import pandas as pd
from src.utils.utilities import read_data


def test_initial_data_read():
    '''
    GIVEN Nothing
    WHEN read_data method is called before any data is stored
    THEN it should return None
    '''

    test_expected = None
    result = read_data()

    assert result == test_expected