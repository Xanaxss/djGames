# Generated by Django 5.1.4 on 2024-12-15 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelcompany',
            name='image',
        ),
        migrations.RemoveField(
            model_name='modelgame',
            name='image',
        ),
        migrations.CreateModel(
            name='ModelImageCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelcompany')),
            ],
        ),
        migrations.CreateModel(
            name='ModelImageGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.modelgame')),
            ],
        ),
        migrations.DeleteModel(
            name='ModelImage',
        ),
    ]
