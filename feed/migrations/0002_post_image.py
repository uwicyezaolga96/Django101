# Generated by Django 5.0.7 on 2024-08-14 06:27

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
