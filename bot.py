import os
import requests
from datetime import datetime, date

# 1. 50天循環資料庫 (Day 1 ~ Day 50)
OAK_DATA = ["3","7","7","1","5","9","11","6","2","2","3","12","11","遺跡","8","5","4","11","遺跡","8","8","2","2","2","1","1","4","8","4","1","遺跡","8","8","6","2","7","12","8","6","11","2","9","3","6","2","11","遺跡","遺跡","7","9"]
FLUORITE_DATA = ["10","3","6","9","4","10","松林","7","6","11","2","12","4","12","松林","2","1","10","5","10","4","7","3","松林","3","5","12","2","8","4","8","6","8","12","10","2","遺跡","5","11","11","2","12","4","11","7","9","4","4","11","5"]

# 2. 計算當天對應索引 (以 2026-08-15 為第 50 天/索引 49)
BASE_DATE = date(2026, 8, 15)
today = date.today()
diff_days = (today - BASE_DATE).days
index = (diff_days + 49) % 50

today_oak = OAK_DATA[index]
today_fluorite = FLUORITE_DATA[index]

# 3. 組裝 Discord 美化卡片 (Embed)
webhook_url = os.environ.get("DISCORD_WEBHOOK")
data = {
    "username": "心動小鎮採集小助手",
    "avatar_url": "https://i.imgur.com/P480et0.jpeg",
    "embeds": [{
        "title": f"📢 今日採集點預報 ({today.strftime('%Y-%m-%d')})",
        "color": 3447003,
        "fields": [
            {"name": "🌳 溜溜木位置", "  value": f"**{today_oak}** 號區域", "inline": True},
            {"name": "💎 螢石位置", "  value": f"**{today_fluorite}** 號區域", "inline": True}
        ],
        "footer": {"text": "心動小鎮 • 50天循環規律自動推播 • 由諾諾贊助"}
    }]
}

# 4. 發送至 Discord
if webhook_url:
    requests.post(webhook_url, json=data)
