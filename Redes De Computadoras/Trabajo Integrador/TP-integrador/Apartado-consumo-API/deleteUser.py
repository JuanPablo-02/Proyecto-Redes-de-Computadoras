import json
import requests

api_url = "http://localhost:58000/api/v1/user/"

headers={"X-Auth-Token": None, "Content-Type" : "application/json"}

###MODIFICAR ACA###
ticket = "NC-39-7ed19e72eb60427abc87-nbi"
username = "prueba100"
######

headers["X-Auth-Token"] = ticket
api_url += username

resp = requests.delete(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()

if resp.status_code == 200:
    print("Usuario Eliminado correctamente")
else:
    print(f"Codigo de error: {response_json["response"]["errorCode"]}")
    print(f"Detalle de error: {response_json["response"]["detail"]}\n")
    print(f"Mensaje de error: {response_json["response"]["message"]}")