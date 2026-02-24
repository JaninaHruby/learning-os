# 🎹 Learning OS — POP Keys Edition

> A personal learning dashboard that tracks parallel certification programs, calculates progress automatically, and works on any device.
> Built with the help of AI (Claude by Anthropic) as a learning project.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.132-009688?style=flat-square&logo=fastapi&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Backend-34A853?style=flat-square&logo=googlesheets&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ What is Learning OS?

Learning OS is a self-hosted web dashboard for people juggling multiple certifications at once. Instead of manually updating progress percentages, you simply mark a module as ✅ in Google Sheets — everything else calculates itself automatically.

The dashboard runs in any browser, is accessible on all devices, and requires no database setup, no paid services, and no complex configuration.

---

## 🖥️ Architecture

```
Browser (Mac / iPhone / Windows / any device)
         ↓
  POP-Keys Dashboard (localhost or Railway)
         ↓
  Python FastAPI Backend
         ↓
  Google Sheets (publicly readable)
```

---

## 🎯 Features

- **Automatic progress calculation** — mark a module ✅, the percentage updates itself via COUNTIF formula
- **Live sync** — dashboard always loads fresh data from Google Sheets
- **Deadline countdown** — days until next exam calculated live
- **Priority system** — highest priority course highlighted as a banner
- **Overdue detection** — overdue courses are automatically flagged
- **Responsive** — works on any device in the browser
- **Completely free** — Google Sheets + FastAPI + Railway Free Tier = €0/month

---

## 🗂️ Project Structure

```
learning-os/
├── main.py              # FastAPI backend — reads Google Sheets, serves JSON
├── requirements.txt     # Python dependencies
├── Procfile             # Railway deployment configuration
├── .env                 # 🔒 Never commit this! (see .env.example)
├── .env.example         # Template for environment variables
├── .gitignore
└── static/
    └── index.html       # POP-Keys dashboard frontend
```

---

## 🚀 Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/JaninaHruby/learning-os.git
cd learning-os
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare your Google Sheet

This project uses Google Sheets as its database. You need a Google Spreadsheet with two tabs:

**Tab 1: `Kurse`** with these columns:

| Kursname | Anbieter | Abgeschlossen | Gesamt | Fortschritt % | Deadline | Aktueller Kurs | Priorität | Status | Notizen |
|----------|----------|---------------|--------|---------------|----------|----------------|-----------|--------|---------|

**Tab 2: `Unterkurse`** with these columns:

| Kursname | Modul | Status |
|----------|-------|--------|

> 💡 A ready-made template with sample data and automatic COUNTIF formulas is available as `learning_os_data.xlsx` — simply import it into Google Sheets and save as a Google Spreadsheet.

**Make the sheet publicly readable:**
1. Click `Share` in the top right
2. Under `General access` → `Anyone with the link` → `Viewer`
3. Copy the Sheet ID from the URL: `docs.google.com/spreadsheets/d/`**`THIS_ID`**`/edit`

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and enter your Sheet ID:

```env
SHEET_ID=your_google_sheet_id_here
```

### 5. Start the server

```bash
uvicorn main:app --reload
```

Open the dashboard: **http://localhost:8000** 🎉

---

## 📊 Google Sheets Logic

Progress is **never entered manually** — it calculates automatically:

```
Tab "Unterkurse": module status → "✅ Abgeschlossen"
                              ↓
Tab "Kurse": COUNTIFS counts completed modules
                              ↓
Progress % = Completed / Total × 100
```

**Possible status values in Unterkurse:**
- `🔜 Offen` — not yet started
- `▶️ Aktiv` — currently in progress
- `✅ Abgeschlossen` — completed

---

## ☁️ Deploy to Railway (free)

1. Go to [railway.app](https://railway.app) → `New Project` → `Deploy from GitHub`
2. Select your repository
3. Under `Variables` add the environment variable:
   ```
   SHEET_ID = your_sheet_id
   ```
4. Railway automatically detects the `Procfile` and starts the server
5. Under `Settings` → `Domains` generate a public URL

Your dashboard will then be available at `https://your-app.railway.app` on **any device**.

---

## 🛠️ Tech Stack

| Component | Technology | Cost |
|-----------|------------|------|
| Backend | Python 3.13 + FastAPI | ✅ Free |
| Database | Google Sheets | ✅ Free |
| Frontend | Vanilla HTML/CSS/JS | ✅ Free |
| Hosting | Railway Free Tier | ✅ Free |
| **Total** | | **€0/month** |

---

## 🔒 Security

- The `.env` file is listed in `.gitignore` and is **never** uploaded to GitHub
- Google Sheets is accessed **read-only** — no write permissions required
- The Sheet ID is not a secret, but better kept in `.env` as best practice

---

## 📁 .env.example

```env
# Google Sheet ID
# Found in the URL: docs.google.com/spreadsheets/d/HERE/edit
SHEET_ID=your_sheet_id_here
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT — do whatever you want with it 🎹
