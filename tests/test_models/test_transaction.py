#!/usr/bin/env python3
"""
Contains the TestMemberDocs classes
"""

from datetime import datetime
import inspect
import models
from models import transaction
from models.base_model import BaseModel
import pep8
import unittest
Transaction = transaction.Transaction


class TestTransactionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Transaction class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.transaction_f = inspect.getmembers(Transaction, inspect.isfunction)

    def test_pep8_conformance_transaction(self):
        """Test that models/transaction.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/transaction.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_transaction(self):
        """Test that tests/test_models/test_transaction.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_transaction.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_transaction_module_docstring(self):
        """Test for the transaction.py module docstring"""
        self.assertIsNot(transaction.__doc__, None,
                         "transaction.py needs a docstring")
        self.assertTrue(len(transaction.__doc__) >= 1,
                        "transaction.py needs a docstring")

    def test_transaction_class_docstring(self):
        """Test for the Transaction class docstring"""
        self.assertIsNot(Transaction.__doc__, None,
                         "Transaction class needs a docstring")
        self.assertTrue(len(Transaction.__doc__) >= 1,
                        "Transaction class needs a docstring")

    def test_transaction_func_docstrings(self):
        """Test for the presence of docstrings in Transaction methods"""
        for func in self.transaction_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestTransaction(unittest.TestCase):
    """Test the Transaction class"""
    def test_is_subclass(self):
        """Test that Member is a subclass of BaseModel"""
        member = Member()
        self.assertIsInstance(transaction, BaseModel)
        self.assertTrue(hasattr(transaction, "id"))
        self.assertTrue(hasattr(transaction, "created_at"))
        self.assertTrue(hasattr(transaction, "updated_at"))

    def test_name_attr(self):
        """Test that Transaction has attribute name, and it's as an empty string"""
        transaction = Transaction()
        self.assertTrue(hasattr(transaction, "name"))
        if models.storage_t == 'db':
            self.assertEqual(transaction.name, None)
        else:
            self.assertEqual(transaction.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        am = Transaction()
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
        am = Transaction()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Book")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        transaction = Transaction()
        string = "[Member] ({}) {}".format(transaction.id, transaction.__dict__)
        self.assertEqual(string, str(transaction))
