# Generated by Django 2.1.7 on 2019-06-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_topbar_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='head',
            name='home_header_1',
            field=models.ImageField(blank=True, null=True, upload_to='home_header/'),
        ),
        migrations.AddField(
            model_name='head',
            name='home_header_2',
            field=models.ImageField(blank=True, null=True, upload_to='home_header/'),
        ),
        migrations.AddField(
            model_name='head',
            name='home_header_3',
            field=models.ImageField(blank=True, null=True, upload_to='home_header/'),
        ),
        migrations.AddField(
            model_name='head',
            name='home_header_4',
            field=models.ImageField(blank=True, null=True, upload_to='home_header/'),
        ),
        migrations.AddField(
            model_name='head',
            name='home_header_5',
            field=models.ImageField(blank=True, null=True, upload_to='home_header/'),
        ),
    ]
