import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, WeatherRecord, add_weather_record, query_weather_record


class TestWeatherData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        # Create a new session for each test
        self.session = self.Session()

    def tearDown(self):
        # Close the session after each test
        self.session.close()

    def test_database_insertion(self):
        # Test that a record is correctly inserted into the database
        record = WeatherRecord(
            latitude=30.2672,
            longitude=-97.7431,
            month=8,
            day=16,
            year=2024,
            avg_temperature=87.38,
            min_temperature=73.42,
            max_temperature=103.21,
            avg_wind_speed=10.56,
            min_wind_speed=8.44,
            max_wind_speed=12.77,
            sum_precipitation=0.13,
            min_precipitation=0.0,
            max_precipitation=0.1
        )
        add_weather_record(record, self.session)

        # Query the database to verify insertion
        queried_record = self.session.query(WeatherRecord).filter_by(
            latitude=30.2672,
            longitude=-97.7431,
            month=8,
            day=16,
            year=2024
        ).first()

        self.assertIsNotNone(queried_record, "Record should be inserted into the database.")
        self.assertEqual(queried_record.avg_temperature, 87.38)
        self.assertEqual(queried_record.min_temperature, 73.42)

    def test_database_query(self):
        # Insert a record
        record = WeatherRecord(
            latitude=30.2672,
            longitude=-97.7431,
            month=8,
            day=16,
            year=2023,
            avg_temperature=85.20,
            min_temperature=70.15,
            max_temperature=100.35,
            avg_wind_speed=9.50,
            min_wind_speed=7.20,
            max_wind_speed=11.80,
            sum_precipitation=0.25,
            min_precipitation=0.0,
            max_precipitation=0.25
        )
        add_weather_record(record, self.session)

        # Query the database using the custom query method
        queried_record = query_weather_record(30.2672, -97.7431, 8, 16, 2023)

        self.assertIsNotNone(queried_record, "Record should be found in the database.")
        self.assertEqual(queried_record.avg_temperature, 85.20)
        self.assertEqual(queried_record.max_wind_speed, 11.80)

    def test_missing_data_handling(self):
        # Test querying for a record that doesn't exist
        queried_record = query_weather_record(30.2672, -97.7431, 8, 16, 2022)
        self.assertIsNone(queried_record, "Should return None when no record is found.")


if __name__ == "__main__":
    unittest.main()
