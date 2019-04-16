#!/usr/bin/env python3

# encoding: UTF-8
import sys
import requests
import csv
import datetime

def getDate():
    x = datetime.datetime.now()
    
    day = str(x.day)
    month = x.month
    year = str(x.year)
    new_month =""

    if month<10:
        new_month = "0"+str(month)
    else:
        new_month = str(month)  

    datestr = year + new_month + day

    return datestr

def main(argv=''):

    if(argv != ''):
        datestr = argv
    else:
        datestr = getDate()

    # 下載股價
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

    list_stock = []

    for i in r.text.split('\n'):
        if len(i.split('",')) == 17 and i[0] != '=':
            list_column = []
            for j in i.split('","'):
                list_column.append(j.replace('",','').replace('"',''))

            list_stock.append(list_column)

    with open(datestr + '.csv', "w", newline="") as g:
        csvwriter = csv.writer(g)

        for items in list_stock:
            csvwriter.writerow(items)
    g.close()

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('error')
