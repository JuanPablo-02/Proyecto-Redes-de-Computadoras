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
username = "prueba22"
password = "prueba"
role = "ROLE_a"      ##El rol debe ser uno de los siguientes 3: ROLE_ADMIN - ROLE_OBSERVER - ROLE_INSTALLER

####### Para cambios de contraseña #######
#oldPassword = "prueba1"
#######

headers["X-Auth-Token"] = ticket
body_json["username"] = username
body_json["password"] = password
body_json["authorization"] = [{"role": role}]

#if oldPassword:
#    body_json["oldPassword"] = oldPassword

resp = requests.put(api_url, json.dumps(body_json), headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()

if resp.status_code == 200:
    print("Usuario modificado con exito")
else:
    print(response_json["response"]["message"])