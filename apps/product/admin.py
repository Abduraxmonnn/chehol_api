# Username: admin
# Password: admin12

from django.contrib import admin
from django.utils.safestring import mark_safe


from product.models import CoverCategory, CarsCategory, Cover


@admin.register(CoverCategory)
class CoverCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'material')
    list_display_links = ('id', )
    search_fields = ('id', 'material')


@admin.register(CarsCategory)
class CarsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'car_model')
    list_display_links = ('id', 'car_name')
    search_fields = ('id', 'car_name')


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'get_image')
    list_display_links = ('id', )
    search_fields = ('id', 'car_name', 'color')
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
        return 'Image'

    get_image.short_description = 'Picture'
