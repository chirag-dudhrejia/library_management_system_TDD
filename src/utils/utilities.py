import pandas as pd

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