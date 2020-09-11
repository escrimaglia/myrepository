# Metodos API Webex Team
# By Ed Scrimaglia

import json
import requests
from pprint import pprint


def getListRooms(_token):

    url = "https://api.ciscospark.com/v1/rooms"

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-type": "application/json; charset=utf-8",
    }

    r = requests.get(url, headers=headers, timeout=10)

    print(r.status_code)
    print("Lista de rooms webex")
    pprint(r.json())


def getRoomDetails(_token, _roomId):

    url = "https://api.ciscospark.com/v1/rooms/" + _roomId

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-type": "application/json; charset=utf-8",
    }

    r = requests.get(url, headers=headers, timeout=10)

    print(r.status_code)
    print("Detalles del roomId ")
    pprint(r.json())


def getMensajesRoom(_token, _roomId):

    url = "https://api.ciscospark.com/v1/messages?roomId=" + _roomId

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-type": "application/json; charset=utf-8",
    }

    r = requests.get(url, headers=headers, timeout=10)

    print(r.status_code)
    print("Mensajes en el roomId ")
    pprint(r.json())


def getTeamsIam(_token):

    url = "https://api.ciscospark.com/v1/teams"

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-type": "application/json; charset=utf-8",
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as error:
        print("error ", error)

    print(r.status_code)
    print("Webex Teams I am ")
    pprint(r.json())


def writeMessage(_token, _msgRoomId, _msg):

    url = "https://api.ciscospark.com/v1/messages"

    headers = {
        "Authorization": "Bearer " + _token,
        "Content-type": "application/json; charset=utf-8",
    }

    body = {"roomId": _msgRoomId, "text": _msg}

    try:
        r = requests.post(
            url, data=json.dumps(body), headers=headers, timeout=10
        )
        print(r.status_code)
        print("mensaje enviado " + _msg)
        pprint(r.json())

    except requests.exceptions.RequestException as error:
        print(error)

if __name__ == "__main__":
    roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vZjg0OWQ0YzAtODdmYi0xMWU5LWE4MzUtMjk0NTQyMzdiODAx"
    msgRoomId = "Y2lzY29zcGFyazovL3VzL1JPT00vZjg0OWQ0YzAtODdmYi0xMWU5LWE4MzUtMjk0NTQyMzdiODAx"
    token = "XXXXXXXXXXX"
    msg = "proceso MPLS-L3-VPN finalizado"

    getListRooms(token)
    #getRoomDetails(token, roomId)
    #getMensajesRoom(token, roomId)
    #getTeamsIam(token)
    #writeMessage(token,msgRoomId,msg)
