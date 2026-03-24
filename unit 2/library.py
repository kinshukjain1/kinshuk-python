class Library:
    def __init__(self,book_name , author , Available= True):
        self.book_name = book_name
        self.author = author 
        self.Available = Available 
        
    def check_out(self):
        if self.Available:
            self.Available = False
            print(f'"{self.book_name}" has been checked out.')
        else :
            print(f'f"{self.book_name}" is currently not available.')
            
    def return_book(self):
        self.Available = True 
        print(f'"(self.book_name)" has been returned and is now available.')
        
    def display_book(self):
        status = "available" if self.Available else "Not available"
        print(f"Book Name:{self.book_name}, Author:{self.author}, Status: {status}")
book1 = Library("Python Programming","Guido van Rossum")
book2 = Library("Data Structures", "Mark Allen Weiss")
        
book1.display_book()
book1.check_out()
book1.display_book()
    
book1.return_book()
book1.display_book()
