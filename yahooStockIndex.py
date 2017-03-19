#!/usr/bin/python
from yahoo_finance import Share
import generic
from datetime import date, timedelta

class YahooStockIndex:
    def __init__(self,ticker, startDate):
        self.closingPrice = []
        self.earliestDate = date.today()

        idx = Share(ticker)

        if idx.get_open() == None:
            print "Error, ticker not found! Tickers can be found on finance.yahoo.com. Example ticker: ^OMX for OMX30"
            return

        historicals = idx.get_historical(str(startDate - timedelta(days=365)), str(date.today()))

        for historical in historicals:
            transactionDate = generic.transactionDateFromString(historical['Date'])
            closingPrice = historical['Close']

            if transactionDate < self.earliestDate:
                self.earliestDate = transactionDate

            self.closingPrice.append([transactionDate, float(closingPrice)])

    def getValue(self, date):
        assert date >= self.earliestDate

        for closingPrice in self.closingPrice:
            if date >= closingPrice[0]:
                return closingPrice[1]

    def getFactor(self, startDate, endDate):
        assert startDate <= endDate

        return self.getValue(endDate) / self.getValue(startDate)

    def getPercent(self, startDate, endDate):
        return self.getFactor(startDate, endDate) - 1