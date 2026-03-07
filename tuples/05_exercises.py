tuple1 = tuple()
tuple1 = (10,20,30,40,50)
print(tuple1)

#2
tuple2 = (100,200,300,400,500)

print(tuple2[1])
print(type(tuple2))

#3
tuple3 = (1, 2, 3)
# tuple3[0] = 10
print(tuple3)

#4
tuple4 =  (1, 2, 3, 3, 4, 5, 3)
print(tuple4.count(3))

#5
tuple5 = ("Java", "Python", "JavaScript", "Python")
print(tuple5.index("Python"))

#6
tupla6 = (1,2,3)
tupla7 = (4,5,6)
tupla8 = tupla6 + tupla7
print(tupla8)

#7
tupla9 = (10, 20, 30, 40, 50)
subtupla = tupla9[1:3]
print(subtupla)

#8
colores = ("rojo", "verde", "azul") 
coloresList = list(colores)
coloresList[1] = "amarillo"
coloresTuple = tuple(coloresList)
print(coloresTuple)
print(type(colores))

#9
del coloresTuple 
# print(coloresTuple)

10#
last_tuple = (100, )
print(last_tuple)