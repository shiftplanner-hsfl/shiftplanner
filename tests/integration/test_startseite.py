"""Integrationstest: Startseite des Grundgerüsts ist erreichbar."""

from django.urls import reverse


def test_startseite_liefert_status_200(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert "ShiftPlanner" in response.content.decode()
