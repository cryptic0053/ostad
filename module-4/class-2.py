import os
import csv
import json

with open("demo.text","w") as file:
     print("success")
with open("demo.text","w") as file:
       file.write("hello")
     print("success")
with open("demo.text","r") as file:
     content=file.read()
     print(content)

os.rename("demo.text","new.text")
os.remove("new.text")

os.mkdir("newFolder")
os.rename("newFolder","newNewFolder")
os.rmdir("newNewFolder")

 with open("newFolder/demo.text","w") as file:
        file.write("hello")
        print("success")

 with open("newFolder/demo.text","r") as file:
        content=file.read()
        print(content)

 myResults=[
     ['Name','Subject','Group','Language'],
     ['Aa','CSE','A','English'],
     ['Ab','CSE','B','English'],
     ['Ac','CSE','C','English']
 ]

 with open("report.csv",'w') as file:
     write=csv.writer(file)
     write.writerows(myResults)
     print("Completed")

 DicData={
     "name":"Argha",
     "age":34,
     "city":"Raj"
}
 JSONData=json.dumps(DicData)

 print(JSONData)

 with open('new.json','w') as file:
     json.dump(DicData,file,indent=4)
     print("completed")

 with open('new.json','r') as file:
     DicData=json.load(file)
     print(DicData)





