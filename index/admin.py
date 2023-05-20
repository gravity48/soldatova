from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MainHeader, Reviews


# Register your models here.


@admin.register(MainHeader)
class MainHeaderAdmin(admin.ModelAdmin):
    fields = (("vk",), ("telegram",), ("whatsapp",), ("instagram",), ("phone",),)
    list_display = ("id", "vk", "telegram", "whatsapp", "instagram", "phone")
    list_display_links = ("vk", "telegram", "whatsapp", "instagram", "phone")


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image',)
    fields = (('review_img',), ('get_image',))

    list_display = ('id', 'name', 'date_join', 'get_image')
    list_display_links = ('id', 'name', 'date_join')

    def get_image(self, obj: Reviews):
        return mark_safe(f'<img src={obj.review_img.url} width=auto height=600px')

    get_image.short_description = 'Изображение'


admin.site.site_title = 'Soldatova Song'
admin.site.site_header = 'Soldatova Song'
