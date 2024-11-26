# Generated by Django 5.1.1 on 2024-11-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_trending_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('ANIME', 'anime')], max_length=20)),
                ('movie_vista_original', models.CharField(default='Movie Vista Original', max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('imdb', models.CharField(default='IMDB', max_length=20)),
                ('rating', models.DecimalField(decimal_places=1, default='0.0', max_digits=3)),
                ('anime_image', models.ImageField(upload_to='anime_images')),
            ],
        ),
    ]
