# Generated by Django 3.0.3 on 2020-02-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_candy_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='candy',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='candy_pics'),
        ),
    ]
