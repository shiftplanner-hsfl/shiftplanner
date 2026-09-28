"""Fachlogik der Schichtplanung.

Enthält reine Python-Funktionen ohne Datenbankzugriff, damit sie einfach per
Unit-Test geprüft werden können.
"""

from datetime import datetime, timedelta

MIN_REST_HOURS = 11
"""Mindestruhezeit zwischen zwei Schichten in Stunden (§ 5 Abs. 1 ArbZG)."""


def is_rest_period_respected(
    shift_end: datetime, next_shift_start: datetime, min_rest_hours: int = MIN_REST_HOURS
) -> bool:
    """Prüft, ob zwischen zwei Schichten die Mindestruhezeit eingehalten wird.

    Args:
        shift_end: Ende der vorherigen Schicht.
        next_shift_start: Beginn der folgenden Schicht.
        min_rest_hours: Geforderte ununterbrochene Ruhezeit in Stunden.

    Returns:
        ``True``, wenn die Ruhezeit mindestens ``min_rest_hours`` beträgt, sonst ``False``.

    Raises:
        ValueError: Wenn die folgende Schicht vor dem Ende der vorherigen beginnt.
    """
    if next_shift_start < shift_end:
        raise ValueError("Die folgende Schicht beginnt vor dem Ende der vorherigen Schicht.")
    return next_shift_start - shift_end >= timedelta(hours=min_rest_hours)
