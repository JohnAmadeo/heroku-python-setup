import requests

dictToSend = {}
res = requests.post('https://whispering-island-32775.herokuapp.com/get_image', 
                    json=dictToSend)
print(res.text)
print(res.json())
