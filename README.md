# KPI-Anomaly-Watcher

Kurze 1-Satz-Beschreibung: <Was macht das Tool – warum nützlich für Smartclip?>

---

## Problem
Bei Smartclip werden KPI-Streams bisher manuell geprüft. Peaks oder Drops werden zu spät entdeckt → Budget-Verlust & weniger Reichweite.

## Lösung
Dieser Prototyp überwacht CTR & eCPM, erkennt Ausreißer mit Evidently-Tests und pusht Alerts in Discord – komplett auf Free-Tier-Infra.

## Live-Demo
[Streamlit-App](<deine-Streamlit-URL>) – interaktive Charts  
[Demo-Video (90 s)](<dein-Loom-Link>)

## Schnellstart

```bash
# klonen
git clone https://github.com/<dein-user>/kpi-anomaly-watcher.git
cd kpi-anomaly-watcher

# Abhängigkeiten
pip install -r requirements.txt   # oder: pip install pandas evidently discord_webhook streamlit

# Daten testen
python src/generate_demo_data.py

# Alert auslösen (Discord-Webhook vorher in .env eintragen)
python src/alert.py
