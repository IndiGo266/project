# Generated by Django 4.2.4 on 2023-08-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0005_alter_advert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]
