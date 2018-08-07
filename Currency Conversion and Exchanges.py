#exchanges is GBP to other currency. for inverse do 1 / exchange.
#exchange rates retrieved: 24-08-16 13:42 UTC
import datetime #for declaring retieval of rates
import csv #for writing to csv files
exchange_rates_retrieved = datetime.datetime(2016, 8, 24, 13, 42)
exchanges = { 'GBP': 1, 'EUR': 1.17699, 'USD': 1.32581, 'AUD': 1.73810, 'INR': 88.9636, 'CAD': 1.71259, 'AED': 4.86964 }

def conversion(currency_from, currency_to):
    while True:
        try: #making sure the value inputted is a float 
            amount_currency_from_float = float(input("Please enter the amount you wish to convert: "))
            break
        except ValueError:
            print("Not a number")
    inverse_exchange = exchanges['GBP'] / exchanges[currency_from] #finding out what the the currency to the pound is. the operation is, eg, EUR > GBP > USD
    converted_amount_float = inverse_exchange * (exchanges[currency_to] * amount_currency_from_float) 
    converted_amount_str = '%f' % (converted_amount_float)
    amount_currency_from_str = '%f' % (amount_currency_from_float)
    print(amount_currency_from_str+currency_from+" is "+converted_amount_str+currency_to)
    

def conversion_select():
    currency_from_chosen = False
    print("Available currencies:")
    print("Pound Sterling [GBP]")
    print("Euro [EUR]")
    print("US Dollar [USD]")
    print("Australian Dollar [AUD]")
    print("Indian Rupee [INR]")
    print("Canadian Dollar [CAD]")
    print("United Arab Emirates Dollar [AED]")
    while currency_from_chosen == False:
        currency_from = input("Please enter a currency name in the [] to choose a currency to convert from: ")
        for currency in exchanges:
            if currency_from == currency:
                currency_from_chosen = True
                break
    currency_to_chosen = False
    while currency_to_chosen == False: #duplicate of before, perhaps edit for efficiency
        currency_to = input("Please enter a currency name in the [] to choose a currency to convert to: ")
        if currency_to == currency_from:
            print("Cannot convert to the same currency")
        else:
            for currency in exchanges:
                if currency_to == currency:
                    currency_to_chosen = True
                    break
    conversion(currency_from, currency_to)
    
def write_exchange():
    while True:
        file_write_choice = str(input("Please choose which type of file to write exchange rates to: [csv] or [txt] "))
        if file_write_choice == 'csv':
            #csv writing
            with open('Exchange Rates (Created).csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(["Exchange rates retrieved:", exchange_rates_retrieved.isoformat(',')]) 
                csvwriter.writerow(["Default Currency:", "Other Currency:"])
                for currency in exchanges:
                    if currency != 'GBP':
                        exchange_rate_str = '%f' % exchanges[currency]
                        csvwriter.writerow(["1 GBP", exchange_rate_str+currency])

            print("Exchange rates have now been written to 'Exchange Rates Write.csv'")    
            break
        elif file_write_choice == 'txt':               
            txt = open("Exchange Rates.txt", 'w')
            txt.write("Exchange rates retrieved: ")
            txt.write(exchange_rates_retrieved.isoformat(' '))
            txt.write("\n")
            for currency in exchanges:
                if currency != 'GBP':
                    exchange_rate_str = '%f' % exchanges[currency]
                    txt.write("1 GBP = "+exchange_rate_str+" "+currency+"\n")
            txt.close()
            print("Exchange rates have now been written to 'Exchange Rates.txt'")
            break

while True:
    convert_or_exchanges = input("Would you like to convert [c] or get exchange rates? [e]: ")
    if convert_or_exchanges == 'c' or convert_or_exchanges == 'e':
        if convert_or_exchanges == 'c':
            conversion_select()
        else:
            write_exchange()
    else:
        print("Invalid command")
