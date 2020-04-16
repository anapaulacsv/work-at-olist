from django.db import models 

class Author(models.Model):
    name = models.CharField(max_length=60)

class Book(models.Model):
    name = models.CharField(max_length=100)
    edition = models.IntegerField()
    pub_year = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')


