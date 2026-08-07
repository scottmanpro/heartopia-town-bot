# heartopia-town-bot
自動每日發送「橡木與螢石位置」到 Discord 群組，Python 腳本（計算當天溜溜木及螢石位置陣列索引並用 requests.post() 發送到 Discord Webhook），然後利用 GitHub Actions 設定 Cron job，讓 GitHub 每天自動執行腳本發送訊息

第一步：取得 Discord Webhook URL
        1. 開啟 Discord，進入目標頻道的「頻道設定」（齒輪圖示）。
        2. 點擊 整合 $\rightarrow$ Webhooks $\rightarrow$ 
        3. 建立 Webhook。複製 Webhook URL 備用。
第二步：建立 GitHub 專案與設定 Secrets
        1. 前往 GitHub 建立一個全新的 Public 專案（Public 專案的 GitHub Actions 完全免費）。
        2. 進入專案的 Settings $\rightarrow$ Secrets and variables $\rightarrow$ Actions。
        3. 點擊 New repository secret：
          Name: DISCORD_WEBHOOK
          Secret: 貼上第一步複製的 Discord Webhook URL。
第三步：新增 Python 腳本 (bot.py)

第四步：設定自動執行流程 (main.yml)
        在專案中建立資料夾與檔案：.github/workflows/main.yml

完成設定後，可以至專案的 Actions 頁籤點擊 Run workflow 手動測試，成功後每天早上 10 點就會自動發送訊息到頻道。

提示： GitHub Cron 延遲說明： GitHub 伺服器在排程尖峰時段，Cron 執行時間可能會有些許延遲（通常在 0~15 分鐘之間，例如 10:05~10:15 才收到訊息），這是正常的現象。
