import pandas as pd
from src.utils.utilities import read_data
from src.customize_data import CustomLibraryData
from src.utils.utilities import is_data_complete
from src.utils.utilities import validate_isbn
from src.utils.utilities import book_exist


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


def test_is_data_incomplete():
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


def test_valid_isbn():
    '''
    GIVEN ISBN of the book
    WHEN Validate_isbn methood is called
    THEN it should return True
    '''

    test_isbn = "9780393978674"
    result = validate_isbn(isbn=test_isbn)

    assert result == True


def test_invalid_isbn():
    '''
    GIVEN ISBN of the book
    WHEN Validate_isbn methood is called
    THEN it should return False
    '''

    test_isbn = "9486473"
    result = validate_isbn(isbn=test_isbn)

    assert result == False


def test_book_not_exist():
    '''
    GIVEN ISBN of the book
    WHEN book_exist method is called
    THEN it should return False
    '''

    test_isbn = "9684857263"
    result = book_exist(isbn=test_isbn)

    assert result == False


def test_read_books_count():
    '''
    GIVEN Nothing
    WHEN read_boks_count methood is called
    THEN it should return an integer value greater than or equal to zero
    '''

    result = int(read_books_count())
    assert result >= 0