from django.contrib import admin
from django.urls import path, include
from library.collection.views import CollectionViewSet
from library.book_collection.views import BookCollectionViewSet, ListBookCollection
from library.book_renter.views import BookRenterViewSet
from library.books.views import BookViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

#principal rota default.


router = routers.DefaultRouter()

#registrando book e collection na rota
router.register('book', BookViewSet, basename='Books')
router.register('collection', CollectionViewSet, basename='Collections')
router.register('bookcollection', BookCollectionViewSet, basename='BookCollection')
router.register('bookrenter', BookRenterViewSet, basename='BookSeller')


urlpatterns = [
    path('room-controler/', admin.site.urls),
    path('', include(router.urls)),
    path('title/<int:pk>/knowledge_area/', ListBookCollection.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
