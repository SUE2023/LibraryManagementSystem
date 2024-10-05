#!/usr/bin/env python3
""" Book model"""


class Book(BaseModel, Base):
    """Book class inheriting from BaseModel and representing a Book"""
    
    if models.storage_t == "db":
        __tablename__ = 'Books'
        name = Column(String(128), nullable=False)
        author = Column(String(1000), nullable=False)
        is_available = Column(Boolean, default=True)  # Add a field to track availability
        issue_date = Column(DateTime, nullable=True)
        return_date = Column(DateTime, nullable=True)
        rent_rate = Column(Float, nullable=False, default=500)  # Base rent rate (per 30 days)
    else:
        name = ""
        author = ""
        is_available = True
        issue_date = None
        return_date = None
        rent_rate = 500

    def __init__(self, *args, **kwargs):
        """Initialize the Book instance"""
        super().__init__(*args, **kwargs)

    @property
    def available(self):
        """Check the availability of a book"""
        return self.is_available

    def issue(self, member_id):
        """Issue the book to a member"""
        if self.is_available:
            self.is_available = False
            self.issue_date = datetime.utcnow()  # Record the current date/time
            self.issued_to = member_id  # Store the member who borrowed the book
            models.storage.save(self)  # Save the changes to storage
            return f"Book issued to member ID {member_id} on {self.issue_date}"
        else:
            return "Book is not available."

    def return_book(self, member_id):
        """Return the book and calculate rent"""
        if not self.is_available:
            self.return_date = datetime.utcnow()
            self.is_available = True
            rent = self.calculate_rent(self.issue_date, self.return_date)
            models.storage.save(self)  # Save the changes to storage
            return f"Book returned by member ID {member_id} on {self.return_date}. Rent due: {rent} Ksh"
        else:
            return "Book was not issued."

    def calculate_rent(self, issue_date, return_date):
        """Calculate the rent based on the number of days the book was issued"""
        if issue_date and return_date:
            delta = (return_date - issue_date).days
            if delta <= 30:
                return self.rent_rate
            elif 30 < delta <= 45:
                return self.rent_rate + 200  # Additional charge after 30 days
            elif 45 < delta <= 60:
                return self.rent_rate + 700  # Further charge after 45 days
            else:
                return self.rent_rate + 1000  # Charge for more than 60 days
        return 0  # No rent if the dates are invalid

    
    @classmethod
    def issue(cls, book_id, member_id):
        """Issues a book to a member by their id"""
        book = models.storage.get(cls, book_id)
        if book and book.available:
            book.available = False
            book.issued_to = member_id
            book.issue_date = datetime.utcnow()
            models.storage.save(book)
            return book
        else:
            return None  # Book not available
    
    @classmethod
    def return_book(cls, book_id):
        """Returns a book to the library by its id"""
        book = models.storage.get(cls, book_id)
        if book and not book.available:
            book.available = True
            book.issued_to = None
            book.issue_date = None  # Clear issue date
            models.storage.save(book)
            return book
        else:
            return None  # Book wasn't issued
    
    @classmethod
    def search(cls, name=None, author=None):
        """Search for books by name and/or author"""
        if name and author:
            return models.storage.search_by_name_and_author(cls, name, author)
        elif name:
            return models.storage.search_by_name(cls, name)
        elif author:
            return models.storage.search_by_author(cls, author)
        else:
            return []
    
    @classmethod
    def charge_rent(cls, book_id):
        """Calculates and charges rent fees for the issued book"""
        book = models.storage.get(cls, book_id)
        if book and not book.available:
            days_issued = (datetime.utcnow() - book.issue_date).days
            rent_fee = days_issued * book.daily_rent_rate  # Assuming book has rent rate
            return rent_fee
        else:
            return 0  # No rent fee if book wasn't issued
