import numpy

arr1 = numpy.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', skip_header=1, usecols=1)
# 첫번째 행(=헤더)을 건너뛰고 두번째 열을 읽어 arr1 배열로 저장.

arr2 = numpy.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', skip_header=1, usecols=1)
arr3 = numpy.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', skip_header=1, usecols=1)

parts = numpy.vstack((arr1, arr2, arr3))
# arr1, arr2, arr3 배열을 병합하여 parts 라는 배열을 만든다.
column_average = numpy.mean(parts, axis=0)  # axis=0 배열의 각 열의 평균값 계산

filtered_values = column_average[column_average < 50]

if filtered_values.size == 0:
    print("파일 생성되지 않음.")
else:
    numpy.savetxt('parts_to_work_on.csv', filtered_values, delimiter=',', fmt='%.2f')
    print('parts_to_work_on.csv가 생성되었습니다.')


# genfromtxt : 텍스트파일 (csv 등)을 읽어 배열로 변환하는 함수. 숫자뿐만 아니라 nan도 처리가능.
# delimiter : 파일에서 데이터를 구분하는 문자 지정. delimiter=',' 는 쉼표로 구분된 파일을 읽겠다는 의미.
# skip_header : 파일의 상단에서 건너뛸 행 수를 지정. skip_header=0일 경우, 모든 행을 읽음.
# usecols : 읽어올 열의 인덱스를 지정. usecols=1은 두번째 열을 읽겠다는 의미.

# vstack : 동일한 열(column) 수를 가진 배열을 하나로 합칠 때 사용.
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# result = np.vstack((arr1, arr2))

# mean : 배열의 평균값을 계산하는 함수. axis=0은 각 열의 평균값을 계산, axis=1은 각 행의 평균값을 계산.
# numpy.mean(parts, axis=0) : parts 배열의 각 열의 평균값을 구한다.

# 아래 코드는 첫 번째 행을 건너뛰고, 두 번째와 세 번째 열만 읽어 배열로 저장한다.
# import numpy as np

# data = np.genfromtxt('data.csv', delimiter=',', skip_header=1, usecols=(1, 2))
# print(data)