from django.db import models
from django.utils.text import slugify


class SofaModels(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Назва моделі')
    img = models.ImageField(upload_to='cart/img/model_img', verbose_name='Картинка моделі')
    show_in_main_page = models.BooleanField(default=True, verbose_name='Показувати на головній сторінці')

    class Meta:
        verbose_name_plural = 'Моделі диванів'
        verbose_name = 'Модель дивану'

    def __str__(self):
        return self.name


class SofaTypes(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Назва типу')
    name_english = models.CharField(max_length=100, unique=True, blank=True, null=True,
                                    verbose_name='Назва типу англійською')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типи виробів'
        verbose_name = 'Тип виробу'


class SofaModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва дивану')
    desc = models.TextField(max_length=1000, verbose_name='Короткий опис товару')
    detail = models.TextField(max_length=2000, verbose_name='Детальний опис')
    characteristic = models.TextField(max_length=2000, verbose_name='Характеристики товару')
    main_image = models.ImageField(upload_to='cart/img/main_img', blank=True, null=True, verbose_name='Головна картинка')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, null=True, blank=True)
    category = models.ForeignKey(SofaModels, on_delete=models.CASCADE, verbose_name='Категорія')
    sofa_type = models.ForeignKey(SofaTypes, on_delete=models.CASCADE, verbose_name='Тип')
    priority = models.PositiveIntegerField(verbose_name='Приоритет показу диванів в каталозі', default=1)
    new = models.BooleanField(default=False, verbose_name='Новинка')
    title_english = models.CharField(max_length=100, verbose_name='Назва дивану англійською(Якщо в цьому є потреба)',
                                     blank=True, null=True)
    desc_english = models.TextField(max_length=1000, default='.', blank=True,
                                    verbose_name='Короткий опис товару англійською')
    detail_english = models.TextField(max_length=2000, default='.', blank=True,
                                      verbose_name='Детальний опис англійською')
    characteristic_english = models.TextField(max_length=2000, default='.', blank=True,
                                              verbose_name='Характеристики товару англійською')

    class Meta:
        verbose_name_plural = 'Дивани'
        verbose_name = 'Диван'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            slug = slugify(self.title)
            if id := SofaModel.objects.filter(slug=slug):
                if id.exists():
                    self.slug = f'{slug}{self.id}'
                    super().save(*args, **kwargs)
            else:
                self.slug = slug
                super(SofaModel, self).save(*args, *kwargs)


class CartImages(models.Model):
    img = models.ImageField(upload_to='cart/img', verbose_name='Додаткові фотографіі')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Фотографії'
        verbose_name = 'Фотографію'


class Cart3dModels(models.Model):
    fbx_file = models.FileField(db_index=True, upload_to='cart/3d', verbose_name='Файл 3Д моделі')
    sofa = models.ForeignKey(SofaModel, on_delete=models.CASCADE)


class PaginatorLimit(models.Model):
    number = models.PositiveIntegerField(default=9)