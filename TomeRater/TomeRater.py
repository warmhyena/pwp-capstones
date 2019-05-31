#creating User class that defines User attributes (name/email) and methods (read & rate books)
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(f"{self.name}'s email address has been updated to {self.address}.")

    def __repr__(self):
        return f"User {self.name}, email: {self.email}, books read: {self.books}"

    def __eq__(self, other_user):
        """Override the default Equals behavior"""
        if isinstance(other_user, User):
            return self.name == other_user.name and self.email == other_user.email
        return False
    def __ne__(self, other_user):
        """Override the default Unequal behavior"""
        return self.name != other_user.name and self.email != other_user.email

    def read_book(self, book, rating = None):
        self.books.update({book: rating}) #ability for user to "read" a book and add a rating for it to its books dictionary
    
    def get_average_rating(self):
        ratings_total = 0
        for rating in self.books.values():
            ratings_total += float(rating)
        return ratings_total / len(self.books.values())


#creating Book class which to represent books that Users can read & rate
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn): # Ability to update a book's ISBN
        self.isbn = isbn
        print(f"The book '{self.title}' now has an updated ISBN: {self.isbn}.")

    def add_rating (self, rating): # Ability to add rating for a book to a list of ratings (if rating is "valid" between 0 - 4)
        if self.rating >= 0 and self.rating <= 4:
            self.ratings.append(self.rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        """Override the default Equals behavior"""
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        return False
    def __ne__(self, other_book):
        """Override the default Unequal behavior"""
        return self.title != other_book.title and self.isbn != other_book.isbn

    def get_average_rating(self):
        ratings_total = 0
        for rating in self.ratings:
            ratings_total += rating
        return ratings_total / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))    

#creating Fiction subclass of Book class
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"

#creating Non_Fiction subclass of Book class
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return f"{self.title}, a{self.level} manual on {self.subject}"

#creating Tome Rater class
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        return Book(self.title, self.isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(self.title, self.author, self.isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(self.title, self.subject, self.level, self.isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users:
            print(f"No user with email {email}!")
        else:
            self.users.get(email).read_book(book, rating)
            book.add_rating(rating)
        if self.book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users.update({email: new_user})
        if user_books != None:
            for user_book in user_books:
                self.add_book_to_user(user_book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)
    
    def most_read_book(self):
        return max(self.books, key=lambda key: self.books[key])

    def highest_rated_book(self):
        highest_rated = None
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rated = book                
                highest_rating = rating
        return highest_rated

    def most_positive_user(self):
        positive_user = None
        highest_rating = 0
        for user in self.users.values():
            avg_user_rating = user.get_average_rating()
            if avg_user_rating > highest_rating:
                positive_user = user
                highest_rating = avg_user_rating
        return positive_user




    
