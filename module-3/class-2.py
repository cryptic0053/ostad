import json

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

cities=("Dhaka","Khulna","Jam")
print(id(cities))
cities=cities=("Dhaka","Khulna")
print(id(cities))
cities=("Dhaka","Khulna","Jam",1,2)
for item in cities:
    print(item)

country={"Bd","Ind","Pak"}
city={"Raj","Dhk","Pak"}
country.add("Nepal")
print(country)
country.update("a","b")
print(country)
country.remove("a")
print(country)
country.pop()
print(country)
country.pop()
print(country)
l=country.union(city)
print(l)
print(country.intersection(city))

bill={
    "Name":"Bill Gates",
    "Age":65,
    "Country":"USA",
    "Occupation":"Business",
    "Gender":"male"
}

bill.update(
    {
        "Age":70,
        "Occupation":"Charity"
    }
)

print(bill.get("Name"))
print(bill["Age"])
print(bill.values())

billJSON=json.dumps(bill)
print(billJSON)


billObj=json.loads(billJSON)
print(billObj)

Peoples=[{
    "name":"A",
    "age":65
},
{
    "name": "B",
    "age": 65
},
{
    "name":"C",
    "age":65
}
]
print(Peoples)
PeopleJSONArray=json.dumps(Peoples)
print(PeopleJSONArray)