#!/usr/bin/python
import csv
import sys
import time
from datetime import date, timedelta
import generic

class Index:
    def __init__(self):
        self.closingPrice = []
        self.earliestDate = date.today()

        self.closingPrice = [[generic.transactionDateFromString("1900-1-1"), 1]]
        self.earliestDate = generic.transactionDateFromString("1900-1-1")

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