from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import httpx
import csv
import io
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Learning OS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SHEET_ID = os.getenv("SHEET_ID", "")

EMOJI_MAP = {
    "Azure DP-900 Exam Prep":    "☁️",
    "Google Data Analytics":     "📊",
    "Generative AI Leader":      "🤖",
    "SAP Technology Consultant": "⚙️",
    "IBM AI Engineering":        "🧠",
    "Data Science Math Skills":  "🔢",
}

PRIORITÄT_MAP = {
    "Azure DP-900 Exam Prep":    "🎯 Hoch",
    "Google Data Analytics":     "📌 Mittel",
    "Generative AI Leader":      "📌 Mittel",
    "SAP Technology Consultant": "📌 Mittel",
    "IBM AI Engineering":        "📎 Niedrig",
    "Data Science Math Skills":  "📌 Mittel",
}

def sheet_csv_url(tab: str) -> str:
    tab_encoded = tab.replace(" ", "%20")
    return f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={tab_encoded}"

@app.get("/api/kurse")
async def get_kurse():
    if not SHEET_ID:
        raise HTTPException(status_code=500, detail="SHEET_ID nicht konfiguriert in .env")

    async with httpx.AsyncClient() as client:
        r_kurse  = await client.get(sheet_csv_url("Kurse"))
        r_module = await client.get(sheet_csv_url("Unterkurse"))

    if r_kurse.status_code != 200:
        raise HTTPException(status_code=502, detail="Google Sheet 'Kurse' nicht erreichbar")
    if r_module.status_code != 200:
        raise HTTPException(status_code=502, detail="Google Sheet 'Unterkurse' nicht erreichbar")

    module_by_kurs: dict[str, list] = {}
    for m in csv.DictReader(io.StringIO(r_module.text)):
        kurs = m.get("Kursname", "").strip()
        if kurs:
            module_by_kurs.setdefault(kurs, []).append({
                "modul":  m.get("Modul", "").strip(),
                "status": m.get("Status", "").strip(),
            })

    kurse = []
    for row in csv.DictReader(io.StringIO(r_kurse.text)):
        name = row.get("Kursname", "").strip()
        if not name:
            continue

        abgeschlossen = int(row.get("Abgeschlossen", 0) or 0)
        gesamt        = int(row.get("Gesamt", 1) or 1)

        try:
            fortschritt = round(float(row.get("Fortschritt %", "0").replace("%", "").strip()) / 100, 4)
        except ValueError:
            fortschritt = round(abgeschlossen / gesamt, 4) if gesamt else 0

        kurse.append({
            "name":          name,
            "emoji":         EMOJI_MAP.get(name, "📚"),
            "anbieter":      row.get("Anbieter", "").strip(),
            "abgeschlossen": abgeschlossen,
            "gesamt":        gesamt,
            "fortschritt":   fortschritt,
            "deadline":      row.get("Deadline", "").strip() or None,
            "aktuell":       row.get("Aktueller Kurs", "").strip(),
            "priorität":     PRIORITÄT_MAP.get(name, "📌 Mittel"),
            "status":        row.get("Status", "").strip(),
            "notizen":       row.get("Notizen", "").strip(),
            "module":        module_by_kurs.get(name, []),
        })

    order = {"🎯 Hoch": 0, "📌 Mittel": 1, "📎 Niedrig": 2}
    kurse.sort(key=lambda k: order.get(k["priorität"], 9))

    return {"kurse": kurse}

@app.get("/api/health")
async def health():
    return {"status": "ok", "sheet_configured": bool(SHEET_ID)}

app.mount("/", StaticFiles(directory="static", html=True), name="static")
