# Generated by Django 3.0.5 on 2021-05-16 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210516_2134'),
        ('models', '0004_auto_20210516_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Dealer'),
        ),
    ]