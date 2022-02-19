from django.db import models

from cart.models import SofaModel


class HeroSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='Головні картинки')
    context = models.TextField(max_length=500, blank=True, verbose_name='Текст до картинки')
    img = models.ImageField(upload_to='section/img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься картинка')

    class Meta:
        verbose_name_plural = 'Головну картинки'
        verbose_name = 'Головні картинку'

    def __str__(self):
        return self.title


class ShopWindow(models.Model):
    img = models.ImageField(upload_to='shop_window/img', verbose_name='Картинка')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься картинка')

    class Meta:
        verbose_name_plural = 'Вітрини'
        verbose_name = 'Вітрини'


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desc = models.TextField(max_length=1000, verbose_name='Текст під заголовком')
    img = models.ImageField(upload_to='about_us/img', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Про нас'
        verbose_name = 'Про нас'
