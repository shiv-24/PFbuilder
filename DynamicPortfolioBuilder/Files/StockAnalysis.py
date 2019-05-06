import numpy
from datetime import datetime
import Files.FetchData as FD

dbName = 'market_data'
stockCollName = 'stock_data'
indexCollName= 'benchmark_data'

data = FD.findDataWithFilters_AllFields(dbName,stockCollName,{'Ticker':'AAPL'},[('Date',1)])
# for val in data:
    # print(val.get('Close'))
# for data in FD.findDataWithFilters_AllFields(dbName,collName,{'Ticker':'AAPL'}):
#     print(data)

print("\n")

# for data in FD.findDataWithFilters_CustomFields(dbName,collName,{'Ticker':'AAPL'},{'CompanyName':1,'_id':0}):
#     print(data)

disStocks = FD.getDistinctValues(dbName,stockCollName,'Ticker')
disIndexes = FD.getDistinctValues(dbName,indexCollName,'BenchmarkTicker')

start = datetime(2014, 5, 2, 0, 0, 0)
end = datetime(2019, 4, 30, 0, 0, 0)
for stock in disStocks:
    print(stock)
    data = FD.findDataWithFilters_CustomFields(dbName,stockCollName,{'Ticker':stock,'Date':{'$lte':end,'$gte':start}},{'Close':1,'Date':1},[('Date',1)])
    stockReturns =[]
    # stockDate =[]
    iterData = iter(data)
    prev = next(iterData)
    for cur in iterData:
        prevClose = prev.get('Close')
        curClose  = cur.get('Close')
        perDayReturn = (curClose-prevClose)/prevClose
        stockReturns.append(perDayReturn)
        prev = cur
        # stockDate.append(cur.get('Date'))
    for index in disIndexes:
        print(index)
        indexData = FD.findDataWithFilters_CustomFields(dbName,indexCollName,{'BenchmarkTicker':index,'Date':{'$lte':end,'$gte':start}},{'Close':1,'Date':1},[('Date',1)])
        indexReturns =[]
        iterIndexData = iter(indexData)
        prevIndex = next(iterIndexData)
        indexDate =[]
        for cur in indexData:
            prevIndexClose = prevIndex.get('Close')
            curIndexClose  = cur.get('Close')
            perDayIndexReturn = (curIndexClose-prevIndexClose)/prevIndexClose
            indexReturns.append(perDayIndexReturn)
            prevIndex = cur
        break
    break

cov = numpy.cov(stockReturns,indexReturns,bias=True)[0][1]
var = numpy.var(indexReturns)
beta = cov/var
rfr = 0.0253
mktAvg = numpy.average(indexReturns)
expectedReturnFromFormula = rfr+beta*(mktAvg-rfr)                  #ER = rfr+beta*(mktAvg-rfr)
expectedReturnWithoutFormula = numpy.average(stockReturns)

# print('variance is ')
# print(var)
#
# print('beta is ')
# print(beta)
#
# print('Mkt avgs is ')
# print(mktAvg)
#
#
# print(expectedReturnFromFormula)
# print(expectedReturnWithoutFormula)


# for returnVal in stockReturns:
#     print(returnVal)

# for oneDate in stockDate:
    # print(oneDate)
# print('##################')
# for returnVal in indexReturns:
#     print(returnVal)
# for oneDate in indexDate:
#     print(oneDate)

