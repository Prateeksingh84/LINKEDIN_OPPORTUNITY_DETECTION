import os
import pandas as pd
import kagglehub

def load_job_dataset():
    """
    Download and load the Kaggle job description dataset.
    Dynamically finds the first CSV file in the dataset folder.
    """
    path = kagglehub.dataset_download("ravindrasinghrana/job-description-dataset")

    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError(f"No CSV file found in {path}")

    file_path = os.path.join(path, files[0])
    print(f"📂 Using dataset file: {file_path}")

    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_job_dataset()
    print(df.head())
    print(f"Dataset contains {len(df)} rows.")
