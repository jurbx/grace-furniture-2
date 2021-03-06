# Generated by Django 4.0.1 on 2022-02-23 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_herosection_priority'),
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusen',
            name='obj',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_page.aboutus', verbose_name='Обьект до якого відноситься англійський варіант'),
        ),
        migrations.AlterField(
            model_name='herosectionen',
            name='section',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_page.herosection', verbose_name='Секція до якої відноситься англійський варіант'),
        ),
    ]
