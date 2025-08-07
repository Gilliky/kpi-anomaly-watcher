import os
import pandas as pd
from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftPreset
from discord_webhook import DiscordWebhook

# Demo-Daten laden
df = pd.read_csv("data/kpi.csv", parse_dates=["ts"])
ref, cur = df.iloc[:7000], df.iloc[7000:]

# Evidently-Tests ausführen
suite = TestSuite(tests=[DataDriftPreset()])
suite.run(ref, cur)

# Discord-Alert, falls etwas auffällig ist
if not suite.as_dict()["summary"]["all_passed"]:
    DiscordWebhook(
        url=os.getenv("DISCORD_URL"),  # Umgebungsvariable!
        content="⚠️ KPI-Anomalie entdeckt!"
    ).execute()
