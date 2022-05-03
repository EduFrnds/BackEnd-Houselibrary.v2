from rest_framework import viewsets, generics, filters
from library.models import Book, Collection, BookCollection, BookSeller
from library.serializer import BookSerializer, CollectionSerializer, BookCollectionSerializer, ListBookCollectionSerializer, ListBookSellerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    """"View all registered books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']

class CollectionViewSet(viewsets.ModelViewSet):
    """View all collection"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class BookCollectionViewSet(viewsets.ModelViewSet):
    """View BookCollection"""
    queryset = BookCollection.objects.all()
    serializer_class = BookCollectionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListBookCollection(generics.ListAPIView):
    """Cataloging in the collection"""

    def get_queryset(self):
        queryset = BookCollection.objects.filter(title_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListBookCollectionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class BookSellerViewSet(viewsets.ModelViewSet):
    """View BookSellers"""
    queryset = BookSeller.objects.all()
    serializer_class = ListBookSellerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'phone_number']