import requests
import json 

res = requests.get("https://jsonplaceholder.typicode.com/todos")
var = json.loads(res.text)
count = 0 
for i in var:
    if i["completed"] == True:
        b = i["userId"]
        print(b)
                
        
           
#       if i["userId"] == 1:
#           count = count + 1
#print(count)

     
        
        

        
