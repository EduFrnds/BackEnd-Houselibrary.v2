from django.contrib import admin
from library.models import Book, Collection, BookCollection, BookSeller
# Register your models here.

class Books(admin.ModelAdmin):
    list_display = ('id', 'title', 'authors', 'translators',
                    'edition','pages','publishing_company')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_per_page = 20
    ordering = ['title']

admin.site.register(Book, Books)

class Collections(admin.ModelAdmin):
    list_display = ('id', 'knowledge_area')
    list_display_link = ('id', 'knowledge_area')
    search_fields = ['knowledge_area']

admin.site.register(Collection, Collections)

class BookCollections(admin.ModelAdmin):
    list_display = ('id', 'title', 'knowledge_area', 'condition', 'knowledge_level')
    list_display_link = ['id']

admin.site.register(BookCollection, BookCollections)

class BookSellers(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone_number', 'email')
    list_display_link = ['name']

admin.site.register(BookSeller, BookSellers)