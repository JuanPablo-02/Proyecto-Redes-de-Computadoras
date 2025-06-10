import json
import requests

api_url = "http://localhost:58000/api/v1/user"

headers={"X-Auth-Token": None, "Content-Type" : "application/json"}

body_json = {
    "username": None,
    "password": None,
    "authorization" : [
        {"role" : None}
    ]
}

###MODIFICAR ACA###
ticket = "NC-25-9d10aef5d2f74d49b29d-nbi"
username = "prueba100"
password = "prueba"
role = "ROLE_OBSERVER"      ##El rol debe ser uno de los siguientes 3: ROLE_ADMIN - ROLE_OBSERVER - ROLE_INSTALLER
#######

headers["X-Auth-Token"] = ticket
body_json["username"] = username
body_json["password"] = password
body_json["authorization"] = [{"role": role}]

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()

if resp.status_code == 201:
    print("Usuario creado con exito")
else:
    print(response_json["response"]["message"]) 