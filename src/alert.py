import os
import pandas as pd
from discord_webhook import DiscordWebhook

THRESHOLD = 3              # 3-Sigma-Grenze
CSV_PATH = "data/kpi.csv"  # richtiges Repo-Verzeichnis!
METRIC   = "ctr"           # oder 'ecpm'

df = pd.read_csv(CSV_PATH, parse_dates=["ts"])

roll   = df[METRIC].rolling(24, min_periods=24)
zscore = (df[METRIC] - roll.mean()) / roll.std()

latest = zscore.iloc[-1]
if latest > THRESHOLD:
    DiscordWebhook(
        url=os.getenv("DISCORD_URL"),
        content=f"⚠️ {METRIC.upper()}-Spike! Z={latest:.1f}"
    ).execute()
