# Generated by Django 2.0 on 2017-12-03 18:18

import apps.core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20171203_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=apps.core.utils.image_upload_to),
        ),
    ]
