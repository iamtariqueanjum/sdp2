# Generated by Django 3.0.5 on 2021-05-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_delete_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='newcars/'),
        ),
    ]
