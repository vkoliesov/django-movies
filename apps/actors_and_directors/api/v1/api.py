from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.actors_and_directors.models import ActorAndDirector
from apps.actors_and_directors.serializers import ActorAndDirectorSerializer


@extend_schema(tags=["Actors and Directors"])
class ActorAndDirectorViewSet(viewsets.ModelViewSet):
    """Actor and Director project API."""

    queryset = ActorAndDirector.objects.all()
    serializer_class = ActorAndDirectorSerializer
