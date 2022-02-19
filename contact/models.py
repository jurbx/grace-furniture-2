from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адреса')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=200, verbose_name='Email')

    class Meta:
        verbose_name_plural = 'Контакти'
        verbose_name = 'Контакти'


class OurShops(models.Model):
    city = models.CharField(max_length=100, verbose_name='Назва міста')
    info = models.TextField(max_length=1000, verbose_name='Інформація про постачальників')

    class Meta:
        verbose_name_plural = 'Наш магазин'
        verbose_name = 'Наші магазини'