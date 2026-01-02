from django.contrib import admin
from myapp.models import myusers, Books
# Register your models here.
admin.site.register(myusers)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ['books', 'author', 'title']
