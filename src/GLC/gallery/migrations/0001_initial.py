# Generated by Django 2.2.1 on 2019-05-09 04:19

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='picture/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
