# Generated by Django 3.0.4 on 2020-11-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201123_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_slug',
            field=models.SlugField(max_length=350),
        ),
    ]
