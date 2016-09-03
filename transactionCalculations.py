#!/usr/bin/python
import csv
import sys
import time
from datetime import date, timedelta
import math
import numpy as np
import matplotlib.pyplot as plt
import index
import generic

# Value for given yearly interest for a set of transactions for a specific day after accounting the index change
def valueTransactionAndIntrest(transactions, date, interest, idx):
    dailyInterest = pow(1 + interest / 100.0, 1.0/365.0)

    sum = 0
    for transaction in transactions:
        daysSinceTransaction = (date - transaction[0]).days

        # Ignore all future transactions
        if (daysSinceTransaction >= 0):
            sum = sum + (pow(dailyInterest, daysSinceTransaction) + idx.getPercent(transaction[0], date)) * transaction[1]

    return sum

# Returns the interest for a given set of transactions and current value for today
def interestFromTransactions(transactions, value, idx):
    delta = 1.0
    interest = -100.0

    acceptableError = 100
    calculatedValue = 0

    # Todays date, used to calculate date since transaction
    today = date.today()

    while abs(calculatedValue - value) > acceptableError:
        interest = interest + delta
        calculatedValue = valueTransactionAndIntrest(transactions, today, interest, idx)

        if calculatedValue > value:
            interest = interest - delta
            delta = delta / 10.0

    return interest
