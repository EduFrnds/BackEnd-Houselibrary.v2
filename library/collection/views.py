from rest_framework import viewsets

from library.collection.models import Collection
from library.collection.serializer import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    """View all collection"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer