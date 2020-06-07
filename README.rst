seoul-py
========

Python API client library for `Seoul Open Data Plaza (서울 열린데이터 광장)`__.

.. __: http://data.seoul.go.kr


Example
-------

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


Supported APIs
--------------

- `서울시 지하철 실시간 열차 위치정보`__

.. __: http://data.seoul.go.kr/dataList/OA-12601/A/1/datasetView.do
