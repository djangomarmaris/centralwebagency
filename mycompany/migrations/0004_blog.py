# Generated by Django 3.2 on 2022-01-19 20:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0003_referance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title:')),
                ('title_info', models.CharField(max_length=50, verbose_name='Title İnfo:')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('info', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('info2', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('red', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('info3', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('big_image', models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='Büyük resim:')),
                ('title2', models.CharField(max_length=50, verbose_name='Title Two:')),
                ('info4', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('black', models.CharField(max_length=100, verbose_name='Black:')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
            ],
        ),
    ]
