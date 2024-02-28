from django.db import models
from django.utils.translation import gettext_lazy as _


class ActorAndDirector(models.Model):
    """Model for actors and directors."""
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        """Representation method."""
        return self.name

    class Meta:
        verbose_name = _("Actor or Director")
        verbose_name_plural = _("Actors and Directors")
