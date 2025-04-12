from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'autorius', 'isleidimo_data')
    list_filter = ('pavadinimas','isleidimo_data')
    search_fields = ('pavadinimas',) # paliekamas kablelis del Python tuplu atvaizdavimo

