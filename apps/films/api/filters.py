import django_filters as filters


class FilmFilterSet(filters.FilterSet):
    """Film fields filterset."""

    min_year = filters.NumberFilter(field_name='year', lookup_expr='gte')
    max_year = filters.NumberFilter(field_name='year', lookup_expr='lte')
    director = filters.CharFilter(field_name='director__name', lookup_expr='icontains')
    actor = filters.CharFilter(field_name='film_actor__actor__name', lookup_expr='icontains')
