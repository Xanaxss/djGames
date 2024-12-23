# Generated by Django 5.1.4 on 2024-12-15 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_remove_modelcompany_image_remove_modelgame_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelcomment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='modelcompany',
            options={'verbose_name': 'Разработчик', 'verbose_name_plural': 'Разработчики'},
        ),
        migrations.AlterModelOptions(
            name='modelgame',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterModelOptions(
            name='modelimagecompany',
            options={'verbose_name': 'Изображения для разработчиков', 'verbose_name_plural': 'Изображения для разработчиков'},
        ),
        migrations.AlterModelOptions(
            name='modelimagegame',
            options={'verbose_name': 'Изображения для игры', 'verbose_name_plural': 'Изображения для игр'},
        ),
        migrations.AlterModelOptions(
            name='modelrating',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='modelcomment',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='modelcomment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelgame', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='modelcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='modelcompany',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='modelcompany',
            name='date_created',
            field=models.DateField(verbose_name='Дата основания'),
        ),
        migrations.AlterField(
            model_name='modelcompany',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelcompany',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelgame',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelcompany', verbose_name='Разработчик'),
        ),
        migrations.AlterField(
            model_name='modelgame',
            name='date_published',
            field=models.DateField(verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='modelgame',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelgame',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelimagecompany',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelcompany', verbose_name='Разработчик'),
        ),
        migrations.AlterField(
            model_name='modelimagecompany',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelimagecompany',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='modelimagegame',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelimagegame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelgame', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='modelimagegame',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='modelrating',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelgame', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='modelrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='modelrating',
            name='value',
            field=models.IntegerField(verbose_name='Оценка'),
        ),
    ]
