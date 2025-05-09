import sys

class Library:
    def __init__(self):
        self.list_of_books = []
        self.books_record = []
        self.borrowed_books = []


    def add_books(self, no_of_books_add):
        for i in range(1, no_of_books_add + 1):
                name_of_books = input(f"{i}.  ")
                if name_of_books.lower() in self.books_record:
                    print("this book already exist")
                    if name_of_books.lower() in self.borrowed_books: 
                        print("it is currently being borrowed")
                        continue
                else:
                    self.list_of_books.append(name_of_books.lower())
                    self.books_record.append(name_of_books.lower())


    def show_books(self):
        if len(self.list_of_books) == 0:
            print("there aren't any books available at the moment...")
        else:
            print("these are the books available - ")
            for i, book in enumerate(self.list_of_books):
                print(f"{i+1}. {book.title()}")

        
    def no_of_books_available(self):
        print(f"there are {len(self.list_of_books)} available at the moment... and {len(self.borrowed_books)} are being borrowed")


    def borrow_books(self):
        if len(self.list_of_books) == 0:
            print("there arent any books available for you to borrow")
        else:
            print("these are the books available....")
            for i, book in enumerate(self.list_of_books):
                print(f"{i+1}. {book.title()}")
            no_of_borrow = int(input("enter the number of books you wanna borrow?\n"))
            if no_of_borrow <= len(self.list_of_books):
                print("please enter the no. specific to the book you wanna borrow")
                indexes = []
                for i in range(1, no_of_borrow + 1):
                    index = int(input("--> ")) - 1
                    indexes.append(index)

                for index in sorted(indexes, reverse=True):
                    book = self.list_of_books[index]
                    print(f"you have successfully borrowed {book}")
                    self.borrowed_books.append(book)
                    self.list_of_books.remove(book)
            else:
                print("there arn't that many books availabe")

    def return_books(self):
        if self.borrowed_books == []:
            print("you havent borrowed any book yet")
        else:
            print("these are the books you have borrowed - ")
            for i, book in enumerate(self.borrowed_books):
                print(f"{i+1}. {book.title()}")
            no_of_return = int(input("How many books would you like to return: "))
            if no_of_return <= len(self.borrowed_books):
                print("enter the number specific to the book you want to return....")
                indexes = []
                for i in range(1, no_of_return+1):
                    returned_book = int(input("--> ")) - 1
                    indexes.append(returned_book)
                for index in sorted(indexes, reverse= True):
                    book = self.borrowed_books[index]
                    print(f"you have succesfuly returned {book}")
                    self.list_of_books.append(book)
                    self.borrowed_books.remove(book)
            else:
                print("you havnt borrowed that many books")

books = Library()
def libraryExecution():
    manual = "what would you wanna do sir - \n1. add books\n2. show books\n3. borrow a book\n4. return a book\n5. no of books\n6. show manual\n7. leave"
    print(manual)
    while True:
        try:
            user = int(input("enter the number here: "))
            if user == 1:
                no_of_books_add = int(input("how many books do you wanna add? : "))
                print("Enter the name of the books - ")
                books.add_books(no_of_books_add)
            elif user == 2:
                books.show_books()
            elif user == 3:
                books.borrow_books()
            elif user == 4:
                books.return_books()
            elif user == 5:
                books.no_of_books_available()
            elif user == 6:
                print(manual)
            elif user == 7:
                print("thanks for you time...")
                print("good bye!!")
                sys.exit()
            else:
                print("please choose from above options...")
        except ValueError:
            print("please give valid response...")
        except IndexError:
            print("please give valid response...")

libraryExecution()