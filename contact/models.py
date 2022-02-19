from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адреса')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=200, verbose_name='Email')

    class Meta:
        verbose_name_plural = 'Контакти'
        verbose_name = 'Контакти'


class TitleOurShop(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)\


    class Meta:
        verbose_name_plural = 'Наші магазини'
        verbose_name = 'Наш магазин'


class OurShops(models.Model):
    title = models.ForeignKey(TitleOurShop, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, verbose_name='Назва міста')
    info = models.TextField(max_length=1000, verbose_name='Інформація про постачальників')

    class Meta:
        verbose_name_plural = 'Наші магазини'
        verbose_name = 'Наш магазин'
