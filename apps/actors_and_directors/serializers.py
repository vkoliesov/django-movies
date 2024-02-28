from rest_framework import serializers

from apps.actors_and_directors.models import ActorAndDirector


class ActorAndDirectorSerializer(serializers.ModelSerializer):
    """Actor and Director model serializer."""

    class Meta:
        model = ActorAndDirector
        fields = ("id", "name")
