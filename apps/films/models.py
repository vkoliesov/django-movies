from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.films.utils import get_today_year


class Film(models.Model):
    """Model for films."""

    title = models.CharField(_("Title"), max_length=200)
    release_year = models.PositiveIntegerField(
        _("Release year"),
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(get_today_year())
        ],
    )
    director = models.ForeignKey(
        "actors_and_directors.ActorAndDirector",
        on_delete=models.CASCADE,
        related_name="films",
        related_query_name="film"
    )

    class Meta:
        ordering = ("title", "-release_year")
        verbose_name = _("Film")
        verbose_name_plural = _("Films")
        indexes = [
            models.Index(fields=["release_year"])
        ]

    def __str__(self):
        """Representation method."""
        return self.title


class FilmActor(models.Model):
    """Film Actor model."""

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name="film_actors",
        related_query_name="film_actor"
    )
    actor = models.ForeignKey(
        "actors_and_directors.ActorAndDirector",
        on_delete=models.CASCADE,
        related_name="film_actors",
        related_query_name="film_actor"
    )

    class Meta:
        verbose_name = _("Film actor")
        verbose_name_plural = _("Film actors")
        unique_together = ("film", "actor")

    def __str__(self):
        """Representation method."""
        return f"{self.film.title} - {self.actor.name}"
