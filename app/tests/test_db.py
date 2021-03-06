from django.test import TestCase
from ..models import Author, Book
from django.db.models import ObjectDoesNotExist


class AuthorTest(TestCase):
    def setUp(self):
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

class BookTest(TestCase):
    def setUp(self):
        #Insert
        aut1 = Author(name='João')
        aut1.save()
        aut2 = Author(name='Maria')
        aut2.save()
        bk1 = Book(name='True story', edition=111, pub_year=1981)
        bk1.save()
        bk1.authors.set([aut1, aut2])
        bk1.save()
        bk2 = Book(name='Happy day', edition=27, pub_year=2002)
        bk2.save()
        bk2.authors.set([aut1])
        bk2.save()

    def test_select(self):
        #Select
        bk1= Book.objects.get(name="True story")
        self.assertEqual(bk1.name, "True story")   
        
    def test_update(self):
        #Update
        bk1 = Book.objects.get(name="True story")
        bk1.name = "True story 2"
        bk1.save()
        bk1 = Book.objects.get(name="True story 2")
        self.assertEqual(bk1.name, "True story 2")

    def test_delete(self):
        #Delete
        bk2 = Book.objects.get(name="Happy day")
        bk2.delete()
        #Test if the delete is true
        with self.assertRaisesMessage(ObjectDoesNotExist,'Book matching query does not exist.'):
            Book.objects.get(name="Happy day")

