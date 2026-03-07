set1 = {1,2,3,4,5}
print(set1)
print(type(set1))

set1.add(6)
print(set1)

#3
set1.add(5)
print(set1)

#4
print(3 in set1)

#5
set1.remove(4)
print(set1)

#6
set1.clear()
print(len(set1))

#7
frutas = {"manzana", "naranja", "plátano"}
list_fruits = list(frutas)
print(list_fruits[0])

#8
set2= {1,2,3}
set3= {4,5,6}
set3 = set2.union(set3)
print(set3) 

#9 
set4 = {1,2,3,4}
set5 = {3, 4, 5, 6}
set6 = set4.difference(set5)
print(set6)

#10
my_set = {1,2,3,4,5}
del my_set
print(my_set)