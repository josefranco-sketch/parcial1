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

def mostrar_inventario_(inventario): #Crear la función mostrar inventario y asignarle el parámetro inventario
    print("\n========== INVENTARIO ACTUAL =========\n") #Estética del menú
    if inventario.empty: #definir si el inventario esta vacío con .empty para devolver el siguiente print
        print("El inventario está vacío")
    else: #si no está vacío devuevle el inventario
        print(inventario)
    
    print("\n=======================================\n") #estética

def agregar_producto(inventario):
    print("\n========== AGREGAR PRODUCTO ==========\n")
    codigo = input("Ingrese el código del producto: ")
    producto = input("Ingrese el nombre del producto: ")
    categoría = input("Ingrese la categoría del producto: ")
    cantidad = int(input("Ingrese la cantidad inicial: "))
    precio = float(input("Ingrese el precio unitario: "))

    if not inventario[inventario["codigo"] == codigo ].empty: #definir condición donde evalua si existe o no existe el codigo a ingresar
        print("\nYa existe un producto con ese código") #El if not hace que se devuelva esto si el codigo que se ingresó ya existe
        return inventario #Es necesario pues no deseamos agregar productos duplicados 
    
    nuevo_producto = pd.DataFrame([{ #Creamos nuevo producto con un data frame y generamos el diccionario {}, la lista [] y () que es llamar al dataframe
        "codigo" : codigo,
        "producto" : producto,
        "categoría" : categoría,
        "cantidad" : cantidad,
        "precio" : precio
    }])
    
    inventario = pd.concat( #Esto hace que unamos la tabla con el nuevo producto
        [inventario, nuevo_producto], #importante el orden pues a la tabla original le agrega el nuevo producto
        ignore_index=True #Hace que ignore los indíces anteriores y los reescribe
    )
    inventario = calcular_valor_total(inventario) #Calculara el valor total nuevo de la tabla con el producto agregado
    print("\nProducto agregado correctamente\n")
    return inventario   

def buscar_producto(inventario): #Definir la función buscar producto
    print("\n========== BUSCAR PRODUCTO ==========\n")
    codigo = input("Ingrese el código del producto a buscar: ") #El usuario ingresa el codigo a buscar
    resultado = inventario[inventario["codigo"] == codigo] #Crea una mascara booleana para filtrar y obtener las filas que coinciden

    if resultado.empty: #Condición cuando no encuentra el código
        print("\nno se encontró ningún producto con ese código\n")
    else: #que pasa si si existe el código
        print("\nProducto encontrado :\n")
        print(resultado)
    
    print("\n====================================\n")

def vender_producto(inventario):
    print("\n========== VENDER PRODUCTO ==========")
    codigo = input("Ingrese el código del producto vendido: ")
    resultado = inventario[inventario["codigo"] == codigo]

    if resultado.empty:
        print("\nNo existe un producto con ese código.\n")
        return inventario #Si no existe el producto terminamos esta función de una vez
    
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    cantidad_actual = resultado["cantidad"].iloc[0]#uso de iloc para que de el valor en la primera fila de cantidad

    if cantidad_vendida > cantidad_actual:
        print("\nNo hay suficiente stock.\n")
        return inventario
    inventario.loc[ #usamos .loc para localizar filas, columnas y modificarlas
        inventario["codigo"] == codigo, #Pide la fila del codigo a poner
        "cantidad" #Pide la columna cantidad siguiendo el orden anterior
    ] = cantidad_actual - cantidad_vendida
    
    inventario = calcular_valor_total(inventario) #Recalcula el valor del inventario
    print("\nVenta registrada correctamente\n")
    return inventario  #Nos devuelve la nueva versión del inventario 

def reabastecer_producto(inventario): #Definimos la función para reabastecer un producto
    print("\n========= REABASTECER PRODUCTO ==========\n")

    codigo = input("Ingrese el código del producto a reabastecer: ") #Solicitamos el codigo
    resultado = inventario[inventario["codigo"] == codigo] #Busca la fila del codigo que pusieron

    if resultado.empty: #Definimos que si busca el codigo y no lo encuentra devuelve el mensaje de abajo
        print("\nNo existe un producto con ese código.\n")
        return inventario #regresamos el inventaro 
    
    cantidad_agregada = int(input("Ingrese la cantidad que deseas agregar: ")) #solamente pedimos que nos digan cuantas unidades agregan.
    cantidad_actual = resultado["cantidad"].iloc[0] #tomamos la columna cantida y con el .iloc pedimos el primer valor
    inventario.loc[
        inventario["codigo"] == codigo, "cantidad" #busca la fila del prodcuto que hayamos puesto el codigo
    ] = cantidad_actual + cantidad_agregada #va a la columna cantidad y luego suma ambas cantidades
    inventario = calcular_valor_total(inventario)#Recalcula el valor total con la funcion previamente echa
    print("\nProducto reabastecido correctamente\n")
    return inventario #otra vez devuelve el inventario actualizado

def mostrar_bajo_stock(inventario): #definir la función para encontrar los productos con stock bajo

    print("\n=========== PRODUCTOS CON BAJO STOCK ==========")
    limite = int(input("Ingrese el límite mínimo de stock para el inventario :")) #Pedimos que nos den el número mínimo para el limite

    productos_bajos = inventario[inventario["cantidad"] <= limite] #En la columna cantidad, si es menor o igual al numero lo detecta como true

    if productos_bajos.empty: #definimos la condición si no encuentra productos con bajo stock
        print("\nNo hay productos con bajo stock\n")
    else:#definimos lo que pasaria si encuentra productos con bajo stock
        print("\nProductos con bajo stock:\n")
        print(productos_bajos)

    print("\n=================================================")

