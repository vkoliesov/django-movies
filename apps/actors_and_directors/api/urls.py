from rest_framework.routers import SimpleRouter

from apps.actors_and_directors.api.v1.api import ActorAndDirectorViewSet

v1_actors_and_directors = SimpleRouter()
v1_actors_and_directors.register("actors-and-directors", ActorAndDirectorViewSet)
