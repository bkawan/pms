# Generated by Django 2.0 on 2017-12-07 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_caption',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_source',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_title',
        ),
    ]
