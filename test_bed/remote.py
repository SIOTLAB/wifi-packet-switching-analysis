import paramiko
import json
from iperf import parse_iperf3_output
import time
import subprocess
import os
from scp import SCPClient
cmd_sudo = """sudo -s su"""
def establish_ssh_connection(host, username, password=None):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password,timeout=20)
        chan = client.invoke_shell()
        time.sleep(1)
        chan.send(cmd_sudo + '\n')
        return client
    except paramiko.AuthenticationException:
        print("Authentication failed. Check your credentials.")
    except paramiko.SSHException as ssh_ex:
        print("Error occurred while connecting or executing the command:", ssh_ex)
        print(host)
    except Exception as ex:
        print("Error:", ex)
    

import paramiko


def establish_ssh(name):
    with open("./ssh.json") as file:
        data = json.load(file)

    remote_host=data[name]["ip"]
    username=data[name]["uname"]
    password=data[name]["pwd"]
    return establish_ssh_connection(remote_host,username,password)

def close_ssh_connection(ssh_client):
    ssh_client.close()

def start_server(test_name,s):
    with open('tests1.json') as file:
        data = json.load(file)
    test_info=data[test_name]["Test_config"]
    port = test_info["port"]
    print(port)
    if port==700:
        port=9000
    if port ==800:
        port=6000
    try:
        command = f"iperf3 -s -p {port} -J > result.json"
        s.exec_command(command) 


    except paramiko.ssh_exception.SSHException as ssh_exception:
        print(f"SSH Exception: {ssh_exception}")
    except paramiko.ssh_exception.socket.timeout as timeout_exception:
        print(f"Command execution timeout: {timeout_exception}")
    except Exception as general_exception:
        print(f"An unexpected exception occurred: {general_exception}")

def start_client(test_name,s):
    with open('tests.json') as file:
        data = json.load(file)
    results = {}
    
    test_info=data[test_name]["Test_config"]
    ip_address = test_info["ip_address"]
    port = test_info["port"]
    duration = test_info["duration"]
    length=test_info["throughput"]
    # bandwidth=test_info["bandwidth"]
    print("Prepare ready!!!")
    print(port)
    try:
        command = f"iperf3 -c {ip_address} -t {duration} -b {length}M -p {port} -u  -J  > iperf_results_{test_name}.json"

        print(command)
        stdin, stdout, stderr = s.exec_command(command) 
        # iperf_output = stdout.read().decode('utf-8')

    except paramiko.ssh_exception.SSHException as ssh_exception:
        print(f"SSH Exception: {ssh_exception}")
    except paramiko.ssh_exception.socket.timeout as timeout_exception:
        
        print(f"Command execution timeout: {timeout_exception}")
    except Exception as general_exception:
        print(f"An unexpected exception occurred: {general_exception}")
        # Handle other possible exceptions here

    time.sleep(duration)

    # end_time =int(time.time())
    print("Finished iperf3")

def start_cpu_at_rpi(s,test_name):
    # executable_path="rpi"
    print("i am here")
    stdin, stdout, stderr=s.exec_command(f"nohup sudo -S taskset -c 3 /home/rpi2/rpi {test_name}> /dev/null 2>&1 & echo $!")
    pid = stdout.read().decode().strip('utf-8')
    # time.sleep(5)
    print(pid)
    return pid

def start_power_at_empiot1(test_name,s):
    print("i am here for power")
    with open('tests1.json') as file:
        data = json.load(file)
    test_info=data[test_name]["Test_config"]
    duration = int(test_info["duration"])+10
    command=f"sudo ./empiot/source/empiot {test_name}_power.txt -t {duration}"
    print(command)
    # s.exec_command(command)
    try:
        # Execute the command over SSH and capture its output
        stdin, stdout, stderr = s.exec_command(command)

        # Wait for the command to complete and get the exit status
        exit_status = stdout.channel.recv_exit_status()
        print(exit_status)

    except paramiko.SSHException as e:
        error_message = f"SSH error: {str(e)}"
        return None, error_message, -1
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"

def end_cpu(pids,s):
    if pids:
        for pid in pids:
            command=f"kill {pid}"
            s.exec_command(command,timeout=10)
        print("finish kill")

def get_file(s,file_name):

    scp = SCPClient(s.get_transport())

    # Copy the remote file to the local machine
    if os.path.isdir(f"./results/"):
        scp.get(file_name, f"./results/")
    else:
        print("local path for result store is gone")
    # Close the SCP and SSH connections
    scp.close()

def get_folder(s,file_name,local_name):
    scp = SCPClient(s.get_transport())

    # Copy the remote file to the local machine
    scp.get(file_name, local_name)

    # Close the SCP and SSH connections
    scp.close()
# ------------------------

# server1=establish_ssh("server1")
# if server1:
#     print("We make it!!")
#     close_ssh_connection(server1)