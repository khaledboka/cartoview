# Generated by Django 2.2 on 2019-04-14 11:04

import cartoview.base_resource.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_resource', '0002_basemodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=cartoview.base_resource.models.thumbnail_path),
        ),
    ]
