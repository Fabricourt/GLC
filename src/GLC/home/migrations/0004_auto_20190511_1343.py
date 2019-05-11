# Generated by Django 2.2.1 on 2019-05-11 10:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190509_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='footer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='phone2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
