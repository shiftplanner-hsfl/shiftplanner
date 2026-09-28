# ShiftPlanner

> Faire, nachvollziehbare automatische Schichtplanung für kleine Betriebe und Filialen
> großer Unternehmen (5–30 Beschäftigte).
> Software-Projekt, Hochschule Flensburg, WS 2026/27 (Prof. Kai Petersen)

## Team und Verantwortlichkeiten

| Verantwortung | Hauptverantwortlich | GitHub |
|---|---|---|
| Anforderungen | Muhammed Asif Shahul Hameed | @muhammedasifshahulhameed-01 |
| Management | Muhammed Asif Shahul Hameed | @muhammedasifshahulhameed-01 |
| Architektur & Entwurf | Mahdi Fazeli | @mahdifazeli46-ux |
| Implementierung | Bennet Schalow | @BennetS4 |
| Qualitätssicherung | Anil Duth | @AnilD-00 |

Hauptverantwortung bedeutet Koordination und Vollständigkeit des Arbeitsergebnisses –
nicht, dass die Person allein daran arbeitet.

## Projektorganisation

- **Board:** GitHub Projects „ShiftPlanner – Backlog & Sprints“ (Organisation `shiftplanner-hsfl` → Projects)
- **Sprints:** Meilensteine „Sprint 0“ bis „Sprint 6“, jeweils bis zur nächsten Pflichtpräsentation
- **Arbeitsweise, Commit-Regeln, Definition of Done:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Kundenfeedback:** [docs/06_feedback/feedback-log.md](docs/06_feedback/feedback-log.md)

## Repository-Struktur

```text
.github/              CI-Workflow, Issue- und PR-Vorlagen, CODEOWNERS
docs/
  00_team/            Rollenverteilung, Teamprofile, Entscheidungsregeln
  01_anforderungen/   Produktidee, Hypothesen, Anforderungen  (-> *_requirements.pdf)
  02_entwurf/         Architektur, Detailentwurf, Datenmodell  (-> *_design.pdf)
  03_implementierung/ Coding-Guidelines, Implementierungsdoku
  04_testen/          Teststrategie, Testfälle, Reviews, Ergebnisse (-> *_testing.pdf)
  05_management/      Vorgehensmodell, Werkzeuge, Aufwand, Statistik (-> *_management.pdf)
  06_feedback/        Feedback-Log realer Kundinnen/Kunden und Expertinnen/Experten
  praesentationen/    Folien P1–P7
src/                  Django-Anwendung (config = Projekt, scheduling = Fach-App)
tests/                Automatisierte Tests (unit, integration, acceptance)
tools/                Hilfsskripte (z. B. Projektstatistik)
```

## Schnellstart (lokal)

```bash
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# macOS/Linux:          source .venv/bin/activate
pip install -r requirements-dev.txt
python src/manage.py migrate
python src/manage.py runserver          # -> http://127.0.0.1:8000
pytest                                  # alle Tests
ruff check . && ruff format --check .   # Coding-Standard prüfen
```
