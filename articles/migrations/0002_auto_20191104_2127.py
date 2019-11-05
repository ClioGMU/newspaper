# Generated by Django 2.2.6 on 2019-11-05 02:27

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_img',
            field=models.ImageField(null=True, upload_to=articles.models.uuid_filename),
        ),
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf/%Y/%m/%d/'),
        ),
    ]
