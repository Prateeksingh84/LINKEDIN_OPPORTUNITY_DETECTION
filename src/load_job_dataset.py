import pandas as pd

def load_job_dataset():
    file_path = 'C:/Users/admin/.cache/kagglehub/datasets/ravindrasinghrana/job-description-dataset/versions/1/job_descriptions.csv'
    return pd.read_csv(file_path)

df = load_job_dataset()

print(df.head())

print(df.isnull().sum())

print(df.columns)
