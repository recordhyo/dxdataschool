import csv

data = []
with open('./data/busan.csv', 'a') as file:
    '''
    rdr = csv.reader(file)
    for line in rdr :
        data.append(line)
print(data)
    '''

    wr = csv.writer(file)
    wr.writerow(['21', '21번약국', '010-010', "부산광역시 00구 "])
