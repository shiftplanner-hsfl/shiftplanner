#!/usr/bin/env python
"""Kommandozeilenwerkzeug von Django für administrative Aufgaben."""

import os
import sys


def main() -> None:
    """Startet das Django-Kommandozeilenprogramm."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django ist nicht installiert. Virtuelle Umgebung aktivieren und "
            "'pip install -r requirements-dev.txt' ausführen."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
