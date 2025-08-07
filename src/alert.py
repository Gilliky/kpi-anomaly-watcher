import os, pandas as pd
from discord_webhook import DiscordWebhook

THRESHOLD = 3        # 3-Sigma-Regel

df = pd.read_csv("data.csv", parse_dates=["ts"])          # Colab-Pfad
metric = "ctr"                                           # oder "ecpm"

# rolling mean + std (24 h)
roll = df[metric].rolling(window=24, min_periods=24)
z_score = (df[metric] - roll.mean()) / roll.std()

# letzte Stunde prüfen
latest = z_score.iloc[-1]
if latest > THRESHOLD:
    DiscordWebhook(
        url=os.getenv("DISCORD_URL"),
        content=f"⚠️ {metric.upper()}-Spike! Z={latest:.1f}"
    ).execute()
