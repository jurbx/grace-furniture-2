# Generated by Django 4.0.1 on 2022-02-21 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopwindow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imgundermainimage',
            options={'verbose_name': 'Фотографію', 'verbose_name_plural': 'Фотографії під головними фотографіями'},
        ),
        migrations.AlterModelOptions(
            name='mainimages',
            options={'verbose_name': 'Головну фотографію', 'verbose_name_plural': 'Головні фотографії вітрин'},
        ),
        migrations.AlterModelOptions(
            name='shopwindowimages',
            options={'verbose_name': 'Фотографію', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='shopwindowlowerslider',
            options={'verbose_name': 'Фотографію', 'verbose_name_plural': 'Нижній слайдер вітрин'},
        ),
        migrations.AlterModelOptions(
            name='shopwindowupperslider',
            options={'verbose_name': 'Фотографію', 'verbose_name_plural': 'Вернхій слайдер вітрин'},
        ),
    ]
