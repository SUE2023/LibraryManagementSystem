#!/usr/bin/env python3
""" Transaction model"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime, Integer, Float
from models.BaseModel import BaseModel
from sqlalchemy.ext.declarative import declarative_base


class Transaction(BaseModel):
    """Transaction class inheriting from BaseModel and representing a Transaction"""

    if models.storage_t == "db":
        __tablename__ = 'Transactions'
        id = Column(Integer, primary_key=True, autoincrement=True)
        books_rent = Column(String(128), nullable=False)
        books_return = Column(String(128), nullable=False)
        registrations = Column(String(128), nullable=False)
        surplus = Column(Float, nullable=False)
        stock = Column(Integer, nullable=False)
        
    else:
        id = ""
        books_rent = ""
        books_return = ""
        registrations = ""
        surplus = 0.0
        stock = 0

    def __init__(self, *args, **kwargs):
        """Initialize the Transaction instance"""
        super().__init__(*args, **kwargs)

    def record_book_rent(self, book_id, member_id):
        """Records a book as rented with book_id and member_id"""
        self.books_rent = f"Book ID: {book_id}, Member ID: {member_id}"
        models.storage.save(self)
        return f"Book {book_id} rented by member {member_id}"

    def record_book_return(self, book_id, member_id):
        """Records a book return with book_id and member_id"""
        self.books_return = f"Book ID: {book_id}, Member ID: {member_id}"
        models.storage.save(self)
        return f"Book {book_id} returned by member {member_id}"

    @classmethod
    def get_all_rented_books(cls):
        """Retrieve all rented books"""
        return models.storage.filter(cls, "books_rent")

    @classmethod
    def get_all_returned_books(cls):
        """Retrieve all returned books"""
        return models.storage.filter(cls, "books_return")

    def record_registration(self, member_id, amount):
        """Records a member registration and the amount paid"""
        self.registrations = f"Member ID: {member_id}, Amount Paid: {amount}"
        models.storage.save(self)
        return f"Member {member_id} registered with an amount of {amount}"

    def record_surplus(self, member_id, amount):
        """Records surplus credit for a member"""
        self.surplus = amount
        models.storage.save(self)
        return f"Surplus of {amount} recorded for member {member_id}"

    def update_stock(self, book_rent, book_return):
        """Updates the stock of books"""
        self.stock = (self.stock + book_return) - book_rent
        models.storage.save(self)
        return f"Current stock is {self.stock}"
