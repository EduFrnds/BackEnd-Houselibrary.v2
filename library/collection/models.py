from django.db import models

class Collection(models.Model):

    knowledge_area = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.knowledge_area