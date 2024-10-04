# Movie Dataset Analysis

This project performs an exploratory data analysis (EDA) on the TMDb 5000 movie and credits datasets. The goal is to understand the data, clean it, and extract useful insights about movie budgets, revenues, and actors.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Analysis Steps](#analysis-steps)
5. [Results](#results)
6. [License](#license)

## Installation

To run this notebook, you'll need to install the necessary Python packages. The script includes code to install required packages and generate a `requirements.txt` file. To ensure that all dependencies are installed, run the following code:

```python
import subprocess
import sys

# List of required packages
required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'scikit-learn']

# Install packages
for package in required_packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Create a requirements.txt file with the current environment's packages
with open('requirements.txt', 'w') as f:
    subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f)
```

Alternatively, you can install the packages manually using the following command:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage

1. **Data Preparation**: The notebook first installs all required dependencies and then imports necessary libraries for data manipulation, visualization, and analysis.
2. **Loading Data**: The datasets for movies and credits are loaded from CSV files located in the `data` directory.
3. **Exploratory Data Analysis (EDA)**: Various steps are taken to explore and clean the data, including merging datasets, visualizing movie budgets, and analyzing actor performance metrics.
4. **Results Visualization**: Several visualizations, including histograms, scatter plots, and bar plots, are created to highlight key insights from the data.

## Project Structure

- **Data Files**:
  - `tmdb_5000_credits.csv`: Contains credit information for movies.
  - `tmdb_5000_movies.csv`: Contains detailed movie information.
  
- **Notebook Sections**:
  - **Installation and Imports**: Handles package installation and imports required libraries.
  - **Data Loading**: Loads the data from CSV files.
  - **Data Exploration**: Explores the datasets by displaying the first few rows, summaries, and checking for missing values.
  - **Merging Datasets**: Merges the movies and credits datasets based on a common key.
  - **Visualizations**: Generates visualizations such as histograms for budget distributions and scatter plots for budget vs. revenue analysis.
  - **Actor and Genre Analysis**: Analyzes genres and actor performance metrics.

## Analysis Steps

1. **Importing Libraries**: All necessary libraries are imported, including `pandas`, `numpy`, `matplotlib`, `seaborn`, `json`, `ast`, and `scikit-learn`.
2. **Loading Data**: The TMDb 5000 movie and credits datasets are loaded from CSV files.
3. **Exploring Data**: The datasets are explored to understand their structure, data types, and missing values.
4. **Merging Data**: The movie and credits datasets are merged on `movie_id` and `id` columns.
5. **Visualization of Budgets**: A histogram is created to visualize the distribution of movie budgets.
6. **Budget vs Revenue Scatter Plot**: A scatter plot is generated to show the relationship between movie budgets and revenues, with a regression line and R² value added.
7. **Genre Analysis**: Genres are extracted and average ratings by genre are calculated and visualized.
8. **Cleaning Cast Data**: The cast data is cleaned, relevant information is extracted, and the data is transformed for further analysis.
9. **Actor Analysis**: Actors are analyzed based on their budget-to-revenue ratio, and top performers are identified.
10. **Top Movies Analysis**: The top movies are analyzed based on their revenue-to-budget ratio, and the most profitable movies are identified and visualized.

## Results

The analysis provided insights into various aspects of the movie industry, including:

- The distribution of movie budgets.
- The relationship between movie budgets and revenues.
- The most profitable genres and actors.
- The top movies by revenue-to-budget ratio.
- The most profitable movies based on absolute profit.