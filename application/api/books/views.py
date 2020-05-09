# Create your views here.
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from api.books.serializers import (AuthorBooksSerializer, BooksSerializer, BookSerializer)
from api.models import (Book, Author)


class AuthorBooksViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorBooksSerializer


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Book/:id/
    PUT Book/:id/
    DELETE Book/:id/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        try:
            book = self.queryset.get(pk=kwargs["pk"])
            return Response(BooksSerializer(book).data)
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            book = self.queryset.get(pk=kwargs["pk"])
            serializer = BooksSerializer()
            updated_book = serializer.update(book, request.data)
            return Response(BooksSerializer(updated_book).data)
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            book = self.queryset.get(pk=kwargs["pk"])
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
