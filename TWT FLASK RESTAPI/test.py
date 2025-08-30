import requests

BASE = "http://127.0.0.1:5000"

# data = [{"likes": 10, "views": 1000000, "name": "Vaibhav"},
#         {"likes": 20, "views": 2000000, "name": "Jahnvi"},
#         {"likes": 30, "views": 3000000, "name": "Miesha"},]

# for i in range(len(data)):
#     response = requests.put(BASE + "/video/" + str(i)  ,json = data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + "/video/0" )
# print(response)  
# input()
response = requests.patch(BASE + "/video/2" , json={"views": 5000000 , "likes": 50}) 
print(response.json())