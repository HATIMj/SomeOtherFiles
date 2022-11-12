import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://crudcrud.com/api/b33c25b6c817439f804ca2c573e91ab',data = pload)
print(r.json())