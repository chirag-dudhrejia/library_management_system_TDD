from src.library_operations import Library
from src.customize_data import CustomLibraryData


class LibraryManagementSystem:

    def __init__(self):
        self.isbn: str = None
        self.title: str = None
        self.author: str = None
        self.publication_year: int = None
        self.operate()

    def operate(self):

        print("Welcome To Brilliance Library.")

        library_is_operating = True

        while library_is_operating:
            try:
                choice = int(input("Choose task to perform.\n1) Add book\n2) Borrow book\n3) return Book\n4) View available books.\n0) Exit."))
            except Exception as e:
                print("Invalid Input please enter again.")
                self.operate()

            if choice == 0:
                break
            elif choice == 1:
                try:
                    self.isbn = input("Enter ISBN of book : ")
                    self.title = input("Enter Title of book : ")
                    self.author = input("Enter Aurhot name : ")
                    self.publication_year = int(input("Enter Publication year of book : "))
                except:
                    print("Invalid Input please enter again.")
                    self.operate()

                Library.add_book(
                        isbn=self.isbn, 
                        title=self.title, 
                        author=self.author, 
                        publication_year=self.publication_year
                        )
            elif choice == 2:
                try:
                    self.isbn = input("Enter ISBN of book : ")
                except:
                    print("Invalid Input please enter again.")
                    self.operate()
            elif choice == 3:
                try:
                    self.isbn = input("Enter ISBN of book : ")
                except:
                    print("Invalid Input please enter again.")
                    self.operate()
                    
                Library.return_book(isbn=self.isbn)
            elif choice == 4:
                Library.show_available_books()


if __name__ == "__main__":
    LibraryManagementSystem()
    print("Thank You for the visit.")