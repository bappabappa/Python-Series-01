# string
# collection of characters inside single or double quotes

first_name = "bappa \n "
last_name = "saha"
full_name = first_name + " "+last_name
print(full_name)
#Error:

# print(first_name + 3) #TypeError: must be str, not int
print(first_name + "3")
print(first_name+str(3))
print(3+3)
print(str(3)+str(3))
print(first_name *3   )
