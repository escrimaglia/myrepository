from netmiko import ConnectHandler


def connectToDevice():
    fromDevice = ConnectHandler(
        device_type="cisco_ios",
        ip="10.54.153.7",
        username="admin",
        password="logicalis",
    )
    try:
        output = fromDevice.send_command("show running-config")
    except ConnectionError as error:
        print("{0} error de conexión".format(error))

    return output.splitlines()


if __name__ == "__main__":
    for linea in connectToDevice():
        print("{}".format(linea))

