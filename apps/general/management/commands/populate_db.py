import requests

from django.core.management.base import BaseCommand

from apps.actors_and_directors.models import ActorAndDirector
from apps.films.models import Film, FilmActor
from apps.general.constants import OMDb_API_KEY


class Command(BaseCommand):
    help = "Populate the database with movies from OMDb API"

    def handle(self, *args, **kwargs):
        """Method for population database from thirdy part API."""
        url = f"http://www.omdbapi.com/?apikey={OMDb_API_KEY}&i=tt3896198"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            director, _ = ActorAndDirector.objects.get_or_create(name=data["Director"])

            film, _ = Film.objects.get_or_create(
                title=data["Title"],
                release_year=data["Year"],
                director=director
            )
            actors = (data["Actors"]).strip().split(",")

            for actor_name in actors:
                actor, _ = ActorAndDirector.objects.get_or_create(name=actor_name)
                FilmActor.objects.get_or_create(film=film, actor=actor)

            self.stdout.write(self.style.SUCCESS("All data were created!"))
        else:
            self.stdout.write("Connection to url refused")
