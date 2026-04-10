class Book_jbgp:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_book_jbgp(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print()

book1_jbgp = Book_jbgp("Python Programming", "John Smith", 2022)
book2_jbgp = Book_jbgp("Data Science Basics", "Jane Doe", 2021)
book3_jbgp = Book_jbgp("Web Development", "Mike Johnson", 2023)

book1_jbgp.display_book_jbgp()
book2_jbgp.display_book_jbgp()
book3_jbgp.display_book_jbgp()

