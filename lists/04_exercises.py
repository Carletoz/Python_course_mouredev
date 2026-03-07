lista = [1, 2, 3, 4, 5]
print(lista)

other_list = [10, 20, 30, 40, 50]
print(other_list[2])

lista.append(6)
print(lista)

other_list.insert(2,15)
print(other_list)


other_list = [10, 20, 30, 30, 40, 50]
other_list.remove(30)
print(other_list)

#6
x = lista.pop(-2)
print(x)
print(lista)

#7
big_list = [100, 200, 300, 400, 500]
big_list.reverse()
print(big_list)

#8 la ordene de manera descendente
list2 = [3, 1, 4, 2, 5]
list2.sort(reverse=True)
print(list2)


#9 
list3 = [1,2,3]
list4 = [4,5,6]
list5 = list3.__add__(list4)
print(list5)

#10
other_list2 = other_list[1:3]
print(other_list2)