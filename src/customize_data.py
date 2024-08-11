from pandas import DataFrame

class CustomLibraryData:
    def __init__(self, isbn: str, title: str, author: str, publication_year: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_dataframe(self) -> DataFrame:
        try:
            custom_data_dict = {
                "ISBN": [self.isbn],
                "Title": [self.title],
                "Author": [self.author],
                "Publication_year": [self.publication_year],
                "Available": ["Yes"]
            }

            return DataFrame(custom_data_dict)
        except Exception as e:
            pass
    
    def get_data_list(self) -> list:
        return [self.isbn, self.title, self.author, self.publication_year, "Yes"]