from django.db import models
from cart.models import SofaModel


class MainImages(models.Model):
    img = models.ImageField(upload_to='shopwindow/main_img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Головні фотографії вітрин'
        verbose_name = 'Головну фотографію'

    def __str__(self):
        return f'Головна фотораграфія №{self.id}'


class ImgUnderMainImage(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_under_main_img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Фотографії під головними фотографіями'
        verbose_name = 'Фотографію'

    def __str__(self):
        return f'Фотографія №{self.id}'


class ShopWindowUpperSlider(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_upper_slider', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Вернхій слайдер вітрин'
        verbose_name = 'Фотографію'

    def __str__(self):
        return f'Фотографія №{self.id}'


class ShopWindowImages(models.Model):
    img = models.ImageField(upload_to='shopwindow/img', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = ''
        verbose_name = 'Фотографію'

    def __str__(self):
        return f'Фотографія №{self.id}'


class ShopWindowLowerSlider(models.Model):
    img = models.ImageField(upload_to='shopwindow/img_upper_slider', verbose_name='Фотографія')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE, verbose_name='Диван до якого відноситься фотографія')

    class Meta:
        verbose_name_plural = 'Нижній слайдер вітрин'
        verbose_name = 'Фотографію'

    def __str__(self):
        return f'Фотографія №{self.id}'