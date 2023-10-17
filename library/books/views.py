from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from library.books.models import Book
from library.books.serializer import BookSerializerV2, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """"View all registered books"""
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    http_method_names = ['get', 'post', 'put', 'path']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    search_fields = ['title']
    filterset_fields = ['title']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return BookSerializerV2
        else:
            return BookSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['location'] = request.build_absolute_uri() + id
            return response

    # Estou indicando os dados que estou colocando em cache
    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(BookViewSet, self).dispatch(*args, **kwargs)