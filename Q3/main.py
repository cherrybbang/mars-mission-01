import csv
import pickle

origin_file = 'Mars_Base_Inventory_List.csv'
output_file = 'Mars_Base_Inventory_danger.csv'
binary_file = 'Mars_Base_Inventory_List.bin'


try:
    with open(origin_file, 'r', encoding='utf-8') as file:
      reader = csv.reader(file)
      header = next(reader) 
      rows = list(reader)

      sorted_rows = sorted(rows, key=lambda x: float(x[4]) if x[4] != 'Various' else -1, reverse=True)

      danger_rows = sorted(
          [row for row in rows if row[4] != 'Various' and float(row[4]) >= 0.7],
          key=lambda x: float(x[4]),
          reverse=True
      )

      with open(binary_file, 'wb') as bin_file:
        pickle.dump(sorted_rows, bin_file)

        print(f'{binary_file} 파일이 생성되었습니다.')

      with open(output_file, 'w', encoding='utf-8') as danger_file:
        writer = csv.writer(danger_file)
        writer.writerow(header)  # 헤더 작성
        writer.writerows(danger_rows)

        print(f'{output_file} 파일이 생성되었습니다.')

except FileNotFoundError:
    print(f'에러내용 : {origin_file} 파일을 찾을 수 없습니다.')
except Exception as e:
    print(f'에러내용 : {e}')




# pickle : pickle module implements binary protocols for serializing and de-serializing a Python object structure

# a = [1,2,3]

# # pkl 저장
# with open('test.pkl', 'wb') as f:
#     pickle.dump(a, f)

# # pkl 불러오기
# with open('test.pkl', 'rb') as f:
#     b = pickle.load(f)

# print(b)
# >>> [1, 2, 3]