# Generated by Django 2.0 on 2018-02-07 17:02

import apps.core.utils
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At.')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At.')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('featured_image', models.ImageField(upload_to=apps.core.utils.image_upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='gallery.AlbumCategory', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'Album category',
                'verbose_name_plural': 'Album categories',
            },
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At.')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At.')),
                ('image_title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, help_text='Image for the Content', upload_to=apps.core.utils.image_upload_to, verbose_name='image')),
                ('image_caption', models.CharField(blank=True, help_text="Image's caption.", max_length=255, null=True, verbose_name='caption')),
                ('image_source', models.CharField(blank=True, max_length=255, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Album')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='album',
            name='categories',
            field=models.ManyToManyField(blank=True, to='gallery.AlbumCategory'),
        ),
        migrations.AddField(
            model_name='album',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='company.CompanyDetail'),
        ),
    ]
