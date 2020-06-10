""":mod:`seoul.air` --- Air quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from dataclasses import dataclass
from datetime import datetime


REGION_STATIONS = {
    '도심권': [
        '중구',
        '종로구',
        '용산구',
    ],
    '서북권': [
        '은평구',
        '서대문구',
        '마포구',
    ],
    '동북권': [
        '광진구',
        '성동구',
        '중랑구',
        '동대문구',
        '성북구',
        '도봉구',
        '강북구',
        '노원구',
    ],
    '서남권': [
        '강서구',
        '구로구',
        '영등포구',
        '동작구',
        '관악구',
        '금천구',
        '양천구'
    ],
    '동남권': [
        '강남구',
        '서초구',
        '송파구',
        '강동구',
    ]
}


@dataclass(frozen=True)
class CityAirQuality:
    measured_at: datetime
    region_name: str
    station_name: str
    pm10: float
    pm25: float
    o3: float
    no2: float
    co: float
    so2: float
    index_name: str
    index_value: float
    index_pollutant: str
