class Library():
   def __init__(self, list):
       self.books_list = list
       self.available_book_list = list[:]
       self.books_lent ={}

   def display_available_books(self):
       for book in self.available_book_list:
           print(book)

   def display_all_books(self):
       for book in self.books_list:
           print(book)

   def lend_books(self, name, book):
       if book not in self.books_list:
           print("Incorrect Book Name. Please Check the Book List")
           return
       if book in self.available_book_list:
           self.books_lent.update({book:name})
           self.available_book_list.remove(book)
           print("You can take the book..")
       else:
           print("The book is already taken by " + self.books_lent[book])


   def return_books(self, book):
       del self.books_lent[book]
       self.available_book_list.append(book)

if __name__ =="__main__":
       lib = Library(["The Alchemist", "The Life Devine", "Da Vinci Code", "The Wings of Fire", "The Comerade"])
       print("Welcome to our Library. Enter an option. ")
       while True:
         print("1. Display available books")
         print("2. Display all books")
         print("3. Borrow a books")
         print("4. Return a books")
         print("5. Quit")
         user_choice = int(input())
         if user_choice == 1:
             lib.display_available_books()
         elif user_choice == 2:
             lib.display_all_books()
         elif user_choice == 3:
             name = input("Enter your Name: ")
             book = input("Enter book name you want: ")
             lib.lend_books(name, book)
         elif user_choice == 4:
             book = input("Enter the book name you return: ")
             lib.return_books(book)
         elif user_choice == 5:
             break
         else:
             print("Invalid choice..")
