import sys
import os
import json
import time

sys.path.append("../Q6")
from mars_mission_computer import DummySensor


class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0,
            "mars_base_external_temperature": 0,
            "mars_base_internal_humidity": 0,
            "mars_base_external_illuminance": 0,
            "mars_base_internal_co2": 0,
            "mars_base_internal_oxygen": 0,
        }

    def get_sensor_data(self):
        while True:
            ds = DummySensor()
            ds.set_env()
            sensor_data = ds.get_env()
            self.env_values.update(sensor_data)

            print(json.dumps(self.env_values, indent=2))

            time.sleep(5)


RunComputer = MissionComputer()
RunComputer.get_sensor_data()


# ds.set_env() 없이 바로 get_env()를 호출하면 env_values값들이 0으로만 반환된다. ds.set_env()로 우선적으로 랜덤한 값들로 env_values를 업데이트 해줘야 한다.

# set_env() : 랜덤 데이터 생성
# get_env() : 현재 저장된 데이터 반환
# time.sleep(5) : 프로그램 일시정지. 5초동안 실행을 멈춤. 초단위로 계산 ex) 6분이면 360

# 다른 파일에서 import 할때는 같은 파일명으로 설정하면 안된다.
