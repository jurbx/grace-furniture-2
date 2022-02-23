from django.db import models


class Contact(models.Model):
    address = models.TextField(max_length=200, verbose_name='Адреса')
    phone = models.TextField(max_length=100, verbose_name='Телефон')
    email = models.TextField(max_length=200, verbose_name='Email')
    address_english = models.TextField(max_length=200, verbose_name='Адреса(english)', default='.', blank=True)

    class Meta:
        verbose_name_plural = 'Контакти'
        verbose_name = 'Контакти'

    def __str__(self):
        return f'Обєкт контактів №{self.id}'


class TitleOurShop(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500, blank=True)

    title_english = models.CharField(max_length=200, default='.', blank=True)
    desc_english = models.TextField(max_length=500, blank=True, default='.')

    class Meta:
        verbose_name_plural = 'Текст над нашими магазинами'
        verbose_name = 'Текст над нашими магазинами'

    def __str__(self):
        return self.title


class OurShops(models.Model):
    city = models.CharField(max_length=100, verbose_name='Назва міста')
    info = models.TextField(max_length=1000, verbose_name='Інформація про мазагини')

    city_english = models.CharField(max_length=100, verbose_name='Назва міста англійською', default='.', blank=True)
    info_english = models.TextField(max_length=1000, verbose_name='Інформація про мазагини англійською',
                                default='.', blank=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Наші магазини'
        verbose_name = 'Наш магазин'
