import json
data='{"jojo":2,"mojo":7,"khojo":"False"}'
m=json.loads(data)
data2={
    "isbad":False,
    "cars":["bmw","lamborghini"],
    "age":18
}
k=json.dumps(data2,sort_keys=True)
print(m)