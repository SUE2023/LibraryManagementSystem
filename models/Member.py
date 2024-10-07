#!/usr/bin/env python3
""" Member model"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime, Integer, Float
from models.BaseModel import BaseModel
from sqlalchemy.ext.declarative import declarative_base


class Member(BaseModel):
    """Member class inheriting from BaseModel and representing a Member"""
    
    if models.storage_t == "db":
        __tablename__ = 'Members'
        id = Column(Integer, primary_key=True, autoincrement=True)
        first_name = Column(String(128), nullable=False)
        second_name = Column(String(128), nullable=False)
        registration_date = Column(DateTime, default=datetime.utcnow)
        outstanding = Column(Float, default=500) 
        rented_books = Column(String, nullable=True)  # Ideally a relationship
    else:
        id = ""
        first_name = ""
        second_name = ""
        registration_date = "" 
        outstanding = 500
        rented_books = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Member instance"""
        super().__init__(*args, **kwargs)
        self.rented_books = kwargs.get('rented_books', [])

    def register(self, first_name, second_name):
        """Registers a member to the library"""
        self.first_name = first_name
        self.second_name = second_name
        self.registration_date = datetime.utcnow()
        models.storage.save(self)
        return f"Registered member {self.id} on {self.registration_date}"
    
    def check_outstanding(self):
        """Check and return the outstanding balance"""
        if self.outstanding > 500:
            return f"Outstanding debt is {self.outstanding}, which exceeds the limit."
        else:
            return f"Outstanding debt is {self.outstanding}, which is within the allowed limit."

    def rent_book(self, book):
        """Adds a book to the rented_books list"""
        self.rented_books.append(book)
        models.storage.save(self)
        return f"Book {book.name} rented by member {self.id}"

    def list_rented_books(self):
        """Returns the list of books rented by the member"""
        return self.rented_books
