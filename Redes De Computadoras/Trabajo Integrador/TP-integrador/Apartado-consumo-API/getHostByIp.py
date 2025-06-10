import json
import requests


api_url = "http://localhost:58000/api/v1/host/ip-address/"
headers={"X-Auth-Token": None}

###MODIFICAR ACA###
ticket = "NC-25-9d10aef5d2f74d49b29d-nbi"
ipDispositivo = "172.24.2.2"
#######

headers["X-Auth-Token"] = ticket
api_url += ipDispositivo

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()

hostData = response_json

if resp.status_code == 200:
      print("Ip del host: "  , hostData["hostIp"], "\n", 
            "Nombre del host: "  , hostData["hostName"], "\n",
            "Tipo de host: "  , hostData["hostType"], "\n",
            "MAC del host: "  , hostData["hostMac"], "\n",
            "id: "  , hostData["id"], "\n",
            )

      if "vlanId" in hostData:
            print("id de VLAN: ", hostData["vlanId"], "\n")

      print("Ultima actualizacion: "  , hostData["lastUpdated"], "\n",
            "Ping Status: "  , hostData["pingStatus"], "\n", 
            "\n",
            "Direccion IP del network device conectado: "  , hostData["connectedNetworkDeviceIpAddress"], "\n", 
            "Nombre del network device conectado: "  , hostData["connectedNetworkDeviceName"], "\n",
            "Nombre de la interfaz conectada: "  , hostData["connectedInterfaceName"], "\n" 
      )