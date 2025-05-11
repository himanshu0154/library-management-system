import sys

class Library:
    def __init__(self):
        self.list_of_books = {}
        self.borrowed_books = {}



    def add_books(self, no_of_books_add):
        for i in range(len(self.list_of_books) + 1, len(self.list_of_books) + no_of_books_add + 1):
                name_of_books = input(f"{i}.  ").lower()
                if any(book[0] == name_of_books for book in self.list_of_books.values()):
                    print("this book already exist")
                    break
                    
                else:
                    self.list_of_books[i] = [name_of_books, "available"]

                   


    def show_books(self):
        if len(self.list_of_books) == 0:
            print("there aren't any books available at the moment...")
        else:
            print("these are the books available - ")
            for i, book in self.list_of_books.items():
                if book[1] == "borrowed":
                    print(f"{i} - {book[0]}(borrowed)")
                elif book[1] != "borrowed":
                    print(f"{i} -  {book[0]}")

        
    def no_of_books_available(self):
        available_count = 0
        borrowed_count = 0
        for i, book in self.list_of_books.items():
            if book[1] == "available":
                available_count += 1
            else:
                borrowed_count += 1

        print(f"there are {available_count} books available at the moment... and {borrowed_count} are being borrowed")


    def borrow_books(self):
        if len(self.list_of_books) == 0:
            print("there aren't any books available at the moment...")
        else:
            print("these are the books available - ")
            for i, book in self.list_of_books.items():
                if book[1] != "borrowed":
                    print(f"{i} -  {book[0]}")
            no_of_borrow = int(input("enter the number of books you wanna borrow?\n"))
            available_books = [k for k, v in self.list_of_books.items() if v[1] == "available"]
            if no_of_borrow <= len(available_books):
                print("please enter the no. specific to the book you wanna borrow")
                for i in range(1, no_of_borrow + 1):
                    index = int(input("--> "))
                    if index not in self.list_of_books:
                        print("Invalid book number")
                        continue
                    elif self.list_of_books[index][1] == "borrowed":
                        print(f"{self.list_of_books[index][0]} book is already borrowed")
                    else:
                        print(f"you have successfully borrowed {self.list_of_books[index][0]}")
                        self.list_of_books[index][1] = "borrowed"
                        self.borrowed_books[index] = [self.list_of_books[index][0], "borrowed"]

            else:
                print("there arn't that many books availabe")

    def return_books(self):
        if len(self.borrowed_books) == 0:
            print("you havent borrowed any book yet")
        else:
            print("these are the books you have borrowed - ")
            for index, book in self.borrowed_books.items():
                if book[1] == "returned":
                    continue
                else:
                    print(f"{index} - {book[0]}")
            no_of_return = int(input("How many books would you like to return: "))
            borrowed_book = [k for k, v in self.list_of_books.items() if v[1] == "borrowed"]
            if no_of_return <= len(borrowed_book):
                print("enter the number specific to the book you want to return....")
                for i in range(1, no_of_return+1):
                    index = int(input("--> "))
                    if self.borrowed_books[index][1] == "returned":
                        print(f"you have already returned that book")
                    else:
                        print(f"you have successfully returned {self.borrowed_books[index][0]}")
                        self.list_of_books[index][1] = "available"
                        self.borrowed_books[index][1] = "returned"
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
            print("please give a integer value...")
        except IndexError:
            print("please select available index...")
        except KeyError:
            print("please select available index")

libraryExecution()