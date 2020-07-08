import unittest

class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self):
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service")
 
class Customer():
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
def setup():
    size(220,100)
    global library, Madzia
    books = ["Naocznosc", "Sens Sztuki", "Hobbit"]
    library = Library(books)
    Madzia = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            
class Testowanie(unittest.TestCase):
    def test_klient_wypozycza_i_oddaje_ksiazke(self):
        klient = Customer()
        self.assertFalse(klient.haveBook)
        self.assertEqual(klient.book, "")
        klient.requestBook("Hobbit")
        self.assertTrue(klient.haveBook)
        self.assertEqual(klient.book, "Hobbit")
        klient.returnBook()
        self.assertFalse(klient.haveBook)
        # to należałoby rozdzielić na oddzielne testy, unittesty z założenia testują najmniejszą możłiwą cząstkę kodu
        
    def test_zwrocenie_ksiazki_do_biblioteki(self):
        biblioteka = Library(["Pan Tadeusz", "Wesele"])
        self.assertEqual(biblioteka.availableBooks, ["Pan Tadeusz", "Wesele"])
        biblioteka.addBook("Romeo i Julia")
        self.assertEqual(biblioteka.availableBooks, ["Pan Tadeusz", "Wesele", "Romeo i Julia"])
        
if __name__ == '__main__':
    unittest.main()
    
#2pkt
