# Generated by Django 5.1.1 on 2024-11-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_anime_movies_director_anime_movies_producers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime_movies',
            name='producers',
        ),
        migrations.RemoveField(
            model_name='carousel_movies',
            name='producers',
        ),
        migrations.RemoveField(
            model_name='hollywood',
            name='producers',
        ),
        migrations.RemoveField(
            model_name='indian_movies',
            name='producers',
        ),
        migrations.RemoveField(
            model_name='trending_movies',
            name='producers',
        ),
        migrations.RemoveField(
            model_name='webseries',
            name='producers',
        ),
    ]
