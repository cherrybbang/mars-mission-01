import csv

print('Hello Mars')

origin_file = 'mission_computer_main.log'
output_file = 'log_analysis.md'

try:
    # mission_computer_main.log 파일 읽기
    with open(origin_file, 'r', encoding='utf-8') as file:
      reader = csv.reader(file)
      header = next(reader)
      rows = list(reader)

      # 화면출력
      print("[mission_computer_main.log 출력하기]")
      for row in rows:
          print(row)

      # 시간역순으로 정렬
      rows.sort(key=lambda x: x[0], reverse=True)

      # 첫 7개의 항목만 처리
      rows = rows[:3]

      # 마크다운으로 저장
      with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write('# log_analysis 보고서\n\n')
        md_file.write('| Timestamp           | Event                     | Message                                   |\n')
        md_file.write('|---------------------|---------------------------|-------------------------------------------|\n')
        for row in rows:
            md_file.write(f'| {row[0]} | {row[1]} | {row[2]} |\n')

      print(f'{output_file} 파일이 생성되었습니다.')

except FileNotFoundError:
    print(f'에러내용 : {origin_file} 파일을 찾을 수 없습니다.')
except Exception as e:
    print(f'에러내용 : {e}')