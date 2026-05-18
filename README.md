# 🚀 SaaS Deals Bot  
Automated bot that publishes SaaS deals on Bluesky every day.

The bot scrapes deals from **saasdeals.app**, formats them, and posts either a **single update** or a **full thread**, depending on how many deals are available.

---

## 🧠 What this bot does

- Scrapes deals from `https://saasdeals.app/deals`
- Formats each deal into clean, readable text
- Publishes:
  - **A single post** if there is 1 deal
  - **A full thread** if there are multiple deals
- If no deals are available, it posts:
  > No deals available today.

No legacy fallbacks, no test messages, no outdated content.

---

## 🏗 Project structure

