seoul-py
========

Python API client library for `Seoul Open Data Plaza (서울 열린데이터 광장)`__.

.. __: http://data.seoul.go.kr


Examples
--------

Realtime subway position
````````````````````````

.. code-block:: python

   >>> from seoul import Client
   >>> seoul = Client()
   >>> trains = seoul.get_subway_realtime_position('6호선')
   >>> for train in trains:
   ...     print(f"{train.subway_name} {train.number}번 열차 @ {train.station_name}")
   ... 
   6호선 6265번 열차 @ 화랑대(서울여대입구)
   6호선 6271번 열차 @ 이태원
   6호선 6277번 열차 @ 불광


Realtime city air quality
`````````````````````````

.. code-block:: python

   >>> from seoul import Client
   >>> seoul = Client()
   >>> measurements = seoul.get_air_realtime_city()
   >>> for m in measurements:
   ...     print(f"AQI @ {m.region_name} {m.station_name}: {m.index_value}")
   ...
   ... AQI @ 도심권 중구: 55.0
   ... AQI @ 도심권 종로구: 55.0
   ... AQI @ 도심권 용산구: 53.0
   ... AQI @ 서북권 은평구: 51.0
   ... AQI @ 서북권 서대문구: 43.0


Supported APIs
--------------

- `서울시 지하철 실시간 열차 위치정보`__
- `서울시 권역별 실시간 대기환경 현황`__

.. __: http://data.seoul.go.kr/dataList/OA-12601/A/1/datasetView.do
.. __: http://data.seoul.go.kr/dataList/OA-2219/S/1/datasetView.do
