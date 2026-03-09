dict1 = {"name": "Carlos", "age":"28", "country":"VE"}

# print(dict1)

#2
print(dict1["name"])

#3
dict1["job"] = "Programador"
print(dict1)

#4
dict1["age"] = 38
print(dict1)

#5
del dict1["country"]
print(dict1)

#6
dict2 = {x:x**2 for x in range(1,6)}
print(dict2)

#7
print("age" in dict1)

#8
print(dict1.keys())

#9
keys = list(dict1.keys())
print(type(keys))

#10
list1 = ["name", "age", "job"]

newDict = dict.fromkeys(list1, "Desconocido")
print(newDict)
