import pandas as pd
from src.utils.utilities import read_data
from src.customize_data import CustomLibraryData
from src.utils.utilities import is_data_complete
from src.utils.utilities import validate_isbn
from src.utils.utilities import book_exist
from src.utils.utilities import read_books_count
from src.utils.utilities import write_books_count
from src.utils.utilities import is_book_available
from src.utils.utilities import add_book_to_library
from src.utils.utilities import mark_unavailable
from src.library_operations import Library


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


def test_write_books_count():
    '''
    GIVEN books count
    WHEN read_boks_count methood is called
    THEN it should return an integer value greater than or equal to zero
    '''

    test_book_count = Library().books_count
    write_books_count(test_book_count)
    result = int(read_books_count())
    assert result >= test_book_count


def test_show_available_books():
    '''
    GIVEN Nothing
    WHEN show_available_books methood is called
    THEN it should return all the books available at library.
    '''

    test_books_count = read_books_count() + 1

    result = Library().show_available_books()

    assert result == test_books_count


def test_is_book_available():
    '''
    GIVEN isbn of the book
    WHEN is_book_available methood is called
    THEN it should return True.
    '''

    test_book = CustomLibraryData(
                        isbn="9780199536405",
                        title="The Great Gatsby",
                        author="F SCOTT FITZGERALD",
                        publication_year=2008
                        )

    book_available = False
    add_book_to_library(test_book)

    result = is_book_available(test_book.isbn)

    assert result == book_available


def test_mark_unavailable():
    '''
    GIVEN isbn of the book
    WHEN mark_unavailable methood is called
    THEN it marks that particualar book unavailable.
    '''

    test_book = CustomLibraryData(
                        isbn="9380169536405",
                        title="War And Peace",
                        author="LEO TOLSTOY",
                        publication_year=1869
                        )
    
    add_book_to_library(test_book)
    
    mark_unavailable(test_book.isbn)

    result = is_book_available(test_book.isbn)

    assert result == False


def test_mark_available():
    '''
    GIVEN isbn of the book
    WHEN mark_available methood is called
    THEN it marks that particualar book available.
    '''

    test_book = CustomLibraryData(
                        isbn="9350169436405",
                        title="Great Expectations",
                        author="CHARLES DICKENS",
                        publication_year=1861
                        )
    
    add_book_to_library(test_book)
    
    mark_unavailable(test_book.isbn)

    result = is_book_available(test_book.isbn)

    assert result == False