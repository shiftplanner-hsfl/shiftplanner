"""Unit-Tests für die Fachlogik in ``scheduling.services``."""

from datetime import datetime

import pytest

from scheduling.services import is_rest_period_respected

ENDE = datetime(2026, 10, 1, 22, 0)


def test_genau_elf_stunden_ruhezeit_ist_erlaubt():
    assert is_rest_period_respected(ENDE, datetime(2026, 10, 2, 9, 0)) is True


def test_weniger_als_elf_stunden_ruhezeit_ist_verboten():
    assert is_rest_period_respected(ENDE, datetime(2026, 10, 2, 8, 59)) is False


def test_ueberlappende_schichten_loesen_fehler_aus():
    with pytest.raises(ValueError):
        is_rest_period_respected(ENDE, datetime(2026, 10, 1, 21, 0))
