# Generated by Django 4.0.1 on 2022-02-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_paginatorlimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofamodel',
            name='show_in_main_page',
            field=models.BooleanField(default=True),
        ),
    ]
