class DummySensor:
  def __init__(self):
    self.env_values = {
      'mars_base_internal_temperature' : 0,
      'mars_base_external_temperature' : 0,
      'mars_base_internal_humidity' : 0,
      'mars_base_external_illuminance' : 0,
      'mars_base_internal_co2' : 0,
      'mars_base_internal_oxygen' : 0
    }



# Class : 상위개념. 블랙핑크, 방탄, 아이유 등은 가수이고 가수가 Class다.
# __init__(self):는 파이썬 클래스에서 생성자 메서드입니다. 객체가 생성될 때 자동으로 호출되며, 클래스의 초기 상태를 설정하는 데 사용됩니다.