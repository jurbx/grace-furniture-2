from django.db import models
from django.utils.text import slugify


class SofaModels(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    img = models.ImageField(upload_to='cart/img/model_img')

    class Meta:
        verbose_name_plural = 'Модели диванов'
        verbose_name = 'Модели диванов'

    def __str__(self):
        return self.name


class SofaTypes(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name


class SofaColor(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name


class SofaModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    main_image = models.ImageField(upload_to='cart/img/main_img', blank=True, null=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, null=True, blank=True)
    category = models.ForeignKey(SofaModels, on_delete=models.CASCADE)
    sofa_type = models.ForeignKey(SofaTypes, on_delete=models.CASCADE)
    sofa_color = models.ForeignKey(SofaColor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Диваны'
        verbose_name = 'Диваны'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if self.slug == slug:
            pass
        else:
            self.slug = slug
        super().save(*args, **kwargs)


class CartImages(models.Model):
    img = models.ImageField(upload_to='cart/img')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE)


class Cart3dModels(models.Model):
    fbx_file = models.FileField(db_index=True, upload_to='cart/3d')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE)

