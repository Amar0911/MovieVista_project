# Generated by Django 5.1.1 on 2024-11-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel_movies',
            name='rating',
            field=models.DecimalField(decimal_places=1, default='0.0', max_digits=3),
        ),
    ]
