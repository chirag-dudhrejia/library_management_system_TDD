from src.customize_data import CustomLibraryData
from src.utils.utilities import is_data_complete
from src.utils.utilities import validate_isbn
from src.utils.utilities import book_exist
from src.utils.utilities import add_book_to_library
from src.utils.utilities import read_books_count
from src.utils.utilities import write_books_count
from src.utils.utilities import read_data


DATA_FILE_PATH = "data/books.csv"

class Library:
        
    books_count = read_books_count()

    def add_book(self, isbn: str, title: str, author: str, publication_year: int) -> None:
        '''
        Adds book to the library after performing required checks.

        Parameters
        ----------
        isbn: str
                International Standars Book Number(ISBN).
        title: str
                Title of the book.
        author: str
                Name of the writer.
        publication_year: int
                Year of book publish.

        Returns
        -------
                None
        '''

        custom_data_obj = CustomLibraryData(
                                    isbn=isbn,
                                    title=title,
                                    author=author,
                                    publication_year=publication_year
                                    )
        
        information_is_complete = is_data_complete(custom_data_obj)

        if information_is_complete:
            isbn_is_valid = validate_isbn(isbn=isbn)
        else:
            print(f"Incomplete information. Please recheck and enter again.")
            return

        if isbn_is_valid:
            book_already_exist = book_exist(isbn=isbn)
        else:
            print("Invalid ISBN. Please recheck and enter again.")
            return

        if book_already_exist:
            print(f"Book with ISBN {isbn} already exist.")
            return
        else:
            add_book_to_library(book_data_obj=custom_data_obj)

        if book_exist(custom_data_obj.isbn):
            Library.books_count += 1
            write_books_count(Library.books_count)
            print("\nBook Successfully added.\n")
        else:
            print("\nFailed to add book, please crosscheck book details and try again.\n")


    def show_available_books(self) -> int:
        '''
        Shows all the available books at the library.

        Returns
        -------
                int
                    returns the number of books available.
        '''
        books_df = read_data()

        available_books_df = books_df[books_df["Available"] == "Yes"][["ISBN", "Title"]]

        print(available_books_df.to_string())

        return len(available_books_df)