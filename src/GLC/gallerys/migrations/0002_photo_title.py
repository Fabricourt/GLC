# Generated by Django 2.1.7 on 2019-06-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallerys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
