import csv
import json

origin_file = 'mission_computer_main.log'
output_json_file = 'mission_computer_main.json'

try:
  # mission_computer_main.log 파일 읽기
  with open(origin_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)

    # 시간역순으로 정렬
    rows.sort(key=lambda x: x[0], reverse=True)

    # 리스트 데이터를 dict로 변환
    log_dicts = [dict(zip(header, row)) for row in rows]

    # JSON으로 저장
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
      json.dump(log_dicts, json_file, ensure_ascii=False, indent=4)

    print(f'{output_json_file} 파일이 생성되었습니다.')

except FileNotFoundError:
  print(f'에러내용 : {origin_file} 파일을 찾을 수 없습니다.')
except Exception as e:
  print(f'에러내용 : {e}')


# csv? 데이터를 쉼표 혹은 다른 구분자로 구분하여 저장하는 텍스트 파일 형식. (comma-separated values)
# csv.reader : csv 파일의 데이터를 row(행) 단위로 읽는다.
# next(reader) : reader에서 첫번째 행을 가져온다.