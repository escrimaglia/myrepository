# Meraki API
# By Ed Scrimaglia

import requests
import sys
import json


def getOrganizaciones(_apikey):

    url = "https://api.meraki.com/api/v0/organizations"

    header = {
        "x-cisco-meraki-api-key": _apikey,
        "Content-Type": "application/json",
    }

    try:
        r = requests.get(url, headers=header, timeout=10)
        r.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print("{0} error HTTP GET {1}".format("\n", error))
        sys.exit(1)
    except requests.exceptions.ConnectionError as error:
        print("{0} error HTTP GET {1}".format("\n", error))
        sys.exit(1)

    parsed = json.loads(r.content)

    return parsed


def getNetwoks(_orgId, _apikey):
    url = (
        "https://api.meraki.com/api/v0/organizations/"
        + str(_orgId)
        + "/networks"
    )

    headers = {
        "x-cisco-meraki-api-key": _apikey,
        "Content-Type": "application/json",
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print("{0} error HTTP GET {1}".format("\n", error))
        sys.exit(1)

    parsed = json.loads(r.content)

    return parsed


if __name__ == "__main__":

    apiKey = "xxxxxxxxxxxx"

    orga = getOrganizaciones(apiKey)

    print("respuesta del API Organizations (Json)", json.dumps(orga, indent=2))

    for ele in orga:
        if ele["id"] == 127342:
            orgId = ele["id"]
            networks = getNetwoks(orgId, apiKey)
            print(
                "respuesta del API Networks (Json)",
                json.dumps(networks, indent=2),
            )

            print("Impresion formateada Networks")
            print(
                "-------------------------------------------------------------------------------"
            )
            print(
                "Networks definidas en organizacion {0} {1}".format(
                    str(orgId), "\n"
                )
            )
            redesToPass = []
            for net in networks:
                print("Network Id: {0}".format(net["id"]))
                print("Nombre: {0}".format(net["name"]))
                print("Organizacion: {0}".format(net["organizationId"]))
                print("TimeZone: {0}".format(net["timeZone"]))
                print("Tipo: {0}".format(net["type"]))
                print("-------------------------------------------")
                redesToPass.append(net["id"])

            break
