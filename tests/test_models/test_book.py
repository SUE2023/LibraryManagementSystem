#!/usr/bin/env python3
"""
Contains the TestBookDocs classes
"""

from datetime import datetime
import inspect
import models
from models import book
from models.base_model import BaseModel
import pep8
import unittest
Book = book.Book


class TestBookDocs(unittest.TestCase):
    """Tests to check the documentation and style of Book class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.book_f = inspect.getmembers(Book, inspect.isfunction)

    def test_pep8_conformance_book(self):
        """Test that models/book.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/book.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_book(self):
        """Test that tests/test_models/test_book.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_book.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_book_module_docstring(self):
        """Test for the book.py module docstring"""
        self.assertIsNot(book.__doc__, None,
                         "book.py needs a docstring")
        self.assertTrue(len(book.__doc__) >= 1,
                        "book.py needs a docstring")

    def test_book_class_docstring(self):
        """Test for the Book class docstring"""
        self.assertIsNot(Book.__doc__, None,
                         "Book class needs a docstring")
        self.assertTrue(len(Book.__doc__) >= 1,
                        "Book class needs a docstring")

    def test_book_func_docstrings(self):
        """Test for the presence of docstrings in Book methods"""
        for func in self.book_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBook(unittest.TestCase):
    """Test the Book class"""
    def test_is_subclass(self):
        """Test that Book is a subclass of BaseModel"""
        book = Book()
        self.assertIsInstance(book, BaseModel)
        self.assertTrue(hasattr(book, "id"))
        self.assertTrue(hasattr(book, "created_at"))
        self.assertTrue(hasattr(book, "updated_at"))

    def test_name_attr(self):
        """Test that Book has attribute name, and it's as an empty string"""
        book = Book()
        self.assertTrue(hasattr(book, "name"))
        if models.storage_t == 'db':
            self.assertEqual(book.name, None)
        else:
            self.assertEqual(book.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        am = Book()
        # print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Book()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Book")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        book = Book()
        string = "[Book] ({}) {}".format(book.id, book.__dict__)
        self.assertEqual(string, str(book))
