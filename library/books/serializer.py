from rest_framework import serializers

from library.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'translators', 'edition', 'pages', 'publishing_company', 'image']


class BookSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'translators', 'edition', 'pages', 'publishing_company', 'rent']