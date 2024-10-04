import subprocess
import zipfile
import os
import pandas as pd

# Download dataset using Kaggle API
subprocess.run(["kaggle", "datasets", "download", "-d", "nikdavis/steam-store-games", "--file", "steam.csv"])

# Unzip file
zip_file = 'steam.csv.zip'
if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

# Load CSV into DataFrame
csv_file = 'steam.csv'
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    print(df.head())  

# Remove zip file
if os.path.exists(zip_file):
    os.remove(zip_file)


