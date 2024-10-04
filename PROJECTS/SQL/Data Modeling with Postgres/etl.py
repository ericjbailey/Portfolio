import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Process song file and insert song and artist records into database.
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = (df.song_id.values[0], df.title.values[0], df.artist_id.values[0], int(df.year.values[0]), float(df.duration.values[0]))
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = (df.artist_id.values[0], df.artist_name.values[0], df.artist_location.values[0], 
                   float(df.artist_latitude.values[0]) if pd.notnull(df.artist_latitude.values[0]) else None, 
                   float(df.artist_longitude.values[0]) if pd.notnull(df.artist_longitude.values[0]) else None)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Process log file and insert time, user, and songplay records into database.
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = [(time, time.hour, time.day, time.week, time.month, time.year, time.weekday()) for time in t]
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']].drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Process all files in given directory and apply function to each file.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print(f'{num_files} files found in {filepath}')

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print(f'{i}/{num_files} files processed.')


def main():
    """
    - Establishes connection to database.
    - Processes all song data files and log data files.
    - Closes database connection.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
