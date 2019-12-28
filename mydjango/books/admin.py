from django.contrib import admin
from .models import Product, Publisher, Book, Author
admin.site.register(Product)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)

# Register your models here.
