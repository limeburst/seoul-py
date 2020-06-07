""":mod:`seoul.subway.train` --- Subway train
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum


class Direction(IntEnum):
    UP = 0  # 상행, 외선
    DOWN = 1  # 하행, 내선


class Status(IntEnum):
    ENTER = 0  # 진입
    ARRIVE = 1  # 도착
    DEPART = 2  # 출발


@dataclass(frozen=True)
class Train(dict):
    number: str
    subway_id: str
    subway_name: str
    station_id: str
    station_name: str
    terminal_station_id: str
    terminal_station_name: str
    express: bool
    last: bool
    status: Status
    direction: Direction
    updated_at: datetime

