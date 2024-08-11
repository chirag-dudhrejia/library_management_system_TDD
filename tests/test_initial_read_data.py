import pandas as pd
from src.utils.utilities import read_data
from src.customize_data import CustomLibraryData
from src.utils.utilities import is_data_complete


def test_initial_data_read():
    '''
    GIVEN Nothing
    WHEN read_data method is called before any data is stored
    THEN it should return None
    '''

    test_expected = None
    result = read_data()

    assert result == test_expected


def test_is_data_complete():
    '''
    GIVEN information of the book
    WHEN add_book method is called
    THEN it should return True
    '''

    test_book = CustomLibraryData(
                        isbn="9780605064225",
                        title="Harry Potter and the Order of the Phoenix",
                        author="J.K. Rowling",
                        publication_year=2003
                        )
    
    result = is_data_complete(test_book)

    assert result == True


def test_is_data_incomplete():              #commit 2 testing is_data_complete function
    '''
    GIVEN information of the book
    WHEN add_book method is called
    THEN it should return False
    '''

    test_book = CustomLibraryData(
                        isbn="9780393978674",
                        title="The Origin of Species",
                        author="Charles Darwin",
                        publication_year=7
                        )
    
    result = is_data_complete(test_book)

    assert result == False