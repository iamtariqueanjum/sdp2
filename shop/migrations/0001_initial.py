# Generated by Django 3.0.5 on 2021-05-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0005_dealer'),
        ('models', '0003_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='shop/')),
                ('description', models.TextField()),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('mileage', models.CharField(blank=True, max_length=20, null=True)),
                ('fuel', models.CharField(blank=True, max_length=20, null=True)),
                ('engine_size', models.CharField(blank=True, max_length=20, null=True)),
                ('power', models.CharField(blank=True, max_length=20, null=True)),
                ('gear_box', models.CharField(blank=True, max_length=20, null=True)),
                ('seats', models.CharField(blank=True, max_length=20, null=True)),
                ('doors', models.CharField(blank=True, max_length=20, null=True)),
                ('colors', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('kilometer', models.CharField(blank=True, max_length=100, null=True)),
                ('reg_no', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.City')),
                ('make', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Make')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Model')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.State')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Variant')),
            ],
        ),
    ]
