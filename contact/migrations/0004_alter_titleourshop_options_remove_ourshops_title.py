# Generated by Django 4.0.1 on 2022-02-21 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_titleourshop_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titleourshop',
            options={'verbose_name': 'Текст над нашими магазинами', 'verbose_name_plural': 'Текст над нашими магазинами'},
        ),
        migrations.RemoveField(
            model_name='ourshops',
            name='title',
        ),
    ]
