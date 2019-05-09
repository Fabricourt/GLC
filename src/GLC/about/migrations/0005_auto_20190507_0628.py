# Generated by Django 2.2.1 on 2019-05-07 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='header',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
