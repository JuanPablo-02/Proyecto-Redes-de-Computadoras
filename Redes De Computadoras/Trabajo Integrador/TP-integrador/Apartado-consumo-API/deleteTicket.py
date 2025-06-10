import json
import requests


api_url = "http://localhost:58000/api/v1/ticket/"
headers={"X-Auth-Token": None, "Content-Type" : "application/json"}

###MODIFICAR ACA###
ticket = "NC-33-2c46a8d256d14d36944f-nbi"
ticketABorrar = "NC-33-2c46a8d256d14d36944f-nbi"
#######

headers["X-Auth-Token"] = ticket
api_url += ticketABorrar

print(api_url)

resp = requests.delete(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()

if resp.status_code == 200:
    print("Ticket borrado exitosamente.")
elif resp.status_code == 403:
    print("X Auth Ticket no valido")
elif resp.status_code == 404:
    print("Ticket a borrar no valido")
