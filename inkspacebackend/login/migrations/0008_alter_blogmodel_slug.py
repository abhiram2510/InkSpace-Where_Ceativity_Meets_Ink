# Generated by Django 4.2.5 on 2023-10-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_rename_blogdal_blogmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
