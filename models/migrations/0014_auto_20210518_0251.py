# Generated by Django 3.0.5 on 2021-05-17 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_messages'),
        ('models', '0013_auto_20210518_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.User'),
        ),
    ]
