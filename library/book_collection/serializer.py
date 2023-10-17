from rest_framework import serializers

from library.book_collection.models import BookCollection


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


class BookCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCollection
        fields = '__all__'
