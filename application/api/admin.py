from django.contrib import admin

# Register your models here.
from api.models import Author, Book


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Book, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
