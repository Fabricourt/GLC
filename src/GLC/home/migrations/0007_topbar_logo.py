# Generated by Django 2.1.7 on 2019-06-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190513_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbar',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
