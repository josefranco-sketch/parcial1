import pandas as pd #importar la librería pandas para usar en este proyecto y renombrarla

#Definir función calcular inventario (será llamada después)

def calcular_valor_total(inventario):
    inventario["valor_total"] = inventario ["cantidad"] * inventario["precio"] #Toma la columna cantidad y precio y las multiplica
    return inventario