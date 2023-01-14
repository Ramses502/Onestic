from fastapi import FastAPI
import csv, operator

app = FastAPI()

#API ENDPOINTS --------------------------------------------------------------------------------------------------

@app.get("/report1")
def report1():
    arraysOfProducts = []
    arrayIDsOrders = []
    
    #Cargo el CSV de pedidos y lo itero para obtener un array de IDs de los pedidos y una array de arrays de los productos.
    with open('../../Data/orders.csv', newline='') as csvfile:
        readerOrders = csv.DictReader(csvfile)
        for orders in readerOrders:
            arrayIDsOrders.append(orders['id'])
            arraysOfProducts.append(orders['products'].split(" "))
        csvfile.close()

    #Cargo el CSV e inicializo las varibales que voy a usar más tarde.
    productsTable = csvtable('../../Data/products.csv')
    tableResult = {}
    rowIterator = 0
    costOfOrder = 0

    #Itero la array de arrays creada al principio y a su vez itero las arrays de dentro de la misma. Para cada iteración de las arrays saco el coste del producto
    #y lo voy sumando al coste total de ese pedido. Al final hago una tabla de IDs de los pedidos con su respectivo coste total calculado.
    for order in arraysOfProducts:
        for product in order:
            if product in productsTable.keys(): 
                cost = productsTable[product]['cost']
                costOfOrder = costOfOrder + float(cost)
                idOrder = arrayIDsOrders[rowIterator]
                tableResult[idOrder] = costOfOrder
        rowIterator = rowIterator + 1
        costOfOrder = 0

    #Se llama a la función que genera el CSV con la tabla resultante a faltas de concatenar a la tabla los IDs de las ordenes.   
    writeCSV(1, arrayIDsOrders, tableResult)

    return "order_prices.csv generated"

@app.get("/report2")
def report2():
    tableResult = {}
    
    #Cargo los dos CSV que voy a usar en tablas para poder extraer sus datos.
    ordersTable = csvtable('../../Data/orders.csv')
    productsTable = csvtable('../../Data/products.csv')

    #Creo he inicializo el array con todas las "posiciones" de la misma que voy a usar. Para ello las inicializo metiendoles la cadena vacía.
    arrayPorductsCustomers = []
    for product in productsTable.keys():
        arrayPorductsCustomers.append("")

    #Itero las tablas de productos y pedidos para comprobar de cada orden si el producto está en la columna products y así recoger su comprador.
    #Este comprador lo añadimos (si no está ya añadido) a una array donde cada posición representa a un producto.
    for product in productsTable.keys():
        for order in ordersTable.keys():
            if product in ordersTable[order]['products'] and not(ordersTable[order]["customer"] in str(arrayPorductsCustomers[int(product)])):
                arrayPorductsCustomers[int(product)] = str(arrayPorductsCustomers[int(product)]) + " " + ordersTable[order]["customer"]
    
    #Generamos la tabla resultante y la pasamos al generador de CSVs
    for product in productsTable:
        tableResult[product] = arrayPorductsCustomers[int(product)]
        
    writeCSV(2, "", tableResult)
    
    return "product_customers.csv generated"

@app.get("/report3")
def report3():

    #Variables que voy a usar
    arrayIDsCustomers = []
    arraysOfProducts = []
    tableResult = {}
    tableCustomerProducts = {}

    #Cargo como tablas los CSV que voy a usar
    customersTable = csvtable('../../Data/customers.csv')
    productsTable = csvtable('../../Data/products.csv')

    #Como en el primer endpoint, extraigo la columna de clientes y la columna de productos como array de arrays.
    with open('../../Data/orders.csv', newline='') as csvfile:
        readerOrders = csv.DictReader(csvfile)
        for orders in readerOrders:
            arrayIDsCustomers.append(orders['customer'])
            arraysOfProducts.append(orders['products'].split(" "))
        csvfile.close() 

    #Inicializo con las posiciones que voy a usar la tabla resultante y la tabla auxiliar de clientes-productos que voy a utilizar.
    rowIterator = 0
    for customer in arrayIDsCustomers:
        tableCustomerProducts[customer] = []
        tableResult[customer] = 0

    #Iteramos la tabla de clientes para que por cada cliente se le añadan los productos que ha comprado.
    for customer in arrayIDsCustomers:
        tableCustomerProducts[customer] += arraysOfProducts[rowIterator]
        rowIterator = rowIterator + 1
    
    #Iteramos la tabla creada anteriormente e iteramos cada array de productos de cada posición. Por cada iteración de las arrays de productos vamos
    #sumando para ese cliente lo que le ha costado cada producto y así obtenemos el total que se ha gastado.
    for customer in tableCustomerProducts.keys():
        for product in tableCustomerProducts[customer]:
            tableResult[customer] += float(productsTable[product]['cost'])

    #Con la tabla resultante llamamos al generador de CSVs.
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
            if column == 'id':                      # table['TREX'] = {}
                key = value
                table[key] = {}
            else:
                table[key][column] = value          # table['TREX']['LENGTH'] = 10
    
    f.close()
    return table

def writeCSV(report, AdditionalData, tableResult):

    #Cuando se le llama para el report1
    if report == 1:
        #Abrimos un writer con el CSV a generar.
        with open('../../Data/order_prices.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            #Escribimos el nombre de las columnas
            writer.writerow(["id", "total"])
            #Iteramos en el array de datos adicionales (en este caso le he pasado el array de IDs de pedidos) para extraerlos para
            #la columna "id" y como indice para la tabla resultante y asi poder printear el id de la orden y cuanto ha costado.
            for idOrder in AdditionalData:
                if idOrder in tableResult.keys():
                    writer.writerow([idOrder, tableResult[idOrder]])
    
    #Cuando se le llama para el report2
    elif report == 2:
        #Abrimos un writer con el CSV a generar.
        with open('../../Data/product_customers.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            #Escribimos el nombre de las columnas
            writer.writerow(["id", "customer_ids"])
            #Iteramos la tabla resultante para sacar los IDs de los productos y poder llenar la columna "id" y estos mismos los usamos
            #para sacar los IDs de los clientes que los compraron.
            for product in tableResult.keys():
                writer.writerow([product, tableResult[product]])

    else:
        #Abrimos un writer con el CSV a generar.
        with open('../../Data/customer_ranking.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            #Escribimos el nombre de las columnas
            writer.writerow(["id", "name", "lastname", "total"])
            #Iteramos en la tabla resultante para sacar el ID de los clientes y su gasto total, también usamos la tabla adicional que le he pasado
            #para extraer el nombre y apellidos de cada cliente.
            for customer in tableResult:
                writer.writerow([customer, AdditionalData[customer]['firstname'], AdditionalData[customer]['lastname'], tableResult[customer]])
        
        #Una vez ya hemos generado el CSV lo volvemos a cargar, esta vez para ordenarlo. Lo hago porque de la forma que trataba los CSV no 
        #me permitia ordenarlo.
        with open('../../Data/customer_ranking.csv', 'r', newline='') as f_input:
            csv_input = csv.DictReader(f_input)
            data = sorted(csv_input, key=lambda row: (float(row['total'])), reverse=True)

        #Sobreescribimos el CSV esta vez ya ordenado por gasto.
        with open('../../Data/customer_ranking.csv', 'w', newline='') as f_output:    
            csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
            csv_output.writeheader()
            csv_output.writerows(data)

            