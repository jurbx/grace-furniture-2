from django.db import models


class Page404(models.Model):
    img = models.ImageField(upload_to='404/img')


class Logo(models.Model):
    img = models.ImageField(upload_to='logo/img')

    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'


class SocialNetwork(models.Model):
    instagram = models.URLField(default='https://www.instagram.com/')
    facebook = models.URLField(default='https://www.facebook.com/')
    telegram = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Соціальні мережі'
        verbose_name = 'Соціальні мережі'
