import MogoConnector as MC
# import datetime
from dateutil.parser import parse
import os
import csv

client = MC.getMongoClient('127.0.0.1:27017')
path = "C:\\Coding Practice\\Stock Data"
list_of_files={}
for fileName in os.listdir(path):
    if fileName[-4:]=='.csv':
        list_of_files[fileName]= path+"\\"+fileName
    with open(list_of_files[fileName],'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        count = 0
        header = ''
        ticker = ''
        companyName= ''
        for line in csv_reader:
            if count == 3:
                header = line
                break
            if count == 0:
                print(line)
                ticker = line[0][line[0].find("(") + 1:line[0].find(")")]
                start = 3
                end = line[0].find("(")-1
                companyName= line[0][start:end]
            count+=1
        # print(line)

        count = 0
        for line in csv_reader:
            if count>4:
                if not line:
                    break
            MC.insertData(client,'market_data','stock_data',{header[0]:parse(line[0]),
                                                             header[1]: float(line[1]),
                                                             header[2]: float(line[2]),
                                                             header[3]: float(line[3]),
                                                             header[4]: float(line[4]),
                                                             header[5]: float(line[5]),
                                                             'Ticker':ticker,
                                                             'CompanyName':companyName
                                                            })
            count+=1