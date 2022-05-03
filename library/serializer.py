from rest_framework import serializers
from library.models import Book, Collection, BookCollection, BookSeller
from library.validators import phone_number_valid


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'translators', 'edition', 'pages', 'publishing_company']

#Create validators if necessary:

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class BookCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCollection
        fields = '__all__'

class ListBookCollectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    knowledge_area = serializers.SerializerMethodField()

    class Meta:
        model = BookCollection
        fields = ['title', 'knowledge_area']

    def get_knowledge_area(self, obj):
        return obj.knowledge_area.knowledge_area

    def get_title(self, obj):
        return obj.title.title

class ListBookSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeller
        fields = ['name', 'address', 'phone_number', 'email']

    def validate(self,data):
        if not phone_number_valid(data['phone_number']):
            raise serializers.ValidationError({'phone_number':"invalid phone number, eleven digits must be"})

        #if not name_valid(data['name']):
            #raise serializers.ValidationError({'name':"The name must contain only alphabetic characters"})

        return data



