from rest_framework.routers import SimpleRouter

from apps.films.api.v1.api import FilmViewSet, FilmActorViewSet

v1_films = SimpleRouter()
v1_films.register("films", FilmViewSet)

v1_film_actors = SimpleRouter()
v1_film_actors.register("film_actors", FilmActorViewSet)
