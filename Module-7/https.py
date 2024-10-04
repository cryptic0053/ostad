import http.client

conn=http.client.HTTPSConnection("kuet.ac.bd")
conn.request("GET",'/')

response=conn.getresponse()

print(response.status)
print(response.headers)
print(response.read())