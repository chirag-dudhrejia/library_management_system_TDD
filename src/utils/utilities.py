import pandas as pd
import re
from src.customize_data import CustomLibraryData

DATA_FILE_PATH = "data/books.csv"


def read_data() -> pd.DataFrame:
    '''
    Reads data from csv file.

    Returns
    -------
    Dataframe
            Data in Dataframe format.
    '''

    try:
        books_df = pd.read_csv(DATA_FILE_PATH)
    except pd.errors.EmptyDataError:
        pass
    except Exception:
        pass
    else:
        return books_df
    
    return


def is_data_complete(book: CustomLibraryData) -> bool:
    '''
    Checks if record of book has all the information.

    Parameters
    ---------
    book: CustomLibraryData
                Information of book stored as object.

    Returns
    -------
    bool
        True if information is not missing.
    '''

    isbn_length = len(book.isbn)
    title_length = len(book.title)
    author_length = len(book.author)
    publication_year_length = len(str(book.publication_year))

    if isbn_length==0 or title_length==0 or author_length==0 or publication_year_length!=4:
        return False
    else:
        return True
    

def validate_isbn(isbn: str) -> bool:
    '''
    Validates that the ISBN is of right size and in all digits format.

    Perameter
    ---------
    isbn: str
            International Standerd Book Number(ISBN) of a book.

    Returns
    -------
    bool
        True if isbn is in correct format.
    '''

    old_pattern = r"^\d{10}$"
    new_pattern = r"^\d{13}$"

    old_pattern_match = re.match(old_pattern, isbn)
    new_pattern_match = re.match(new_pattern, isbn)

    if old_pattern_match or new_pattern_match:
        return True
    
    return False


def book_exist(isbn) -> bool:
    '''
    Checks for duplication of book if already exist.

    Parameters
    ----------
    isbn: str
            International Standard Book Number(ISBN) of book

    Returns
    -------
    bool
        True if book ISBN is present in data.
    '''

    book_df = read_data()

    if book_df is not None:
        book_df["ISBN"] = book_df["ISBN"].astype(str)
        if book_df["ISBN"].str.contains(isbn).sum() > 0:
            return True

    return False