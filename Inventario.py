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

def mostrar_reporte_general(inventario):#definimos la funcion para que nos de los reportes generales
    print("\n========= REPORTE GENERAL ==========")
    inventario = calcular_valor_total(inventario) #Para estar tranquilos volvemos a calcular el valor total

    total_productos = len(inventario) #len cuenta cuantas filas tiene la tabla
    #(Cuantos productos distintos hay en el inventario)
    total_unidades = inventario["cantidad"].sum()#sum suma la columna cantidad
    valor_total_inventario = inventario["valor_total"].sum()#Suma el valor monetario del inventario
    producto_mayor_valor = inventario.sort_values( #sort values ordena la tabla por una columna
        by = "valor_total", #este es por lo cual quiero ordenar la columna
        ascending = False #significa de mayor a menor (descender)
    ).head(1) #toma solo la primera fila, la cual seria el mas valioso

    producto_mayor_stock = inventario.sort_values(
        by = "cantidad",
        ascending = False
    ).head(1) #Hace exactamente lo mismo solo que para el producto con mayor cantidad

    valor_por_categoria = inventario.groupby("categoria")["valor_total"].sum()#agrupa por categoria de producto.
    #Luego solo trabaja la columna de valor total y suma cada categoría por valor 

    print("La cantidad de productos diferentes son :", total_productos)
    print("Total de unidades en inventario :", total_unidades)
    print("El valor total del inventario es de :Q", valor_total_inventario)

    print("El producto con mayor valor en inventario es: ", producto_mayor_valor)
    print("El producto con mayor stock disponible es: ", producto_mayor_stock)
    print("El valor total por categoría es:")
    print(valor_por_categoria)

    print("\n=============================================")

def guardar_inventario(inventario): #recibe el data frame inventario

    inventario = calcular_valor_total(inventario) #por seguridad guardamos 
    inventario.to_csv(#convierte el data frame en un archivo CSV (comma separated values)
        "inventario.csv",#nombre del achivo
        index=False#para que no tome los indices como parte de los datos.
    )
    print("\nInventario guardado en inventario.csv\n")

def mostrar_menu(): #definimos la funcion mostrar menu

    print("========== SISTEMA DE INVENTARIO JF ===========")

    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Vender producto")
    print("5. Reabastecer producto")
    print("6. Ver productos con bajo stock")
    print("7. Ver reporte general")
    print("8. Guardar inventario")
    print("9. Salir")

    print("================================================")

def main(): #no recibe un parámetro porque esta función crea el inventario

    inventario = crear_inventario_inicial()#esta funcion crea el diccionario, data frame, calcula total y regresa inventario
    continuar = True #creacion de una variable booleana

    while continuar:#minetras continuar sea true repite el menú
        mostrar_menu()
        opcion = input("Selecciona la opción que prefieras :")

        if opcion == "1":
            mostrar_inventario_(inventario)

        elif opcion == "2":
            inventario = agregar_producto(inventario)
        
        elif opcion == "3":
            buscar_producto(inventario)

        elif opcion == "4":
            inventario = vender_producto(inventario)
        
        elif opcion == "5":
            inventario = reabastecer_producto(inventario)
        
        elif opcion == "6":
            mostrar_bajo_stock(inventario)
        
        elif opcion == "7":
            mostrar_reporte_general(inventario)

        elif opcion == "8":
            guardar_inventario(inventario)
        
        elif opcion == "9":
            guardar_inventario(inventario)
            print("Gracias por usar este sistema")
            continuar = False
        
        else:
            print("Opción no válida.")

main()

            