import pandas as pd
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