# Generated by Django 4.0.1 on 2022-02-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_404', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='logo/img')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотип',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(default='https://www.instagram.com/')),
                ('facebook', models.URLField(default='https://www.facebook.com/')),
                ('telegram', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Соціальні мережі',
                'verbose_name_plural': 'Соціальні мережі',
            },
        ),
    ]
