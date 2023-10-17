from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from library.book_renter.models import BookRenter
from library.book_renter.serializer import ListBookRenterSerializer


class BookRenterViewSet(viewsets.ModelViewSet):
    """View BookSellers"""
    queryset = BookRenter.objects.all()
    serializer_class = ListBookRenterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'phone_number']