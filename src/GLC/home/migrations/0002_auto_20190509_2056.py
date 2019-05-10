# Generated by Django 2.2.1 on 2019-05-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='head',
            name='logo_short_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='head',
            name='motivational_statement',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='topbar',
            name='statement',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
