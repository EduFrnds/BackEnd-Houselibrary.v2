from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    authors = models.CharField(max_length=50)
    translators = models.CharField(max_length=50, blank=True, null=True)
    edition = models.IntegerField(max_length=10)
    pages = models.IntegerField(max_length=1000)
    publishing_company = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Collection(models.Model):

    knowledge_area = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.knowledge_area

class BookCollection(models.Model):
    CONDICTION = (
        ('A', 'Great'),
        ('B', 'Execellent'),
        ('C', 'Good')
    )
    KNOWLEDGE_LEVEL = (
        ('A', 'Advanced'),
        ('B', 'Intermediate'),
        ('C', 'Basic')
    )
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    knowledge_area = models.ForeignKey(Collection, on_delete=models.CASCADE)
    condition = models.CharField(max_length=1, choices=CONDICTION, blank=False, null=False, default='C')
    knowledge_level = models.CharField(max_length=1, choices=KNOWLEDGE_LEVEL, blank=False, null=False, default='C')

class BookSeller(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, )
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(blank=False, max_length=30)


