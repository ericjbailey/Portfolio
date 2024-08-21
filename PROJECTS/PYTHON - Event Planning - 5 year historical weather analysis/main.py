from WeatherDataCollector import WeatherDataCollector
from database import WeatherRecord, add_weather_record, query_weather_record

def main():
    # Initialize the weather data collector for Austin, TX on August 16
    austin_weather = WeatherDataCollector(30.2672, -97.7431, 8, 16, 2024)
    austin_weather.fetch_historical_data()
    austin_weather.calculate_statistics()

    # Create a WeatherRecord instance
    record = WeatherRecord(
        latitude=austin_weather.latitude,
        longitude=austin_weather.longitude,
        month=austin_weather.month,
        day=austin_weather.day,
        year=austin_weather.year,
        avg_temperature=austin_weather.avg_temperature,
        min_temperature=austin_weather.min_temperature,
        max_temperature=austin_weather.max_temperature,
        avg_wind_speed=austin_weather.avg_wind_speed,
        min_wind_speed=austin_weather.min_wind_speed,
        max_wind_speed=austin_weather.max_wind_speed,
        sum_precipitation=austin_weather.sum_precipitation,
        min_precipitation=austin_weather.min_precipitation,
        max_precipitation=austin_weather.max_precipitation
    )

    # Add the record to the database
    add_weather_record(record)

    # Query the record from the database
    queried_record = query_weather_record(
        latitude=30.2672,
        longitude=-97.7431,
        month=8,
        day=16,
        year=2024
    )

    # Display the queried record
    if queried_record:
        print(f"Queried Weather Data for {queried_record.month}/{queried_record.day}/{queried_record.year}")
        print(f"Location: {queried_record.latitude}N, {queried_record.longitude}E")
        print(f"Avg Temperature: {queried_record.avg_temperature}°F")
        print(f"Min Temperature: {queried_record.min_temperature}°F")
        print(f"Max Temperature: {queried_record.max_temperature}°F")
        print(f"Avg Wind Speed: {queried_record.avg_wind_speed} mph")
        print(f"Min Wind Speed: {queried_record.min_wind_speed} mph")
        print(f"Max Wind Speed: {queried_record.max_wind_speed} mph")
        print(f"Sum Precipitation: {queried_record.sum_precipitation} inches")
        print(f"Min Precipitation: {queried_record.min_precipitation} inches")
        print(f"Max Precipitation: {queried_record.max_precipitation} inches")

if __name__ == "__main__":
    main()
