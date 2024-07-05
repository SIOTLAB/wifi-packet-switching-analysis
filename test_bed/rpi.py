import paramiko
import json
from iperf import parse_iperf3_output
import time
import subprocess
from scp import SCPClient

def establish_ssh_connection(host, username, password=None):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password,timeout=20)
        return client
    except paramiko.AuthenticationException:
        print("Authentication failed. Check your credentials.")
    except paramiko.SSHException as ssh_ex:
        print("Error occurred while connecting or executing the command:", ssh_ex)
        print(host)
    except Exception as ex:
        print("Error:", ex)

def establish_ssh(name):
    with open("./ssh.json") as file:
        data = json.load(file)

    remote_host=data[name]["ip"]
    username=data[name]["uname"]
    password=data[name]["pwd"]
    return establish_ssh_connection(remote_host,username,password)

# rpi = establish_ssh("ap")
# stdin, stdout, stderr=rpi.exec_command("nohup sudo -S /home/ap/rpi > /dev/null 2>&1 & echo $!")
# print("stdout:", stdout.read().decode())
# print("stderr:", stderr.read().decode())
# print(pid)