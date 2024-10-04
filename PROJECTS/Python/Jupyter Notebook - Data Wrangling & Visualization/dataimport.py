import zipfile
import os
import pandas as pd

zip_file_path = r'C:\Users\15126\Desktop\vgsales.csv.zip'
extract_to_path = r'C:\Users\15126\Desktop\D497-1'
csv_file_path = os.path.join(extract_to_path, 'vgsales.csv')

# Unzip file & extract
if os.path.exists(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
    print(f'Extracted files to {extract_to_path}')

# Load csv file into DataFrame and preview
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    print(df.head())