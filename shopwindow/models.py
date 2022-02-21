from django.db import models
from cart.models import SofaModel


class MainImages(models.Model):
    img = models.ImageField(upload_to='shopwindow/main_img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Головні фотографії вітрин'
        verbose_name = 'Головну фотографію для вітрини'


class ImgUnderMainImage(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_under_main_img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Фотографії під головними фотографіями'
        verbose_name = 'Фотографію під головними фотографіями'


class ShopWindowUpperSlider(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_upper_slider', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = ''
        verbose_name = ''


class ShopWindowImages(models.Model):
    img = models.ImageField(upload_to='shopwindow/img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = ''
        verbose_name = ''


class ShopWindowLowerSlider(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_upper_slider', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = ''
        verbose_name = ''