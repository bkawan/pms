# Generated by Django 2.0 on 2018-02-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('service', models.CharField(blank=True, max_length=255, null=True)),
                ('team_member', models.CharField(blank=True, max_length=255, null=True)),
                ('company_detail', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]