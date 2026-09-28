# Coding-Guidelines (Entwurf)

Status: **Entwurf** – wird im Team abgestimmt (Issue „Coding-Guidelines entwerfen“).

| Regel | Begründung | Durchsetzung |
|---|---|---|
| PEP 8, max. 100 Zeichen pro Zeile | Einheitlicher Python-Standard | `ruff check` in der CI |
| Einheitliche Formatierung | Keine Diskussionen über Stil in Reviews | `ruff format --check` in der CI |
| Bezeichner auf Englisch, Kommentare und Docstrings auf Deutsch | Englisch ist in Django üblich; Doku ist Teil der Abgabe (Deutsch) | Review |
| Docstrings im Google-Stil für Module, Klassen, öffentliche Funktionen (Args/Returns/Raises) | Ein- und Ausgaben sowie Rolle einer Klasse erkennbar | `ruff` (Regeln D) |
| Fachlogik in `services.py`, Views nur für Ein-/Ausgabe | Testbarkeit, lose Kopplung | Review |
| Kein direkter Push auf `main` | Jede Änderung wird geprüft | Branch-Schutz |
