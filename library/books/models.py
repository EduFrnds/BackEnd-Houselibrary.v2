from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=50, unique=True)
    authors = models.CharField(max_length=50)
    translators = models.CharField(max_length=50, blank=True, null=True)
    edition = models.CharField(max_length=10)
    pages = models.CharField(max_length=100)
    publishing_company = models.CharField(max_length=50, blank=True, null=True)
    rent = models.BooleanField(null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title