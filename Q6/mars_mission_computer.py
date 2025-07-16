import random

class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0,
            "mars_base_external_temperature": 0,
            "mars_base_internal_humidity": 0,
            "mars_base_external_illuminance": 0,
            "mars_base_internal_co2": 0,
            "mars_base_internal_oxygen": 0,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    def get_env(self):
        return self.env_values


ds = DummySensor()
ds.set_env()
print(ds.get_env())


# Class : 상위개념. 블랙핑크, 방탄, 아이유 등은 가수이고 가수가 Class다.
# __init__(self):는 파이썬 클래스에서 생성자 메서드입니다. 객체가 생성될 때 자동으로 호출되며, 클래스의 초기 상태를 설정하는 데 사용됩니다. 클래스의 초기 상태를 설정하는 생성자 역할을 하려면 반드시 __init__(self) 메서드를 정의해야 한다.
# random.uniform()을 사용하여 각 항목의 값을 지정된 범위 내에서 랜덤하게 생성
#  self는 파이썬 클래스에서 현재 객체(instance)를 참조하기 위해 사용된다. 클래스 메서드에서 self를 사용하면 해당 객체의 속성이나 메서드에 접근할 수 있다.
