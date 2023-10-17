from django.db import models

class BookRenter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, )
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(blank=False, max_length=30)