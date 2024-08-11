from src.customize_data import CustomLibraryData
from src.utils.utilities import is_data_complete
from src.utils.utilities import validate_isbn
from src.utils.utilities import book_exist
from src.utils.utilities import add_book_to_library
from src.utils.utilities import read_books_count
from src.utils.utilities import write_books_count
from src.utils.utilities import read_data
from src.utils.utilities import is_book_available
from src.utils.utilities import mark_unavailable


DATA_FILE_PATH = "data/books.csv"

class Library:
        
    books_count = read_books_count()

    def add_book(isbn: str, title: str, author: str, publication_year: int) -> None:
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


    def show_available_books() -> int:
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
    
    def borrow_book(isbn: str):
        '''
        Borrows a book from the library.

        Parameters
        ----------
                isbn: str
                        International Standard Book Number(ISBN).
        
        Returns
        -------
            None
        '''

        valid_isbn = validate_isbn(isbn=isbn)

        if validate_isbn:
            book_available = is_book_available(isbn=isbn)

        marked_unavailable = None
        if book_available:
            marked_unavailable = mark_unavailable(isbn=isbn)
            print(marked_unavailable)

        if marked_unavailable:
            print("Book Borrowed Successfully.")


    def return_book(isbn: str):
        '''
        returns a book to the library.

        Parameters
        ----------
                isbn: str
                        International Standard Book Number(ISBN).
        
        Returns
        -------
            None
        '''

        valid_isbn = validate_isbn(isbn=isbn)

        if validate_isbn:
            book_not_available = is_book_available(isbn=isbn)

        if book_not_available:
            marked_unavailable = mark_unavailable(isbn=isbn)

        if marked_unavailable:
            print("Book returned Successfully.")