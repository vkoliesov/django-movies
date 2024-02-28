from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.films.models import Film, FilmActor
from apps.films.serializers import FilmSerializer, FilmActorSerializer

@extend_schema(tags=["Films"])
class FilmViewSet(viewsets.ModelViewSet):
    """Film project API."""

    queryset = Film.objects.all().select_related("director")
    serializer_class = FilmSerializer
    filterset_fields = ("title", "release_year", "director__name")


@extend_schema(tags=["Film Actors"])
class FilmActorViewSet(viewsets.ModelViewSet):
    """Film Actor project API."""

    queryset = FilmActor.objects.all().select_related("actor", "film")
    serializer_class = FilmActorSerializer
    filterset_fields = ("film__title", "film__release_year", "actor__name")
