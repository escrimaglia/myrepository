from netmiko import Netmiko
import sys
import re

def connectToDevice():
    fromDevice = Netmiko(
        device_type="cisco_ios",
        ip="10.54.153.52",
        username="admin",
        password="cisco1234",
        secret='cisco1234',
        fast_cli = True
    )
    fromDevice.enable()
    return fromDevice

def send_command(device,source_config,cmd=""):
    if source_config == "file":
        try:
            output = device.send_config_from_file(config_file="config.cfg")
        except ConnectionError as error:
            print (f"Error de conexión {error}")
            sys.exit(1)
        except Exception as error:
            print (f" Error netmiko {error}")
            sys.exit(1)

        device.save_config()
        device.disconnect()
        return output
    elif source_config != "file" and type(cmd) == list:
            try:
                output = device.send_config_set(cmd)
            except ConnectionError as error:
                print(f"Error de conexión {error}")
                sys.exit(1)
            except Exception as error:
                print(f" Error netmiko {error}")
                sys.exit(1)

            device.save_config()
            device.disconnect()
            return output
    else:
        try:
            output = device.send_command(cmd)
        except ConnectionError as error:
            print(f"Error de conexión {error}")
            sys.exit(1)
        except Exception as error:
            print(f" Error netmiko {error}")
            sys.exit(1)

        device.disconnect()
        return output


if __name__ == "__main__":
    device = connectToDevice()
    print ("enable mode: ","#" in device.find_prompt())
    if "#" in device.find_prompt():
        source_cmd = ""
        cmd = "show running-config"
        salida_cmd = send_command(device,source_cmd,cmd)
        print (salida_cmd)

        # Expresión regular para buscar interfaces
        # device = connectToDevice()
        # source_cmd = ""
        # cmd = "show running-config"
        # salida_cmd = send_command(device,source_cmd,cmd)
        # output_regex = re.findall(r'^interface.+',salida_cmd,flags=re.M)
        # print (output_regex)
