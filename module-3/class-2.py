
fruits = ["apple", "banana", "cherry"]
print(id(fruits))
print(fruits)
fruits.append("mango")
print(id(fruits))
print(fruits)
fruits.insert(2 ,"orange")
print(fruits)

fruits1 =["apple", "banana", "cherry"]
fruits2 =["apple", "banana", "cherry"]
fruits1.extend(fruits2)
print(fruits1)
fruits1.remove("apple")
print(fruits1)
fruits1.pop()
print(fruits1)
fruits.clear()
print(fruits)
print(fruits1.index("banana"))
print(fruits1.count("banana"))

marks =[100 ,120 ,80 ,90]
marks.sort()
marks.reverse()
print(marks)

for item in marks:
    print(item)
