age=34#int
print(age)

marks=85.5#float data type
print(marks)

complex_number=10+20j
print(complex_number)

name="Anirban Argha"#String
print(name)

#Sequence type

#list type
city=["Dhaka","Rangpur","Khulna"]#mixed type data are allowed
print(city)

c=["Dhaka",3.4,12]#Duplicate data are allowed
print(c)
print(c[2])

#tuple data type
numbers=("A","B","C","D")
numbers2=("A","B","C","D","B")
print(numbers2)

#range data type
num=range(1,10)
num2=range(0,16,2)
num3=range(10)
print(*num2)
print(*num3)

#Boolean type
isBD=True
print(isBD)

#None type
taka=None
print(taka)

#Mapping type/dict type
person={
    'First_name':'Anirban',
    'Last_name':'Argha',
    'Age':22,
    'isBangladeshi':True
}

print(person['First_name'])
print(person['Last_name'])

#set type
unique_numbers={1,2,3,4,5,3,5,7}#duplicate values are not allowed
print(unique_numbers)#unordered

#frozenset-imutable
unique_numbers=frozenset([1,2,3,4,4,3,5,7,6])
print(unique_numbers)

#data type checking
check=type(taka)
print(check)
