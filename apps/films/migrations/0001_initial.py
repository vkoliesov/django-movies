# Generated by Django 3.2.24 on 2024-02-28 09:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors_and_directors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2024)], verbose_name='Release year')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', related_query_name='film', to='actors_and_directors.actoranddirector')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'ordering': ('title', '-release_year'),
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_actors', related_query_name='film_actor', to='actors_and_directors.actoranddirector')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_actors', related_query_name='film_actor', to='films.film')),
            ],
            options={
                'verbose_name': 'Film actor',
                'verbose_name_plural': 'Film actors',
                'unique_together': {('film', 'actor')},
            },
        ),
        migrations.AddIndex(
            model_name='film',
            index=models.Index(fields=['release_year'], name='films_film_release_ecd8a1_idx'),
        ),
    ]
