# Weather Data Collector and Analyzer

## Overview

This project collects historical weather data for a specified location and date, calculates statistics over a five-year period, and stores the results in a SQLite database using SQLAlchemy. The program also allows querying the stored data for later analysis.

## Features

- **Weather Data Collection**: Fetches weather data from the Open-Meteo API.
- **Data Storage**: Stores the collected data in a SQLite database.
- **Querying**: Allows querying the database to retrieve stored weather records.
- **Unit Tests**: Includes tests to verify the correct functionality of the data collection and storage process.

## Prerequisites

Before running the program, ensure that you have Python installed on your machine. You will also need to install the required packages listed in `requirements.txt`.

## Installation

1. **Clone the repository** :

   ```bash
   git clone https://gitlab.com/wgu-gitlab-environment/student-repos/ebai147/d493-scripting-and-programming-applications.git
   cd d493-scripting-and-programming-applications
   ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    
    ```bash
    pip install -r requirements.txt
   ```

## Usage

### 1. Running the Main Program

The main program (`main.py`) collects weather data for Austin, TX on August 16, stores the data in a SQLite database, and retrieves it for display.

```bash
python main.py
```

#### Inputs

- **Latitude**: Latitude of the location (e.g., `30.2672` for Austin, TX).
- **Longitude**: Longitude of the location (e.g., `-97.7431` for Austin, TX).
- **Date**: The date for which weather data is collected (e.g., `August 16, 2024`).

#### Outputs

- The program prints the fetched and calculated weather data to the console.
- The weather data is stored in a SQLite database (`weather_data.db`).
- The queried data is displayed in the console in a formatted manner.

### 2. Running Unit Tests

The unit tests (`test.py`) verify that records are correctly inserted and queried from the database.

```bash
python test.py
```

#### Test Scenarios

- **Database Insertion**: Verifies that a weather record is correctly inserted into the database.
- **Database Query**: Checks that the correct weather record is retrieved from the database.
- **Missing Data Handling**: Ensures that the program handles cases where no data is found.

### 3. Querying the Database

You can query the SQLite database manually or by modifying the `main.py` script to fetch data for different locations or dates.

#### Example Query (within `main.py`)

```python
# Query the record from the database
queried_record = query_weather_record(
    latitude=30.2672,
    longitude=-97.7431,
    month=8,
    day=16,
    year=2024
)
```

This will output the queried weather data in the console.

## Files

- **`main.py`**: The main script for collecting, storing, and displaying weather data.
- **`WeatherDataCollector.py`**: Contains the `WeatherDataCollector` class responsible for data collection and processing.
- **`openmeteo.py`**: Handles API requests and processing for weather data.
- **`database.py`**: Manages the SQLite database using SQLAlchemy, including record insertion and querying.
- **`test.py`**: Contains unit tests for verifying the functionality of the program.
- **`requirements.txt`**: Lists the Python packages required to run the program.
- **`README.md`**: Provides an overview and instructions for using the program.
