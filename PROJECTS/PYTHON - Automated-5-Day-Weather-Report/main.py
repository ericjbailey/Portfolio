import requests
from datetime import datetime
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
import schedule
import time


api_key = 'lJ2OLWd4baP7Kid4JEYNtSKKgevZeEdb'
#email_address = 'sophiapythoncourse@gmail.com'
#email_password = 'intentionally_left_blank'
#recipient_email = 'sophiapythoncourse@gmail.com'

def get_5_day_forecast(location_key):
        base_url = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/34420_PC'

        # Set the parameters for the request (units, language, etc.)
        params = {
            'apikey': api_key,
            'metric': False,  # Set to True for Celcius. Change lines 43&44 if changing this line.
            'details': True,  # Request additional details in the response
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'DailyForecasts' in data:
            for day in data['DailyForecasts']:
                date_str = day['Date']

                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")

                # Format the date in a more readable way
                formatted_date = date.strftime("%A, %B %d, %Y")

                min_temp = day['Temperature']['Minimum']['Value']
                max_temp = day['Temperature']['Maximum']['Value']
                day_forecast = day['Day']['LongPhrase']
                night_forecast = day['Night']['LongPhrase']

                print(f"Date: {formatted_date}")
                print(f"Minimum Temperature: {min_temp}°F")
                print(f"Maximum Temperature: {max_temp}°F")
                print(f"Day Forecast: {day_forecast}")
                print(f"Night Forecast: {night_forecast}")
                print("\n")
        else:
            print("Forecast data not found.")

if __name__ == "__main__":
    location_key = '34220_PC'
    get_5_day_forecast(location_key)

def save_to_file(filename, content):
  with open(filename, 'a') as file:
      file.write(content)
      file.write("\n\n\n")  # Add a separator between daily reports

      # Append the daily forecast to the file
      save_to_file("weather_forecast.txt", forecast_message)
      send_email("Daily Weather Forecast", forecast_message)

#def send_email(subject, message):
#  msg = MIMEMultipart()
#  msg['From'] = email_address
#  msg['To'] = recipient_email
#  msg['Subject'] = subject
#  msg.attach(MIMEText(message, 'plain'))

#  server = smtplib.SMTP('smtp.gmail.com', 587)
#  server.starttls()
#  server.login(email_address, email_password)
#  server.sendmail(email_address, recipient_email, msg.as_string())
#  server.quit()

def get_weather_forecast():
  location_key = '34220_PC'  
  forecast_message = get_5_day_forecast(location_key)


schedule.every(1).days.do(get_weather_forecast)

while True:
  schedule.run_pending()
  time.sleep(1)

#The original idea was to have the report emailed every 5 days
#but Google has discontinued 3rd party apps outside of their 
#developer and business profiles. The intent now is to save the
#5 day forecast daily, so that the data can be used to measure
#the reliability of the forecast past 1, 2, 3, or 4 days.
