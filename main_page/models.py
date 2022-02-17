from django.db import models

from cart.models import SofaModel


class HeroSection(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to='section/img')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинки'

    def __str__(self):
        return self.title