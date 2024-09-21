# Sparkify Data Pipeline

## Purpose of the Database

Sparkify is a startup that provides a music streaming app. The analytics team at Sparkify wants to better understand user behavior by analyzing song play data. Specifically, they are interested in knowing what songs users are listening to and how they interact with the app. The purpose of this database is to provide a structured, optimized schema to help answer key questions about song play activity. This includes understanding which songs are played the most, who the top artists are, and when users are most active. The database supports fast and efficient querying to facilitate these analyses.

## How to Run the Python Scripts

1. **Set up the Database:**
Before running any ETL processes, the PostgreSQL database must be set up. You can create and set up the database using the following script:
```bash
python create_tables.py
```
This script will drop any existing tables and create the required schema for Sparkify’s analytics.

2. **Run the ETL Process: After setting up the database, run the ETL pipeline to process the song and log data:**

```bash
python etl.py
```
This script processes the raw data from the song and log files, then loads it into the database.

3. **Testing: You can verify the data was successfully loaded by running the Jupyter notebook:**

```bash
jupyter notebook test.ipynb
```

## Explanation of the Files in the Repository
`create_tables.py`: This script contains the logic to create and reset the database schema (fact and dimension tables). It ensures the database is prepared for the ETL pipeline by creating fresh tables.

`etl.py`: This script processes the raw song and log files, extracts the necessary information, and loads the data into the appropriate database tables. It reads from two datasets:
- Song Dataset: Contains metadata about songs and artists.
- Log Dataset: Contains user activity logs from the app, simulating what users have played.

`sql_queries.py`: Contains all the SQL queries used for table creation, data insertion, and query execution. This file is imported by `create_tables.py` and `etl.py`.

`test.ipynb`: A Jupyter notebook used to run tests to verify that the ETL pipeline is correctly processing and loading the data into the tables.

## Database Schema Design
The database schema follows a star schema design. This design is optimal for running analytical queries since it reduces the complexity of joins and improves query performance.

- Fact Table:
    - `songplays`: This table records every user interaction with the app (i.e., song plays). It includes references to the song and artist played, as well as the user, time, and session information.
- Dimension Tables:

    - `users`: Stores information about users, including their first and last names, gender, and subscription level.
    - `songs`: Contains details about each song, such as title, artist, and duration.
    - `artists`: Stores information about artists, including name and location.
    - `time`: Contains timestamps broken down into specific units (hour, day, week, etc.) to facilitate time-based analysis.

## Justification for Schema Design
- Star schema was chosen for its simplicity and performance in querying large datasets for analytical purposes. The fact table (`songplays`) centralizes user interaction data, while the dimension tables provide context about users, songs, artists, and time.
- This schema allows for fast, efficient queries that join the fact table with the dimension tables to perform analyses such as identifying the most popular songs and artists, understanding user listening patterns, and tracking usage over time.

## ETL Pipeline
- The ETL pipeline reads data from JSON files, transforms it into the appropriate format, and loads it into the database.
- Song Data is loaded into the `songs` and `artists` tables.
- Log Data is filtered to include only song play actions (`NextSong`), and data is loaded into the `time`, `users`, and `songplays` tables.
- The pipeline ensures that each step of the process is done in the correct sequence, handling missing or null data appropriately.

## Function Docstrings
Each function in the Python scripts includes a docstring to describe its purpose. Below is one example:

```python
def create_database():
    """
    - Creates and connects to the Sparkify database.
    - Returns the connection and cursor to Sparkifydb.
    """
```