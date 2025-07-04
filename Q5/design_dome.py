import numpy as np

arr1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', skip_header=1)
arr2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', skip_header=1)
arr3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', skip_header=1)

parts = np.vstack((arr1, arr2, arr3))
column_average = np.mean(parts, axis=0)  # axis=0 배열의 각 열의 평균값 계산

# 디버깅 출력
print("parts 배열:", parts)
print("각 열의 평균값:", column_average)

filtered_values = column_average[column_average < 50]

if filtered_values.size == 0:
    print("조건에 맞는 값이 없습니다. 파일이 생성되지 않았습니다.")
else:
    np.savetxt('parts_to_work_on.csv', filtered_values, delimiter=',', fmt='%.2f')
    print('parts_to_work_on.csv가 생성되었습니다.')