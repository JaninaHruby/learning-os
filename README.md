# 🎹 Learning OS — POP Keys Edition

> A personal learning dashboard that tracks parallel certification programs.
> Built with the help of AI (Claude by Anthropic). This is not my own code. I had a personal problem I wanted solved quickly, and since I remember from learning HTML how much work goes into building something like this, I used it as a learning project to see how fast and how well AI can put something like this together.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.132-009688?style=flat-square&logo=fastapi&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Backend-34A853?style=flat-square&logo=googlesheets&logoColor=white)

<img width="700" height="450" alt="Learning OS Dashboard" src="https://github.com/user-attachments/assets/1b0d568a-7bba-48cf-9ef4-eda02347e580" />

---

## What is this?

Learning OS is a simple web dashboard I built to track my progress across multiple certifications. Instead of manually updating percentages, I mark a module as ✅ in Google Sheets and the dashboard pulls the data automatically.

It uses Google Sheets as a backend, so there's no database to set up. It works, it does what I need, but let's be real: this is a learning project, not a scalable product. The architecture is simple on purpose.

---

## How it works

```
Browser
  ↓
Dashboard (localhost or Railway)
  ↓
Python FastAPI Backend
  ↓
Google Sheets (publicly readable)
```

The backend reads from a public Google Sheet and serves the data as JSON. The frontend is a single HTML file that displays it. That's it.

---

## What it does

- Calculates progress automatically from Google Sheets via COUNTIF
- Loads fresh data on every page visit
- Shows a countdown to the next exam deadline
- Highlights the highest priority course
- Flags overdue courses
- Works on any device in the browser
- Costs nothing (Google Sheets + FastAPI + Railway Free Tier)

---

