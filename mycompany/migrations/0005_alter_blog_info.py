# Generated by Django 3.2 on 2022-01-19 20:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='info',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Açıklama:'),
        ),
    ]
