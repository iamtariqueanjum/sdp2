# Generated by Django 3.0.5 on 2021-05-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0014_auto_20210518_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='newcars/'),
        ),
    ]
