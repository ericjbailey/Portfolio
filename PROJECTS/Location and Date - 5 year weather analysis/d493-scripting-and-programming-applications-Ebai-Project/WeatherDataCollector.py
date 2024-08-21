import numpy as np
from openmeteo import fetch_weather_data, process_daily_data

class WeatherDataCollector:
    def __init__(self, latitude: float, longitude: float, month: int, day: int, year: int):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

        self.temperatures_max = []
        self.temperatures_min = []
        self.temperatures_mean = []
        self.precipitations_sum = []
        self.wind_speeds_max = []

        self.avg_temperature = None
        self.min_temperature = None
        self.max_temperature = None
        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None
        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None

    def fetch_weather_data_for_year(self, year: int):
        """
        Fetch weather data for a specific year and store the results.
        """
        start_date = f"{year}-{self.month:02d}-{self.day:02d}"
        end_date = start_date

        response = fetch_weather_data(self.latitude, self.longitude, start_date, end_date)
        daily_df = process_daily_data(response)

        # Debug: Print the entire dataframe to check for issues
        print(daily_df)

        # Check for NaN values and handle them
        if daily_df.isnull().values.any():
            print(f"Warning: Missing data detected for {start_date}")
            return

        self.temperatures_max.append(daily_df['temperature_2m_max'][0])
        self.temperatures_min.append(daily_df['temperature_2m_min'][0])
        self.temperatures_mean.append(daily_df['temperature_2m_mean'][0])
        self.precipitations_sum.append(daily_df['precipitation_sum'][0])
        self.wind_speeds_max.append(daily_df['wind_speed_10m_max'][0])

    def fetch_historical_data(self):
        """
        Fetch weather data for the selected day across the current year and the four preceding years.
        """
        for year in range(self.year, self.year - 5, -1):
            self.fetch_weather_data_for_year(year)

    def calculate_statistics(self):
        """
        Calculate the five-year averages, minimums, and maximums for each weather variable,
        converting NumPy types to Python floats and rounding the results to 2 decimal places.
        """
        if self.temperatures_mean:
            self.avg_temperature = round(float(np.mean(self.temperatures_mean)), 2)
            self.min_temperature = round(float(np.min(self.temperatures_min)), 2)
            self.max_temperature = round(float(np.max(self.temperatures_max)), 2)

        if self.wind_speeds_max:
            self.avg_wind_speed = round(float(np.mean(self.wind_speeds_max)), 2)
            self.min_wind_speed = round(float(np.min(self.wind_speeds_max)), 2)
            self.max_wind_speed = round(float(np.max(self.wind_speeds_max)), 2)

        if self.precipitations_sum:
            self.sum_precipitation = round(float(np.sum(self.precipitations_sum)), 2)
            self.min_precipitation = round(float(np.min(self.precipitations_sum)), 2)
            self.max_precipitation = round(float(np.max(self.precipitations_sum)), 2)

# Example usage for Austin, TX on August 16
austin_weather = WeatherDataCollector(30.2672, -97.7431, 8, 16, 2024)
austin_weather.fetch_historical_data()
austin_weather.calculate_statistics()

print(f"Five-Year Avg Temperature: {austin_weather.avg_temperature}")
print(f"Five-Year Min Temperature: {austin_weather.min_temperature}")
print(f"Five-Year Max Temperature: {austin_weather.max_temperature}")
print(f"Five-Year Avg Wind Speed: {austin_weather.avg_wind_speed}")
print(f"Five-Year Min Wind Speed: {austin_weather.min_wind_speed}")
print(f"Five-Year Max Wind Speed: {austin_weather.max_wind_speed}")
print(f"Five-Year Sum Precipitation: {austin_weather.sum_precipitation}")
print(f"Five-Year Min Precipitation: {austin_weather.min_precipitation}")
print(f"Five-Year Max Precipitation: {austin_weather.max_precipitation}")
