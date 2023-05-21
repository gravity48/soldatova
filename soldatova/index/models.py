from django.db import models


class MainHeader(models.Model):
    vk = models.SlugField('Ссылка ВК', max_length=200)
    telegram = models.CharField('Ссылка telegram', max_length=200)
    whatsapp = models.CharField('Ссылка whatsapp', max_length=200)
    instagram = models.CharField('Ссылка instagram', max_length=200)
    phone = models.CharField('Номер телефона', max_length=200, null=True)

    def __str__(self):
        return 'Контактная информация'

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'


class Reviews(models.Model):
    name = models.CharField('Имя отзыва', max_length=50)
    img_show = models.BooleanField('Черновик', default=True)
    review_img = models.ImageField(
        'Изображение', height_field="img_height", width_field="img_width", upload_to='review/'
    )
    img_width = models.PositiveIntegerField('Высота', blank=True)
    img_height = models.PositiveIntegerField('Ширина', blank=True)
    date_join = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Block2Content(models.Model):
    card_text = models.TextField('Текст карточки')

    def __str__(self):
        return f'Текст {self.id} блока'

    class Meta:
        db_table = 'block2'
        verbose_name = 'Контент второго блока'
        verbose_name_plural = 'Контент второго блока'
