# Generated by Django 4.2.4 on 2023-08-11 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_adv', '0003_advert_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(default='', upload_to='BASE_DIR', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]