# Generated by Django 4.2.10 on 2024-02-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_alter_class_obj_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
