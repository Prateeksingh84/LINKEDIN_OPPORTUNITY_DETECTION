# LinkedIn Agency Opportunity Detection

A Python-based system to detect agency / marketing / branding leads from LinkedIn posts (or simulated datasets). It qualifies, scores, and exports opportunities in CSV and JSON formats.

---

## 🚀 Features

- Keyword-based detection of posts mentioning "looking for agency", "need marketing help", etc.  
- Scoring based on engagement metrics (likes/comments/shares) + firmographic signals  
- Qualification into "qualified" vs "unqualified" leads  
- Export to `sample_output.csv` and `sample_output.json`  
- Notification stubs (Slack / Email) for high-priority opportunities  
- Fallback simulation mode (using Kaggle dataset, dummy scraper) for testing

---

## 📁 Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data_loader.py
│   ├── qualifier.py
│   ├── file_store.py
│   ├── sheet_store.py
│   └── notifier.py
├── tests/
│   ├── test_qualifier.py
│   ├── test_sheet_store.py
│   └── test_simulated_pipeline.py
├── outputs/
│   ├── sample_output.csv
│   └── sample_output.json
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠 Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/linkedin-opportunity-detection.git
   cd linkedin-opportunity-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create outputs folder**
   ```bash
   mkdir outputs
   ```

4. **Set environment variables (in .env file)**
   ```env
   LINKEDIN_ACCESS_TOKEN=   # optional, leave blank for simulation
   GOOGLE_API_KEY=           # optional, for fallback scraper
   SLACK_WEBHOOK_URL=        # optional
   SMTP_HOST=                 # optional
   SMTP_PORT=
   SMTP_USER=
   SMTP_PASS=
   NOTIFICATION_EMAIL=
   ```

5. **Ensure src/__init__.py exists** so Python treats src as a module.

---

## ▶ Running the Pipeline

**Simulation mode** (using Kaggle dataset / dummy posts):
```bash
python src/main.py
```
*If LINKEDIN_ACCESS_TOKEN is not set, the script runs simulated mode.*

**LinkedIn mode** (if you have valid access token & scraper):
Set LINKEDIN_ACCESS_TOKEN (and optionally GOOGLE_API_KEY fallback) then run:
```bash
python src/main.py
```

---

## 📦 Outputs

- `outputs/sample_output.csv` — all opportunities (one row per post)
- `outputs/sample_output.json` — JSON representation of the same data

You can open the CSV in Excel / Sheets / pandas; JSON in code or JSON viewers.

---

## 🧪 Testing

Use pytest to run the test suite:
```bash
pytest -v
```

You can disable output capturing to see print statements by running:
```bash
pytest -s
```

---

## 🔧 Keywords & Scoring Logic (Summary)

- **Keywords**: "looking for agency", "need marketing help", "RFP", etc.
- **Engagement**: sum of likes/comments/shares
- **Company signals**: employee count, revenue
- **Score thresholds**:
  - >= 70 → high priority
  - >= 40 → qualified
  - otherwise → unqualified

You can fine-tune the weights and thresholds in `qualifier.py`.

---

## 🔁 Alternative / Fallback Data Sources

- Kaggle datasets (job descriptions) used for simulation
- Dummy scrapers / fallback logic for LinkedIn posts
- External scraping or APIs (if you integrate later)

---

## 🛡 License & Contribution

This project is licensed under MIT.

Contributions welcome — fork, commit, and submit pull requests.
