from django.contrib import admin

from apps.films.models import Film, FilmActor


class FilmActorInline(admin.TabularInline):
    """Film Actor inline to use in FilmAdmin class."""

    model = FilmActor
    extra = 0
    classes = ("collapse",)
    ordering = ("actor__name",)

    def get_queryset(self, request):
        """Method to retrive base queryset."""
        return super().get_queryset(request).select_related("actor", "film")


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Film admin site settings."""

    search_fields = ("title", "release_year", "director__name")
    ordering = ("title", "-release_year")
    inlines = (FilmActorInline,)

    def get_queryset(self, request):
        """Method to retrive base queryset."""
        return super().get_queryset(request).select_related("director")


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    """Film Actor admin site settings."""

    search_fields = ("actor__name", "film__name")
