"""Views der Fach-App: nehmen Anfragen entgegen und liefern Antworten."""

from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """Zeigt die Startseite als Lebenszeichen des Grundgerüsts.

    Args:
        request: Eingehende HTTP-Anfrage.

    Returns:
        HTML-Antwort mit Status 200.
    """
    return HttpResponse("<h1>ShiftPlanner</h1><p>Das Grundgerüst läuft.</p>")
