# Generated by Django 4.0.1 on 2022-02-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_sofamodel_show_in_main_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sofamodel',
            name='show_in_main_page',
        ),
        migrations.AddField(
            model_name='sofamodels',
            name='show_in_main_page',
            field=models.BooleanField(default=True, verbose_name='Показувати на головній сторінці'),
        ),
    ]