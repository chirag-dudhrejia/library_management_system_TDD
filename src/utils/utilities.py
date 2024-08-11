import pandas as pd
import re
from src.customize_data import CustomLibraryData

DATA_FILE_PATH = "data/books.csv"
BOOKS_COUNT_FILE_PATH = "data/books_count.txt"


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


def add_book_to_library(book_data_obj: CustomLibraryData) -> None:
    '''
    Adds new book information into the books data file.

    Parameters
    ----------
    book_data_obj
                Information of book stored as object.
    
    Returns
    -------
        None
    '''

    book_df = read_data()

    if book_df is not None:
        book_df.loc[len(book_df)] = book_data_obj.get_data_list()
        book_df.to_csv(DATA_FILE_PATH, index=False)
    else:
        new_book_df = book_data_obj.get_dataframe()
        new_book_df.to_csv(DATA_FILE_PATH, index=False)


def read_books_count() -> int:
    '''
    Reads count of books from txt file.

    Returns
    -------
        int
            count of books read from the txt file.
    '''
    try:
        with open(BOOKS_COUNT_FILE_PATH, "r") as book_count_file:
            book_count = book_count_file.read()
            return int(book_count)
    except FileNotFoundError as file_not_found_error:
        with open(BOOKS_COUNT_FILE_PATH, "w") as book_count_file:
            book_count_file.write("0")
            return 0
        

def write_books_count(book_count: int) -> None:
    '''
    Writes books count into txt file.

    Parameters
    ----------
    book_count
            number of books in library.
    
    Returns
    -------
        None
    '''
    with open(BOOKS_COUNT_FILE_PATH, "w") as book_count_file:
        book_count_file.write(str(book_count))


def is_book_available(isbn: str) -> bool:
    '''
    Searches for a book if available at library.

    Parameters
    ----------
    isbn: str
            International Standard Book Number(ISBN).
    
    Returns
    -------
        bool
            returns True if book is available at libraty.
    '''

    books_df = read_data()

    all_available_books = books_df[books_df["Available"] == "Yes"]
    searched_book_avaibility = len(all_available_books[books_df["ISBN"] == int(isbn)])

    if searched_book_avaibility == 0:
        return True

    return False


def mark_unavailable(isbn: str):
    '''
    Markes book unavailable when book is borrowed.

    Parameters
    ----------
    isbn: str
            International Standard Book Number(ISBN).
    
    Returns
    -------
        None
    '''

    book_df = read_data()

    book_df[book_df["ISBN"] == int(isbn)]["Available"] = "No"
    book_df.to_csv(DATA_FILE_PATH, index=False)


def mark_available(isbn: str):
    '''
    Markes book available when book is borrowed.

    Parameters
    ----------
    isbn: str
            International Standard Book Number(ISBN).
    
    Returns
    -------
        None
    '''

    book_df = read_data()

    book_df[book_df["ISBN"] == int(isbn)]["Available"] = "Yes"
    book_df.to_csv(DATA_FILE_PATH, index=False)