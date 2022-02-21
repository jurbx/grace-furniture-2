from django.db import models


class Page404(models.Model):
    img = models.ImageField(upload_to='404/img')