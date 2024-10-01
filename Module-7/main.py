import json

#python object ---->JSON String

person={
    "Name":"Argha",
    "Age":22,
    "City":"Rajshahi",
    "hasChildren":False,
    "titles":["Engineer","Programmer"]
}
personJSON=json.dumps(person,indent=4)
print(personJSON)

#JSON String ----->Python Object

personJSON='{"Name": "Argha", "Age": 22, "City": "Rajshahi", "hasChildren": false, "titles": ["Engineer", "Programmer"]}'
personObj=json.loads(personJSON)
print(personObj)

# Python Object ----->JSON String+File Write

person={
    "Name":"Argha",
    "Age":22,
    "City":"Rajshahi",
    "hasChildren":False,
    "titles":["Engineer","Programmer"]
}

with open("person.json","w") as personJSONFile:
    json.dump(person,personJSONFile,indent=4)

#JSON FIle Read----->Python Obj--->JSON String

with open("person.json","r") as personObjFile:
    person=json.load(personObjFile)
    print(person["hasChildren"])