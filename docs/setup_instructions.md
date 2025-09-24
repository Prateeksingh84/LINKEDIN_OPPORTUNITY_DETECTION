# Setup Instructions

Guide to setting up the environment, dependencies, credentials, and running the pipeline (simulation & production).

---

## 🛠 Prerequisites

- Python 3.8 or higher  
- `pip` for package management  
- Internet access (for API usage / dataset download)  
- (Optional) Google Cloud project + service account for Google Sheets (if using Sheets)  

---

## Folder & File Structure

Make sure your project root looks like:

linkedin-agency-opportunity-detector/
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── data_loader.py
│ ├── qualifier.py
│ ├── file_store.py
│ ├── sheet_store.py
│ ├── notifier.py
│ └── ... other modules
│
├── tests/
│ ├── test_qualifier.py
│ ├── test_sheet_store.py
│ ├── test_simulated_pipeline.py
│ └── ...
│
├── outputs/
│ ├── sample_output.csv
│ └── sample_output.json
│
├── requirements.txt
├── .env
├── README.md
└── credentials/ (if using Google Sheets)