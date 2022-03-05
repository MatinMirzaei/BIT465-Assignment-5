# Generated by Django 4.0.2 on 2022-02-28 07:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('size', models.CharField(choices=[('T', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=2)),
                ('friendliness', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('trainability', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('sheddingamount', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('exerciseneeds', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('color', models.CharField(default='', max_length=50)),
                ('favoritefood', models.CharField(default='', max_length=200)),
                ('favoritetoy', models.CharField(default='', max_length=200)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.breed')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
