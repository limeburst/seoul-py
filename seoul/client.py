""":mod:`seoul.client` --- Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from datetime import datetime
from typing import List

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .subway.train import Direction, Train


SAMPLE_API_KEY = 'sample'

BASE_URL = 'http://swopenapi.seoul.go.kr'
SUBWAY_REALTIME_POSITION_URL = '/api/subway/{api_key}/{format}/realtimePosition/{start_index}/{end_index}/{subway_name}'


class Client:
    def __init__(self, api_key: str = SAMPLE_API_KEY):
        self.api_key = api_key

    def get_subway_realtime_position(self, subway_name: str,
                                     start_index: int = 0, end_index: int = 1000) -> List[Train]:
        """Get realtime train position for subway line.
        
        Specification: http://data.seoul.go.kr/dataList/OA-12601/A/1/datasetView.do
        
        """
        if self.api_key == SAMPLE_API_KEY:
            start_index = 0
            end_index = 5

        s = Session()
        retries = Retry(status_forcelist=[503])
        s.mount(BASE_URL, HTTPAdapter(max_retries=retries))
        url = BASE_URL + SUBWAY_REALTIME_POSITION_URL.format(
            api_key=self.api_key,
            format='json',
            subway_name=subway_name,
            start_index=start_index,
            end_index=end_index,
        )
        r = s.get(url)

        d = r.json()
        if 'realtimePositionList' not in d:
            """
            code: 'INFO-200'
            message: '해당하는 데이터가 없습니다.'

            Returned when the subway line has ended operations for the day.
            """
            if d['status'] == 500 and d['code'] == 'INFO-200':
                return []

            raise Exception(f"{d['code']}: {d['message']}")
        else:
            trains = []
            for t in d['realtimePositionList']:
                data = {
                    'subway_id': t['subwayId'],
                    'subway_name': t['subwayNm'],
                    'station_id': t['statnId'],
                    'station_name': t['statnNm'],
                    'terminal_station_id': t['statnTid'],
                    'terminal_station_name': t['statnTnm'],
                    'number': t['trainNo'],
                    'status': t['trainSttus'],
                    'direction': Direction(int(t['updnLine'])),
                    'updated_at': datetime.strptime(t['recptnDt'], '%Y-%m-%d %H:%M:%S'),
                    'express': t['directAt'] == '1',
                    'last': t['lstcarAt'] == '1',
                }
                trains.append(Train(**data))
            return trains
