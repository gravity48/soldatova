from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import MainHeader, Reviews, Block2Content


# Register your models here.


class Block2Form(forms.ModelForm):
    card_text = forms.CharField(label='Текст карточки', widget=CKEditorUploadingWidget())

    class Meta:
        model = Block2Content
        fields = '__all__'


@admin.register(Block2Content)
class Block2ContentAdmin(admin.ModelAdmin):
    form = Block2Form
    save_on_top = True


@admin.register(MainHeader)
class MainHeaderAdmin(admin.ModelAdmin):
    fields = (
        ("vk",),
        ("telegram",),
        ("whatsapp",),
        ("instagram",),
        ("phone",),
    )
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
