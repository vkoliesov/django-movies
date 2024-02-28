from django.contrib import admin

from apps.actors_and_directors.models import ActorAndDirector
from apps.films.models import FilmActor


class FilmActorInline(admin.TabularInline):
    """Film Actor inline to use in ActorAndDirectorAdmin class."""

    model = FilmActor
    extra = 0
    classes = ("collapse",)
    ordering = ("film__title",)

    def get_queryset(self, request):
        """Method to retrive base queryset."""
        return super().get_queryset(request).select_related("actor", "film")


@admin.register(ActorAndDirector)
class ActorAndDirectorAdmin(admin.ModelAdmin):
    """Actor and Director admin site settings."""

    search_fields = ("name", )
    inlines = (FilmActorInline,)
