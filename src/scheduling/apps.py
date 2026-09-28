"""App-Konfiguration der Fach-App ``scheduling``."""

from django.apps import AppConfig


class SchedulingConfig(AppConfig):
    """Konfiguration der App für die Schichtplanung."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "scheduling"
    verbose_name = "Schichtplanung"
