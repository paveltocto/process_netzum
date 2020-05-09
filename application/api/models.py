from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "ntz_author"

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=150)

    class Meta:
        db_table = "ntz_book"

    def __str__(self):
        return self.title
