from rest_framework import viewsets, generics

from library.book_collection.models import BookCollection
from library.book_collection.serializer import BookCollectionSerializer, ListBookCollectionSerializer


class BookCollectionViewSet(viewsets.ModelViewSet):
    """View BookCollection"""
    queryset = BookCollection.objects.all()
    serializer_class = BookCollectionSerializer


class ListBookCollection(generics.ListAPIView):
    """Cataloging in the collection"""

    def get_queryset(self):
        queryset = BookCollection.objects.filter(title_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListBookCollectionSerializer