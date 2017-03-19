#!/usr/bin/python
import generic
from datetime import date, timedelta

class PercentageIndex:
    def __init__(self,percentage):
        self.percentage = 1 + percentage/100.0

    def getValue(self, date):
        assert 0 == 1
		# Get value not relevant for percentage index.

    def getFactor(self, startDate, endDate):
        assert startDate <= endDate

        yearBetweenDates = ((endDate - startDate).days)/365.25
        return pow(self.percentage, yearBetweenDates)

    def getPercent(self, startDate, endDate):
        return self.getFactor(startDate, endDate) - 1