# Generated by Django 4.2.5 on 2023-10-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(max_length=1000),
        ),
    ]
