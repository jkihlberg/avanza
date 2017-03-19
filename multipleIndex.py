#!/usr/bin/python
import generic
from datetime import date, timedelta

class MultipleIndex:
    def __init__(self,indexes):
        self.indexes = indexes

    def getValue(self, date):
        # Get Value not relevant for this kind of index.
        assert 0 == 1

    def getFactor(self, startDate, endDate):
        assert startDate <= endDate

        factor = 1
        for index in self.indexes:
            factor = factor * index.getFactor(startDate, endDate)
        return factor

    def getPercent(self, startDate, endDate):
        return self.getFactor(startDate, endDate) - 1