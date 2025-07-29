import sys
import os
import json
import time
import platform
import psutil

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

    def get_mission_computer_info(self):
        computer_info = {
            "operation_system": platform.system(),
            "operation_system_version": platform.version(),
            "cpu_type": platform.processor(),
            "cpu_core_amount": psutil.cpu_count(logical=True),
            "memory_size": round(psutil.virtual_memory().total / (1024**3), 2),
        }

        print(json.dumps(computer_info, indent=2))

    def get_mission_computer_load(self):
        load_info = {
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
        }

        print(json.dumps(load_info, indent=2))


runComputer = MissionComputer()

if __name__ == "__main__":
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()


# platform 모듈은 운영체제의 이름, 버전 등 시스템 정보를 얻을 수 있다. 아래와 같이 platform 모듈을 사용하는 주요함수가 있다. (현재 실행 중인 시스템 정보를 파악하는데 유용)
# platform.system()은 운영체제의 이름을 반환한다.
# platform.version()은 운영체제의 버전을 반환한다.
# platform.processor()는 CPU의 정보를 반환한다.
