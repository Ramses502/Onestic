from fastapi import FastAPI
import pandas as pd
import csv

app = FastAPI()
#API ENDPOINTS --------------------------------------------------------------------------------------------------
@app.get("/my-first-api")
def hello():
    arraysOfProducts = []
    arrayIDsOrders = []

    with open('../../Data/orders.csv', newline='') as csvfile:
        readerOrders = csv.DictReader(csvfile)
        for orders in readerOrders:
            arrayIDsOrders.append(orders['id'])
            arraysOfProducts.append(orders['products'].split(" "))

    with open('../../Data/products.csv', newline='') as csvfile:
        readerProducts = csv.DictReader(csvfile)
        #Hacer bucle anidado que llame los mini arrays a los productos por id
        for product in readerProducts:
            if product['id'] == 

    return arraysOfProducts


#FUNCTIONS ------------------------------------------------------------------------------------------------------


def getProductById(productId, products):
    for p in products:
        if p['id'] == productId:
            product = p
    return product

def loadProducts():
    with open('../../Data/products.csv', newline='') as csvfile:
        readerProducts = csv.DictReader(csvfile)
    return readerProducts