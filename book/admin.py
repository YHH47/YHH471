from django.contrib import admin
# from .models import  Book,BookAdmin
# Register your models here.
# admin.site.register(Book)
from django.contrib import admin
from django.template.defaultfilters import title

from .models import Book
from django.contrib import admin
from .models import Book
from .models import Book, Review

admin.site.register(Book)
admin.site.register(Review)
