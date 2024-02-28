from django.utils import timezone


def get_today_datetime():
    """Get today date and time method."""
    return timezone.now()


def get_today_year():
    """Get today year method."""
    return get_today_datetime().year
