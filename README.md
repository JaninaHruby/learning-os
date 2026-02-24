# 🎹 Learning OS — POP Keys Edition

> Ein persönliches Lern-Dashboard das parallele Zertifizierungsprogramme trackt, Fortschritte automatisch berechnet und auf allen Geräten läuft.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.132-009688?style=flat-square&logo=fastapi&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Backend-34A853?style=flat-square&logo=googlesheets&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Was ist Learning OS?

Learning OS ist ein selbst gehostetes Web-Dashboard für Menschen die mehrere Zertifizierungen parallel verfolgen. Statt Fortschritte manuell einzutragen, genügt es ein Modul in Google Sheets auf ✅ zu setzen — alles andere berechnet sich automatisch.

Das Dashboard läuft im Browser, ist auf allen Geräten erreichbar und braucht keine Datenbank, kein Framework-Setup und keinen bezahlten Service.

---

## 🖥️ Architektur

```
Browser (Mac / iPhone / Windows / egal)
         ↓
  POP-Keys Dashboard (localhost oder Railway)
         ↓
  Python FastAPI Backend
         ↓
  Google Sheets (öffentlich lesbar)
```

---

## 🎯 Features

- **Automatische Fortschrittsberechnung** — Module auf ✅ setzen, Prozent berechnet sich selbst per COUNTIF-Formel
- **Live Sync** — Dashboard lädt immer aktuelle Daten aus Google Sheets
- **Deadline Countdown** — Tage bis zur nächsten Prüfung live berechnet
- **Prioritätssystem** — Höchste Priorität wird als Banner hervorgehoben
- **Überfällige Kurse** werden automatisch markiert
- **Responsive** — funktioniert auf jedem Gerät im Browser
- **Komplett kostenlos** — Google Sheets + FastAPI + Railway Free Tier = 0€/Monat

---

## 🗂️ Projektstruktur

```
learning-os/
├── main.py              # FastAPI Backend — liest Google Sheets, liefert JSON
├── requirements.txt     # Python Abhängigkeiten
├── Procfile             # Railway Deployment Konfiguration
├── .env                 # 🔒 Nicht auf GitHub! (siehe .env.example)
├── .env.example         # Vorlage für Umgebungsvariablen
├── .gitignore
└── static/
    └── index.html       # POP-Keys Dashboard Frontend
```

---

## 🚀 Quickstart

### 1. Repository klonen

```bash
git clone https://github.com/DEIN-USERNAME/learning-os.git
cd learning-os
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. Google Sheet vorbereiten

Das Projekt nutzt Google Sheets als Datenbank. Du brauchst eine Google Tabelle mit zwei Tabs:

**Tab 1: `Kurse`** mit diesen Spalten:

| Kursname | Anbieter | Abgeschlossen | Gesamt | Fortschritt % | Deadline | Aktueller Kurs | Priorität | Status | Notizen |
|----------|----------|---------------|--------|---------------|----------|----------------|-----------|--------|---------|

**Tab 2: `Unterkurse`** mit diesen Spalten:

| Kursname | Modul | Status |
|----------|-------|--------|

> 💡 Eine fertige Vorlage mit Beispieldaten und automatischen COUNTIF-Formeln liegt als `learning_os_data.xlsx` bereit — einfach in Google Sheets importieren und als Google Tabelle speichern.

**Sheet öffentlich lesbar machen:**
1. Oben rechts `Teilen` klicken
2. `Allgemeiner Zugriff` → `Jeder im Internet mit diesem Link` → `Betrachter`
3. Sheet ID aus der URL kopieren: `docs.google.com/spreadsheets/d/`**`DIESE_ID`**`/edit`

### 4. Umgebungsvariablen konfigurieren

```bash
cp .env.example .env
```

`.env` öffnen und Sheet ID eintragen:

```env
SHEET_ID=deine_google_sheet_id_hier
```

### 5. Server starten

```bash
uvicorn main:app --reload
```

Dashboard öffnen: **http://localhost:8000** 🎉

---

## 📊 Google Sheets Logik

Der Fortschritt wird **nie manuell eingetragen** — er berechnet sich automatisch:

```
Tab "Unterkurse": Status eines Moduls → "✅ Abgeschlossen"
                              ↓
Tab "Kurse": COUNTIFS zählt abgeschlossene Module
                              ↓
Fortschritt % = Abgeschlossen / Gesamt × 100
```

**Mögliche Status-Werte in Unterkurse:**
- `🔜 Offen` — noch nicht begonnen
- `▶️ Aktiv` — aktuell in Bearbeitung
- `✅ Abgeschlossen` — fertig

---

## ☁️ Deployment auf Railway (kostenlos)

1. [railway.app](https://railway.app) → `New Project` → `Deploy from GitHub`
2. Repository auswählen
3. Unter `Variables` die Umgebungsvariable eintragen:
   ```
   SHEET_ID = deine_sheet_id
   ```
4. Railway erkennt den `Procfile` automatisch und startet den Server
5. Unter `Settings` → `Domains` eine öffentliche URL generieren

Das Dashboard ist dann unter `https://deine-app.railway.app` auf **allen Geräten** erreichbar.

---

## 🛠️ Tech Stack

| Komponente | Technologie | Kosten |
|------------|-------------|--------|
| Backend | Python 3.13 + FastAPI | ✅ Kostenlos |
| Datenbank | Google Sheets | ✅ Kostenlos |
| Frontend | Vanilla HTML/CSS/JS | ✅ Kostenlos |
| Hosting | Railway Free Tier | ✅ Kostenlos |
| **Gesamt** | | **0 €/Monat** |

---

## 🔒 Sicherheit

- Die `.env` Datei ist in `.gitignore` eingetragen und wird **nie** auf GitHub hochgeladen
- Das Google Sheet wird nur **lesend** abgefragt — keine Schreibrechte nötig
- Die Sheet ID ist kein Geheimnis, aber trotzdem besser in der `.env` aufbewahrt

---

## 📁 .env.example

```env
# Google Sheet ID
# Zu finden in der URL: docs.google.com/spreadsheets/d/HIER/edit
SHEET_ID=deine_sheet_id_hier
```

---

## 🤝 Contributing

Pull Requests sind willkommen! Für größere Änderungen bitte erst ein Issue öffnen.

---

## 📄 License

MIT — mach damit was du willst 🎹
