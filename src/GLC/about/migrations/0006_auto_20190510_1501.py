# Generated by Django 2.2.1 on 2019-05-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20190507_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='statements',
            field=models.TextField(blank=True, null=True),
        ),
    ]
