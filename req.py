import requests
'''data={
    "p1":2,
    "p4":666}'''

j=requests.get("https://financialmodelingprep.com")
print(j.status_code)
