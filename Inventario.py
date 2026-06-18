import pandas as pd #importar la librería pandas para usar en este proyecto y renombrarla

#Definir función calcular inventario (será llamada después)

def calcular_valor_total(inventario):
    inventario["valor_total"] = inventario ["cantidad"] * inventario["precio"] #Toma la columna cantidad y precio y las multiplica
    return inventario

#Sección 1, crear el inventario y almacenarlo en la función crear inventario inicial

def crear_inventario_inicial ():
    datos = { #Creamos el diccionario que se llama datos para esta función
        "código" : ["LAP001", "MOU001", "TEC001", "MON001", "USB001"],
        "producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Memoria USB"],
        "categoría": ["Computadoras", "Accesorios", "Accesorios", "Pantallas", "Almacenamiento"],
        "cantidad": [5, 20, 10, 4, 30],
        "precio": [4500.00, 75.00, 150.00, 1200.00, 60.00]
    }
    inventario = pd.DataFrame(datos) #Convierte los datos anteriores en una tabla
    inventario = calcular_valor_total(inventario) #Ahora si, calcula el valor total con la función previamente definída
    return inventario 