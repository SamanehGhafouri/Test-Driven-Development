# Generated by Django 3.1.7 on 2021-03-21 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]
