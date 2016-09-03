#!/usr/bin/python
import sys
import time
from datetime import date, timedelta
import generic
import index
import transactionCalculations
import yahooIndex

def main(argv):
    transactions = generic.getTransaction(argv[1])

    totalDeposit = 0
    deposits = {}
    earliestDate = date.today()
    for transaction in transactions:
        if transaction[0].year not in deposits:
            deposits[transaction[0].year] = 0

        deposits[transaction[0].year] = deposits[transaction[0].year] + transaction[1]

        totalDeposit = totalDeposit + transaction[1]

        if transaction[0] < earliestDate:
            earliestDate = transaction[0]

    print "Share of deposits per year:"
    for key in deposits.keys():
        print("%d: %.2f%%" % (key, deposits[key]/totalDeposit*100))
    print ""

    interest = transactionCalculations.interestFromTransactions(transactions, int(argv[2]), index.Index())
    print "Yearly interest: " + str(interest) + "%"

    if len(argv) == 4:
        idx = yahooIndex.YahooIndex(argv[3], earliestDate)
        interest = transactionCalculations.interestFromTransactions(transactions, int(argv[2]), idx)
        print "Yearly interest relative to " + argv[3] + ": " + str(interest) + "%"

if __name__ == "__main__":
    if len(sys.argv) != 4 and len(sys.argv) != 3:
        print "Usage: python " + sys.argv[0] + " [csv file] [value today] [index (optional)]"
        exit(1)
    main(sys.argv)
