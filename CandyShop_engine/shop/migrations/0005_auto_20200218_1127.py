# Generated by Django 3.0.3 on 2020-02-18 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200218_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candy',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
