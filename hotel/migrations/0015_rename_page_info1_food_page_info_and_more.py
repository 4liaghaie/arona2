# Generated by Django 4.0.2 on 2023-06-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_food_info_en_food_info_tr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='page_info1',
            new_name='page_info',
        ),
        migrations.RemoveField(
            model_name='food',
            name='page_info2',
        ),
        migrations.AddField(
            model_name='villa',
            name='page_info',
            field=models.TextField(null=True),
        ),
    ]