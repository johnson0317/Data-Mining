from openpyxl import load_workbook
import pandas as pd
import csv
result = []
with open('records.csv', 'r', newline = '') as csvFile:
    File = csv.reader(csvFile)
    for rows in File:
        r = []
        for ele in rows:
            if ele == 'False':
                r.append('0')
            elif ele == 'True':
                r.append('1')
            else:
                r.append(ele)
        result.append(r)
with open('processed.csv', 'a', newline = '') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(result)