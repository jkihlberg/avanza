#!/usr/bin/python
import sys
import time
from datetime import date, timedelta
import generic
import index
import transactionCalculations
import yahooStockIndex
import multipleIndex
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the interest from given sets of extracted transactions from Avanza")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("file", type=str, help="transactions file from avanza")
    parser.add_argument("value", type=int, help="value of account")
    parser.add_argument("-s", "--stock", type=str, action='append', help="stock ticker to be added from YahooFinance")
    parser.add_argument("-c", "--currency", type=str, action='append', help="currency ticker to be added from YahooFinance")
    args = parser.parse_args()

    transactions = generic.getTransaction(args.file)

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

    interest = transactionCalculations.interestFromTransactions(transactions, args.value, index.Index())
    print "Yearly interest: " + str(interest) + "%"

    if args.stock or args.currency:
        indexes = []
        indexesString = ""

        if args.currency:
            print "Currency not implemented yet"
            assert 0 == 1
            for currency in args.currency:
                print currency

        if args.stock:
            for stock in args.stock:
                indexesString += stock + "+"
                idx = yahooStockIndex.YahooStockIndex(stock, earliestDate)
                indexes.append(idx)

        indexesString = indexesString[:-1]
        concatantedIndexes = multipleIndex.MultipleIndex(indexes)

        interest = transactionCalculations.interestFromTransactions(transactions, args.value, concatantedIndexes)
        print "Yearly interest relative to " + indexesString + ": " + str(interest) + "%"
        print "\n\n"

        print "List of transactions and yearly interest for each"
        for transaction in transactions:
            value = transactionCalculations.valueTransactionAndIntrest([transaction], date.today(), interest, concatantedIndexes)
            yearsSinceTransaction = ((date.today() - transaction[0]).days)/365.0
            yearlyInterest = pow((value / transaction[1]), (1 / yearsSinceTransaction))
            print("%s: %.1f%%" % (str(transaction[0]), (((yearlyInterest) - 1)* 100.0)))

if __name__ == "__main__":
    main()
