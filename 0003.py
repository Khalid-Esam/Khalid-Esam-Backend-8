#list:
my_list=[8,23,45,19,"list",[4,15,22]]
print(my_list[4])
print(my_list[1:3])
print(my_list[5][1])

#set:
my_set={8,23,45,19}
my_set.add(15)
my_set.remove(23)
print(my_set)

#dictionary:
my_dict={
    "f_name":"Khalid",
    "l_name":"Esam",
    "GPA":0.52,
    "Grades":[8,23,45,19]
}
print(my_dict["l_name"])
print(my_dict["Grades"][2])

#tuple:
my_tuple=(8,23,45,19,"Khalid")
print(my_tuple)