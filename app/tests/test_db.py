from django.test import TestCase
from ..models import Author, Book
from django.db.models import ObjectDoesNotExist


class AuthorTest(TestCase):
    def setUp (self):
        #Insert
        a = Author(name='João')
        a.save()
        b = Author(name='Maria')
        b.save()
    
    def test_select(self):
        #Select 
        aut = Author.objects.get(name="João")
        self.assertEqual(aut.name, "João")

    def test_update(self):
        #Update
        aut = Author.objects.get(name="João")
        aut.name = "Pedro"
        aut.save()
        aut = Author.objects.get(name="Pedro")
        self.assertEqual(aut.name, "Pedro")

    def test_delete(self):
        #Delete
        aut = Author.objects.get(name="Maria")
        aut.delete()
        #Test if the delete is true
        with self.assertRaisesMessage(ObjectDoesNotExist,'Author matching query does not exist.'):
            Author.objects.get(name="Maria")
