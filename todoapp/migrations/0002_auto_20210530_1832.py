# Generated by Django 3.1.8 on 2021-05-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='published_On',
            field=models.DateTimeField(blank=True, verbose_name=False),
        ),
    ]
