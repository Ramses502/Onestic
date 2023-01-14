from fastapi import FastAPI
import csv, operator

app = FastAPI()

#API ENDPOINTS --------------------------------------------------------------------------------------------------

@app.get("/report1")
def report1():
    arraysOfProducts = []
    arrayIDsOrders = []

    with open('../../Data/orders.csv', newline='') as csvfile:
        readerOrders = csv.DictReader(csvfile)
        for orders in readerOrders:
            arrayIDsOrders.append(orders['id'])
            arraysOfProducts.append(orders['products'].split(" "))
        csvfile.close()

    productsTable = csvtable('../../Data/products.csv')
    tableResult = {}
    rowIterator = 0
    costOfOrder = 0

    for order in arraysOfProducts:
        for product in order:
            if product in productsTable.keys(): 
                cost = productsTable[product]['cost']
                costOfOrder = costOfOrder + float(cost)
                idOrder = arrayIDsOrders[rowIterator]
                tableResult[idOrder] = costOfOrder
        rowIterator = rowIterator + 1
        costOfOrder = 0
    writeCSV(1, arrayIDsOrders, tableResult)

    return "order_prices.csv generated"

@app.get("/report2")
def report2():
    tableResult = {}

    ordersTable = csvtable('../../Data/orders.csv')
    customersTable = csvtable('../../Data/customers.csv')
    productsTable = csvtable('../../Data/products.csv')

    arrayPorductsCustomers = []
    for product in productsTable.keys():
        arrayPorductsCustomers.append("")

    for product in productsTable.keys():
        for order in ordersTable.keys():
            if product in ordersTable[order]['products']:
                arrayPorductsCustomers[int(product)] = str(arrayPorductsCustomers[int(product)]) + " " + ordersTable[order]["customer"]

    for product in productsTable:
        tableResult[product] = arrayPorductsCustomers[int(product)]
        
    writeCSV(2, "", tableResult)
    
    return "product_customers.csv generated"

@app.get("/report3")
def report3():

    arrayIDsCustomers = []
    arraysOfProducts = []
    tableResult = {}
    tableCustomerProducts = {}

    customersTable = csvtable('../../Data/customers.csv')
    productsTable = csvtable('../../Data/products.csv')

    with open('../../Data/orders.csv', newline='') as csvfile:
        readerOrders = csv.DictReader(csvfile)
        for orders in readerOrders:
            arrayIDsCustomers.append(orders['customer'])
            arraysOfProducts.append(orders['products'].split(" "))
        csvfile.close() 

    rowIterator = 0
    for customer in arrayIDsCustomers:
        tableCustomerProducts[customer] = []
        tableResult[customer] = 0

    for customer in arrayIDsCustomers:
        tableCustomerProducts[customer] += arraysOfProducts[rowIterator]
        rowIterator = rowIterator + 1
    
    for customer in tableCustomerProducts.keys():
        for product in tableCustomerProducts[customer]:
            tableResult[customer] += float(productsTable[product]['cost'])

    writeCSV(3, customersTable, tableResult)

    return "customer_ranking.csv generated"

#FUNCTIONS ------------------------------------------------------------------------------------------------------

def csvtable(file):     # Read CSV file into 2-D dictionary
    table = {}
    f = open(file)
    columns = f.readline().strip().split(',')       # Get column names
    
    for line in f.readlines():
        values = line.strip().split(',')            # Get current row
        for column,value in zip(columns,values):
            if column == 'id':                    # table['TREX'] = {}
                key = value
                table[key] = {}
            else:
                table[key][column] = value          # table['TREX']['LENGTH'] = 10
    
    f.close()
    return table

def writeCSV(report, AdditionalData, tableResult):
    if report == 1:
        with open('../../Data/order_prices.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["id", "total"])
            for idOrder in AdditionalData:
                if idOrder in tableResult.keys():
                    writer.writerow([idOrder, tableResult[idOrder]])
    
    elif report == 2:
        with open('../../Data/product_customers.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["id", "customer_ids"])
            for product in tableResult.keys():
                writer.writerow([product, tableResult[product]])

    else:
        with open('../../Data/customer_ranking.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["id", "name", "lastname", "total"])
            for customer in tableResult:
                writer.writerow([customer, AdditionalData[customer]['firstname'], AdditionalData[customer]['lastname'], tableResult[customer]])
        
        with open('../../Data/customer_ranking.csv', 'r', newline='') as f_input:
            csv_input = csv.DictReader(f_input)
            data = sorted(csv_input, key=lambda row: (float(row['total'])), reverse=True)

        with open('../../Data/customer_ranking.csv', 'w', newline='') as f_output:    
            csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
            csv_output.writeheader()
            csv_output.writerows(data)

            