from django.db import models
from main_page.models import HeroSection, AboutUs

# Main Page


class HeroSectionEn(models.Model):
    section = models.ForeignKey(HeroSection, on_delete=models.CASCADE,
                                verbose_name='Секція до якої відноситься англійський варіант')
    title = models.CharField(max_length=100, verbose_name='Заголовок до картинки англійською')
    context = models.TextField(max_length=500, blank=True, verbose_name='Текст до картинки англійською')
    priority = models.PositiveIntegerField(default=1, verbose_name='Пріоритет показу')

    class Meta:
        verbose_name_plural = 'Головні картинки(english)'
        verbose_name = 'Головну картинку(english)'


class AboutUsEn(models.Model):
    obj = models.ForeignKey(AboutUs, on_delete=models.CASCADE,
                            verbose_name='Обьект до якого відноситься англійський варіант')
    title = models.CharField(max_length=100, verbose_name='Заголовок англійською')
    desc = models.TextField(max_length=1000, verbose_name='Текст під заголовком англійською')


# End Main Page