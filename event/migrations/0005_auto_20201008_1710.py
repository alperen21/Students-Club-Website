# Generated by Django 3.1 on 2020-10-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20201008_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='Uzun tanıtım'),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(verbose_name='Kısa tanıtım'),
        ),
    ]
