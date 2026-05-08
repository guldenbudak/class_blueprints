book_list = []

class Book:
    def __init__(self, title, author, page_count, is_borrowed=False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.is_borrowed = is_borrowed

    def summary_book(self):
        borrow_status = "Available"
        if self.is_borrowed == True:
            borrow_status = "Borrowed"

        return f"{self.title} by {self.author}, {self.page_count} pages, {borrow_status}"

    def borrow_book(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"You have borrowed {self.title}.")
        else:
            print(f"Sorry, {self.title} is already borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(f"You have returned {self.title}.")
        else:
            print(f"{self.title} was not borrowed.")


book_list.append(Book(title="Fareler ve Insanlar", author="Van Gogh", page_count=1200))
book_list.append(Book(title="Sefiller", author="Viktor Hugo", page_count=1235))
book_list.append(Book(title="Cin Ali", author="Selamet", page_count=10))
book_list.append(Book(title="Harry Potter", author="Selena Gomez", page_count=123))

while True:
    print("Chose your option:")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")

    option = int(input("Enter the number of your option: "))
    if option == 1:
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        page_count = int(input("Enter the number of pages: "))
        new_book = Book(title=title, author=author, page_count=page_count)
        book_list.append(new_book)
    elif option == 2:
        title = input("Enter the book title: ")
        selected_book = book_list[0]
        for book in book_list:
            if book.title == title:
                selected_book = book
                break

        selected_book.borrow_book()

    elif option == 3:
        title = input("Enter the book title: ")
        selected_book = book_list[0]
        for book in book_list:
            if book.title == title:
                selected_book = book
                break

        selected_book.return_book()