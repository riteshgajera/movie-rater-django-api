from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Movie, Rating

# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ["movei_image"]

    def movei_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
        ))


admin.site.register(Rating)
