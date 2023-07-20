

from django.urls import path
from . import views
from .views import add_to_wishlist


urlpatterns = [
    path('books/', views.book_catalog, name='book_catalog'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/reserve/<int:book_id>/', views.book_reservation, name='book_reservation'),
    path('wishlist/add/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
]
