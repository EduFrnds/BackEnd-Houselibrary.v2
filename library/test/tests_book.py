from rest_framework.test import APITestCase
from library.books.models import Book
from django.urls import reverse
from rest_framework import status

class BookTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Books-list')
        self.book_1 = Book.objects.create(
            title='TST1', authors='ATST1', translators='TTST1'
        )

    # Cenário de teste GET
    def test_get_book(self):
        """Test to verify the GET type request"""

        response = self.book_1.get(self.list_url)  # request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
