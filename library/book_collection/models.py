from django.db import models

from library.books.models import Book
from library.collection.models import Collection


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