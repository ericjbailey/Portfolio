from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class WeatherRecord(Base):
    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    avg_temperature = Column(Float)
    min_temperature = Column(Float)
    max_temperature = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    sum_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

    def __init__(self, latitude, longitude, month, day, year,
                 avg_temperature, min_temperature, max_temperature,
                 avg_wind_speed, min_wind_speed, max_wind_speed,
                 sum_precipitation, min_precipitation, max_precipitation):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temperature = avg_temperature
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.avg_wind_speed = avg_wind_speed
        self.min_wind_speed = min_wind_speed
        self.max_wind_speed = max_wind_speed
        self.sum_precipitation = sum_precipitation
        self.min_precipitation = min_precipitation
        self.max_precipitation = max_precipitation

# SQLAlchemy setup
engine = create_engine('sqlite:///weather_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_weather_record(record, session):
    session.add(record)
    session.commit()

def query_weather_record(latitude, longitude, month, day, year):
    record = session.query(WeatherRecord).filter_by(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        year=year
    ).first()

    if record:
        return record
    else:
        print(f"No data found for {latitude}, {longitude} on {month}/{day}/{year}")
        return None
