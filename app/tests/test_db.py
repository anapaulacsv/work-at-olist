from django.test import TestCase
from ..models import Author, Book


class AuthorTest(TestCase):
    def setUp (self):
        #Insert
        a = Author (name='João')
        a.save()
    
    def test_select(self):
        #Select 
        aut = Author.objects.get(name="João")
        self.assertEqual(aut.name, "João")
