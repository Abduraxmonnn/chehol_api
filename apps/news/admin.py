from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'get_image', 'created_date')
    list_display_links = ('theme', )
    search_fields = ('id', 'theme', 'created_date')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
        return 'Image'

    get_image.short_description = 'Picture'


admin.site.register(News, NewsAdmin)
