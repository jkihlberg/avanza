#!/usr/bin/python
import csv
import time
from datetime import date, timedelta

# Date to date-type for date on the format '2016-07-16'
def transactionDateFromString(stringDate):
    stringSplit = stringDate.split('-')
    return date(int(stringSplit[0]), int(stringSplit[1]), int(stringSplit[2]))

def getTransaction(filename):
    csvfile = open(filename, 'rb')
    transactionreader = csv.reader(csvfile, delimiter=';', quotechar='|')

    # Transactions, on the format [[date, ammount], ... ]
    transactions = []

    # Skip the first row, it is just headings that we are not interested in
    row = transactionreader.next()
    for row in transactionreader:
        transactionDate = transactionDateFromString(row[0])
        userText = row[3]
        ammount = float(row[6].replace(',', '.'))

        # 'Avanzakonto' is present during internal transactions, which we ignore
        if "Avanzakonto" in userText:
            continue

        transactions.append([transactionDate, ammount])

    return transactions
