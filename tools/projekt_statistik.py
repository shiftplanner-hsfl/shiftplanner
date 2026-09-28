"""Erzeugt Projektstatistiken für Präsentationen und das Management-Dokument.

Auswertungen:
    1. Commits je Person und je Kalenderwoche (Anzahl und Frequenz)
    2. Codezuwachs über die Zeit (hinzugefügte/entfernte Zeilen je Woche, kumuliert)
    3. Hauptbeitragende je Datei (meiste hinzugefügte Zeilen)
    4. Aufwand je Person und Aktivität aus docs/05_management/aufwand/*.csv

Aufruf:
    python tools/projekt_statistik.py
    python tools/projekt_statistik.py --ausgabe docs/05_management/statistik.md
"""

import argparse
import csv
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
AKTIVITAETEN = ["anforderungen", "architektur", "implementierung", "qa", "management"]


def lies_commits() -> list[dict]:
    """Liest die Commit-Historie (ohne Merge-Commits) mit Zeilenstatistik ein.

    Returns:
        Liste von Commits mit den Schlüsseln ``autor``, ``datum`` und ``dateien``
        (Liste von Tupeln ``(pfad, hinzugefuegt, entfernt)``).
    """
    ausgabe = subprocess.run(
        [
            "git",
            "log",
            "--no-merges",
            "--numstat",
            "--date=iso-strict",
            "--pretty=format:@@%aN|%ad",
        ],
        cwd=WURZEL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout
    commits: list[dict] = []
    for zeile in ausgabe.splitlines():
        if zeile.startswith("@@"):
            autor, datum = zeile[2:].split("|", 1)
            commits.append({"autor": autor, "datum": datetime.fromisoformat(datum), "dateien": []})
        elif zeile.strip() and commits:
            plus, minus, pfad = zeile.split("\t", 2)
            if plus != "-":  # "-" = Binärdatei
                commits[-1]["dateien"].append((pfad, int(plus), int(minus)))
    return commits


def kalenderwoche(datum: datetime) -> str:
    """Formatiert ein Datum als ``JJJJ-KWnn``.

    Args:
        datum: Zeitpunkt des Commits.

    Returns:
        Kalenderwoche als Text.
    """
    jahr, woche, _ = datum.isocalendar()
    return f"{jahr}-KW{woche:02d}"


def tabelle(kopf: list[str], zeilen: list[list]) -> str:
    """Erzeugt eine Markdown-Tabelle.

    Args:
        kopf: Spaltenüberschriften.
        zeilen: Tabelleninhalt.

    Returns:
        Tabelle als Markdown-Text.
    """
    teile = ["| " + " | ".join(kopf) + " |", "|" + "---|" * len(kopf)]
    teile += ["| " + " | ".join(str(z) for z in zeile) + " |" for zeile in zeilen]
    return "\n".join(teile)


def auswertung_commits(commits: list[dict]) -> str:
    """Commits je Person und je Woche sowie Codezuwachs.

    Args:
        commits: Ergebnis von :func:`lies_commits`.

    Returns:
        Markdown-Abschnitt.
    """
    je_person = Counter(c["autor"] for c in commits)
    wochen: dict[str, Counter] = defaultdict(Counter)
    zuwachs: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for c in commits:
        kw = kalenderwoche(c["datum"])
        wochen[kw][c["autor"]] += 1
        for _, plus, minus in c["dateien"]:
            zuwachs[kw][0] += plus
            zuwachs[kw][1] += minus
    personen = sorted(je_person)
    teil = [
        "## Commits je Person",
        "",
        tabelle(["Person", "Commits"], [[p, je_person[p]] for p in personen]),
        "",
        "## Commits je Kalenderwoche",
        "",
        tabelle(
            ["Woche", *personen, "Summe"],
            [
                [kw, *(wochen[kw][p] for p in personen), sum(wochen[kw].values())]
                for kw in sorted(wochen)
            ],
        ),
        "",
        "## Codezuwachs über die Zeit",
        "",
    ]
    kumuliert, zeilen = 0, []
    for kw in sorted(zuwachs):
        plus, minus = zuwachs[kw]
        kumuliert += plus - minus
        zeilen.append([kw, f"+{plus}", f"-{minus}", kumuliert])
    teil.append(tabelle(["Woche", "hinzugefügt", "entfernt", "Zeilen gesamt"], zeilen))
    return "\n".join(teil)


def auswertung_dateien(commits: list[dict]) -> str:
    """Hauptbeitragende je Datei (nach hinzugefügten Zeilen).

    Args:
        commits: Ergebnis von :func:`lies_commits`.

    Returns:
        Markdown-Abschnitt.
    """
    je_datei: dict[str, Counter] = defaultdict(Counter)
    for c in commits:
        for pfad, plus, _ in c["dateien"]:
            je_datei[pfad][c["autor"]] += plus
    zeilen = []
    for pfad in sorted(je_datei):
        if not (WURZEL / pfad).exists():
            continue  # gelöschte oder umbenannte Dateien auslassen
        autor, anzahl = je_datei[pfad].most_common(1)[0]
        gesamt = sum(je_datei[pfad].values()) or 1
        zeilen.append([pfad, autor, f"{100 * anzahl // gesamt} %"])
    return "## Hauptbeitragende je Datei\n\n" + tabelle(
        ["Datei", "Hauptbeitragende/r", "Anteil"], zeilen
    )


def auswertung_aufwand() -> str:
    """Aufwand in Stunden je Person und Aktivität.

    Returns:
        Markdown-Abschnitt.
    """
    stunden: dict[str, Counter] = defaultdict(Counter)
    for datei in sorted((WURZEL / "docs/05_management/aufwand").glob("*.csv")):
        with datei.open(encoding="utf-8") as f:
            for zeile in csv.DictReader(f):
                if zeile.get("stunden"):
                    person = zeile["person"] or datei.stem
                    stunden[person][zeile["aktivitaet"].strip().lower()] += float(
                        zeile["stunden"].replace(",", ".")
                    )
    zeilen = [
        [p, *(f"{stunden[p][a]:.1f}" for a in AKTIVITAETEN), f"{sum(stunden[p].values()):.1f}"]
        for p in sorted(stunden)
    ]
    return "## Aufwand je Person und Aktivität (Stunden)\n\n" + tabelle(
        ["Person", *AKTIVITAETEN, "Summe"], zeilen
    )


def main() -> None:
    """Erzeugt alle Auswertungen und gibt sie aus bzw. schreibt sie in eine Datei."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ausgabe", help="Pfad der Markdown-Datei (sonst Bildschirm)")
    args = parser.parse_args()
    commits = lies_commits()
    bericht = (
        "\n\n".join(
            [
                f"# Projektstatistik (Stand {datetime.now():%d.%m.%Y})",
                auswertung_commits(commits),
                auswertung_dateien(commits),
                auswertung_aufwand(),
            ]
        )
        + "\n"
    )
    if args.ausgabe:
        Path(args.ausgabe).write_text(bericht, encoding="utf-8")
        print(f"Geschrieben: {args.ausgabe}")
    else:
        print(bericht)


if __name__ == "__main__":
    main()
