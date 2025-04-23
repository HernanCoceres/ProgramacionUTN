#Actividades: 1)
a = list(range(4,101,4)) #Creo la lista "a" que empieza en 4 porque 1,2,3 no son multiplos de 4 y termina en 101 porque 100 quedaria excluido. Y el paso en 4 como pide el ejercicio.
print(a)

# 2)
b = ["a","b","c","d","e"] # el penultimo seria la letra c, que tiene indice 2.
print(b[2])

# 3)
c = [] #declaro array vacio
c.append("mañana") #agrego un elemento, ya que el metodo solo permite 1.
c.append("ayer")
c.append("hoy")
print(c)

# 4)
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro" #reemplazo el valor indicando el indice y reasignando un valor, para reemplazar
animales[3] = "oso"
print(animales)

# 5)
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) #Este codigo esta borrando el elemento con mayor valor de la lista
print(numeros) #Porque imprime la misma lista pero sin el numero 22

# 6)
d = list(range(10,31,5)) #Creo la lista como el primer ejercicio pero ajustando los parametros a esta consigna
print(d[0],d[1]) #Imprimo los dos primeros elementos utilizando sus respectivos indices

# 7)
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fox" #este valor reemplaza "polo". Asignando un nuevo valor al elemento
autos[2] = "saveiro"#este otro valor reemplaza "suran". Asignando un nuevo valor al elemento

# 8)
dobles = [] #creo la lista vacia
dobles.append(5*2) #agrego los valores solicitados multiplicando por 2, porque debia ingresar el doble del valor pedido.
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# 9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo") #agrego usando el indice 2, osea el tercer elemento que es otra lista y le agrego jugo con append()
compras[1][1] = "tallarines" #selecciono el segundo elemento del segundo elemento y le reasigno el valor de tallarines
compras[0].remove("pan") #selecciono el primer elemento y remuevo un elemento que se llame pan
print(compras)

# 10)
lista_anidada = [[15],[True],[[25.5],[57.9],[30.6]],[False]] #Creo la lista con los elementos solicitados segun su posicion.
print(lista_anidada)