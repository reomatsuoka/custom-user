# Generated by Django 2.2.17 on 2021-01-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='store',
            name='tel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号'),
        ),
    ]
