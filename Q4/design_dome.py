import math

# 재질의 무게 (화성무게로 계산)
glass = 2.4 / 6
aluminum = 2.7 / 6
carbon_steel = 7.8 / 6

# 전역변수
material = glass
diameter = None
thickness = 1
area = None
weight = None

# 돔 전체 면적 구하기
def sphere_area(diameter):
    """
    돔 전체 면적을 구하는 함수.
    입력: diameter (지름)
    출력: 반구체의 총 표면적
    """
    radius = diameter / 2
    area = 3 * math.pi * (radius ** 2)
    return area   # 돔의 전체 면적

# 돔 무게 구하기
def calculate_weight():
    global material, diameter, thickness, area, weight

    area = sphere_area(diameter_input)
    weight = area * thickness * material

# 재질 입력
while True:
    material_input = input('재질입력 (유리, 알루미늄, 탄소강 중 선택): ')
    if material_input == '유리':
        material = glass
        break
    elif material_input == '알루미늄':
        material = aluminum
        break
    elif material_input == '탄소강':
        material = carbon_steel
        break
    else:
        print('잘못된 재질입니다. 다시 입력해주세요.')

# 지름 입력
while True:
    diameter_input = input('지름입력 (숫자만 입력): ')
    try:
        diameter_input = float(diameter_input)
        if diameter_input <= 0:
            print('지름은 0보다 커야 합니다. 다시 입력해주세요.')
            continue
        break
    except ValueError:
        print('숫자를 입력해주세요.')

calculate_weight()

print(f'재질 => {material_input}, 지름 => {diameter_input}, 두께 => {thickness}, 면적 => {area:.3f}, 무게 => {weight:.3f}kg')

# 반복 여부 확인
# repeat = input('다시 계산하시겠습니까? (예/아니오): ')
# if repeat.lower() != '예':
#   print('프로그램을 종료합니다.')