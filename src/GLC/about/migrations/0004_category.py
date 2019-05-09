# Generated by Django 2.2.1 on 2019-05-06 17:44

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20190506_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='image1/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
