# 파이썬 외부 파일 처리
# Excel CSV 파일 읽기 쓰기 
# CSV : MIME - text/csv

# 예제1
import csv

with open('../resource/sample1.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵하기
    #확인
    for c in reader:
        print(c)

# 예제 2
# 구분열이 , 가 아니면 구분이 안된다
with open('../resource/sample2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader) Header 스킵하기
    #확인
    for c in reader:
        print(c)

# 예제 3 (dict변환)

with open('../resource/sample1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # next(reader) Header 스킵하기
    #확인
    for c in reader:
        for k,v in c.items():
            print(k, v)

# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# newline을 통해 라인처리를 해줘야함. 개행없음처리
with open('../resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

# 예제5
# 위의 예제는 필터링 즉 조건문을 사용해서 처리가 가능
# 이 예제는 바로 쓰는것이다
with open('../resource/sample5.csv', 'w', newline='') as f:
    wt = csv.writer(f)  
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyx1
# pip install pandas

import pandas as pd 

# sheetname = '시트명' 또는 숫자, header=숫자 
xlsx = pd.read_excel('../resource/sample.xlsx')

print(xlsx.head()) # 5개 상위데이터
print(xlsx.tail()) # 5개 하위데이터
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('../resource/result.xlsx', index=False)
xlsx.to_csv('../resource/result.csv', index=False)
