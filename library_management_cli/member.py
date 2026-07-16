class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return  f"Name : {self.name} | {self.name}'s ID : {self.member_id} | Borrowed books : {self.borrowed_books}"
    
