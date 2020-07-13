from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Movie, Rating

admin.site.register(Movie)
admin.site.register(Rating)
