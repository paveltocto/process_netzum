from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.books.views import AuthorBooksViewSet, BooksDetailView

urlpatterns = [
    path('<int:pk>/', BooksDetailView.as_view()),
    path('authors', AuthorBooksViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
