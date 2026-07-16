class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def register_member(self,member):
        self.members.append(member)
