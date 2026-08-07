# heartopia-town-bot
自動每日發送「橡木與螢石位置」到 Discord 群組，Python 腳本（計算當天溜溜木及螢石位置陣列索引並用 requests.post() 發送到 Discord Webhook），然後利用 GitHub Actions 設定 Cron job，讓 GitHub 每天自動執行腳本發送訊息
