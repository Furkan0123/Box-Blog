# Generated by Django 4.2.10 on 2024-02-26 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_rename_category_class_obj_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_obj',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.category'),
        ),
    ]
