from django.contrib import admin
from django.urls import path, include
from library.views import BookViewSet, CollectionViewSet,BookCollectionViewSet, ListBookCollection, BookSellerViewSet
from rest_framework import routers

#principal rota default.
router = routers.DefaultRouter()

#registrando book e collection na rota
router.register('book', BookViewSet, basename='Books')
router.register('collection', CollectionViewSet, basename='Collections')
router.register('bookcollection', BookCollectionViewSet, basename='BookCollection')
router.register('bookseller', BookSellerViewSet, basename='BookSeller')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('title/<int:pk>/knowledge_area/', ListBookCollection.as_view())
]
