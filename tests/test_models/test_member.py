#!/usr/bin/env python3
"""
Contains the TestMemberDocs classes
"""

from datetime import datetime
import inspect
import models
from models import member
from models.base_model import BaseModel
import pep8
import unittest
Member = member.Member


class TestMemberDocs(unittest.TestCase):
    """Tests to check the documentation and style of Member class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.member_f = inspect.getmembers(Member, inspect.isfunction)

    def test_pep8_conformance_member(self):
        """Test that models/member.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/member.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_member(self):
        """Test that tests/test_models/test_member.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_member.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_member_module_docstring(self):
        """Test for the member.py module docstring"""
        self.assertIsNot(member.__doc__, None,
                         "member.py needs a docstring")
        self.assertTrue(len(member.__doc__) >= 1,
                        "member.py needs a docstring")

    def test_member_class_docstring(self):
        """Test for the Member class docstring"""
        self.assertIsNot(Member.__doc__, None,
                         "Member class needs a docstring")
        self.assertTrue(len(Member.__doc__) >= 1,
                        "Member class needs a docstring")

    def test_member_func_docstrings(self):
        """Test for the presence of docstrings in Member methods"""
        for func in self.member_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestMember(unittest.TestCase):
    """Test the Member class"""
    def test_is_subclass(self):
        """Test that Member is a subclass of BaseModel"""
        member = Member()
        self.assertIsInstance(member, BaseModel)
        self.assertTrue(hasattr(member, "id"))
        self.assertTrue(hasattr(member, "created_at"))
        self.assertTrue(hasattr(member, "updated_at"))

    def test_name_attr(self):
        """Test that Member has attribute name, and it's as an empty string"""
        member = Member()
        self.assertTrue(hasattr(member, "name"))
        if models.storage_t == 'db':
            self.assertEqual(member.name, None)
        else:
            self.assertEqual(member.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        am = Member()
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
        member = Member()
        string = "[Member] ({}) {}".format(member.id, member.__dict__)
        self.assertEqual(string, str(member))
