from django.test import TestCase
from .models import Articles


class YourTestClass(TestCase):
    def test_false_is_false(self):
        response = Articles.title
        self.assertEqual(response, "test data")

"""
Знаю що не правильно, але я тупо не знаю як відтестувати якісь данні 
"""
