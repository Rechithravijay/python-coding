print("operation on tuple and list")
my_tuple=( 1, 2, 3)
my_list=[4, 5, 6]
print(my_tuple[0])
print(my_list[1])
my_list[2]=7
print(my_list)
print(my_tuple[1:3])
print(my_list[0:2])
new_tuple=my_tuple+(4,5)
print(new_tuple)
new_list=my_list+[6,7]
print(new_list)
print(len(my_tuple))
print(len(my_list))
print(2 in my_tuple)
print(8 in my_list)
my_list.sort()
print(my_list)
