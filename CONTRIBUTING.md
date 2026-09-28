# Arbeitsweise im Team

## 1. Grundregel

Jede Arbeit beginnt mit einem Issue auf dem Board – auch Dokumentation, Interviews und
Präsentationen. So bleiben Fortschritt, Aufwand und Traceability jederzeit nachvollziehbar.

## 2. Ablauf für jede Aufgabe

1. Issue auf dem Board nach **In Progress** ziehen und sich selbst zuweisen.
2. Aktuellen Stand holen und Branch anlegen:
   ```bash
   git switch main
   git pull
   git switch -c <typ>/<issue-nr>-<kurzname>     # z. B. docs/6-hypothesen
   ```
   Branch-Typen: `feature`, `fix`, `docs`, `test`, `chore`.
3. Klein und häufig committen (Format siehe Abschnitt 3).
4. Pushen und Pull Request öffnen:
   ```bash
   git push -u origin HEAD
   gh pr create --fill        # oder über die GitHub-Website
   ```
   Im PR-Text steht `Closes #<issue-nr>` – dann schließt sich das Issue beim Merge.
5. Mindestens ein anderes Teammitglied reviewt (Leitfaden unter `docs/04_testen/`).
6. Die CI (ruff + pytest) muss grün sein.
7. Merge über **Create a merge commit**. So bleiben alle Einzel-Commits für die
   Projektstatistik erhalten. Der Branch wird automatisch gelöscht, das Board setzt „Done“.

## 3. Commit-Nachrichten (Conventional Commits)

```text
<typ>(<bereich>): <kurze Beschreibung im Imperativ> (#<issue-nr>)
```

Typen: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.
Beispiele:

```text
docs(anforderungen): Hypothesen H1–H5 ergänzen (#6)
feat(scheduling): Ruhezeitprüfung nach ArbZG umsetzen (#31)
test(scheduling): Grenzfall 11 h Ruhezeit abdecken (#31)
```

## 4. Aufwandserfassung

Jede Person trägt ihren Aufwand in ihre eigene Datei
`docs/05_management/aufwand/<name>.csv` ein (eigene Datei = keine Merge-Konflikte),
am besten im selben Pull Request wie die Arbeit.
Erlaubte Werte in `aktivitaet`: `anforderungen`, `architektur`, `implementierung`, `qa`,
`management`. Auswertung: `python tools/projekt_statistik.py`.

## 5. Definition of Done

- Akzeptanzkriterien des Issues erfüllt
- Review durch mindestens eine weitere Person
- CI grün; neuer Code hat Tests
- Dokumentation (Docstrings bzw. `docs/`) aktualisiert, Aufwand erfasst
- Bei Anforderungen: Quelle bzw. Feedback-ID eingetragen (Traceability)

## 6. Git-Identität

```bash
git config --global user.name "Vorname Nachname"
git config --global user.email "die-bei-github-hinterlegte@adresse"
```

Nur wenn die E-Mail zum GitHub-Konto passt, werden Commits eurem Profil zugeordnet.
Mehrere Adressen einer Person lassen sich über eine `.mailmap` zusammenführen.
