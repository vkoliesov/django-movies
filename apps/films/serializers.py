from rest_framework import serializers

from apps.actors_and_directors.models import ActorAndDirector
from apps.films.models import Film, FilmActor


class ActorAndDirectorNestedSerializer(serializers.ModelSerializer):
    """Actor and Director model serializer."""

    class Meta:
        model = ActorAndDirector
        fields = ("id", "name")


class ActorNestedSerializer(serializers.ModelSerializer):

    actor = ActorAndDirectorNestedSerializer(read_only=True)

    class Meta:
        model = FilmActor
        fields = ("id", "actor",)


class FilmSerializer(serializers.ModelSerializer):
    """Film model serializer."""

    director = ActorAndDirectorNestedSerializer(read_only=True)
    director_id = serializers.IntegerField(write_only=True, required=False)
    actors = ActorNestedSerializer(source="film_actors", many=True, read_only=True)

    class Meta:
        model = Film
        fields = "__all__"


class FilmActorSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    film_id = serializers.IntegerField(write_only=True, required=False)
    actor = ActorAndDirectorNestedSerializer(read_only=True)
    actor_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = FilmActor
        fields = "__all__"
