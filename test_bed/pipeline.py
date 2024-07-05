from remote import establish_ssh, close_ssh_connection,start_client, start_cpu_at_rpi, end_cpu, get_file, start_power_at_empiot1
from local import parse_data
import time
import threading
import json

folder="rpi2_data2_one_core_onetx"
def start_test(test_name,test_config):
    
    # check the environment
    pids_rpi = []

    server1 = establish_ssh("server1")
    server2 = establish_ssh("server2")
    rpi = establish_ssh("rpi2")
    # try:
    #     empiot1 = establish_ssh("empiot1")
    # except:
    #     print("can't connect to empiot1")
    if server2 and rpi:
        print("SSH connection to server2 and rpi established successfully.")

        # thread1 = threading.Thread(target=start_power_at_empiot1, args=(test_name, empiot1))
        print("power connected")
        ip=test_config["ip_address"]
        
        pids_rpi.append(start_cpu_at_rpi(rpi,test_name))
        time.sleep(5)
        # thread1.start()
        
        if ip=="172.16.11.3":
            thread2 = threading.Thread(target=start_client, args=(test_name, server2))
        else:
            thread2 = threading.Thread(target=start_client, args=(test_name, server1))
        thread2.start()
        thread2.join()
        # thread1.join()
        # print("i am here")
        # print(thread1_result)
        end_cpu(pids_rpi, rpi)
        # if ip=="172.16.11.3":
        #     end_cpu(thread1_result,server1)
        # else:
        #     end_cpu(thread1_result,server2)
        print(f"Test {test_name} started successfully.")

        # get the tests result
        files = ["cpu.txt", "eth_interrupts.txt", "eth.txt", "iwlwifi_interrupts.txt", "softirqs.txt", "wlan.txt"]
        for i in files:
            get_file(rpi, f"./rpi_results/{test_name}_{i}")
            print(f"Retrieved file {i} from rpi successfully.")
        iperf_file=f"iperf_results_{test_name}.json"
        ip=test_config["ip_address"]
        if ip=="172.16.11.3":
            get_file(server2,iperf_file)
        else:
            get_file(server1,iperf_file)
        # get the power
        # get_file(empiot1, f"/home/sq5/{test_name}_power.txt")
        print("Retrieved power file from empiot1 successfully.")

        # close the ssh
        close_ssh_connection(server1)
        close_ssh_connection(server2)
        close_ssh_connection(rpi)
        # close_ssh_connection(empiot1)
        print("SSH connections closed successfully.")
        time.sleep(10)
        
        #manage the data
        parse_data(test_name,folder)
    # plot()

def run_exp():
    with open("./tests.json",'r') as test_file:
        tests=json.load(test_file)
    with open(f"./{folder}/iperf.json",'r') as already_test:
        already=json.load(already_test)
            
    for test_name, configs in tests.items():
        env=configs["Env_config"]
        if env["seperate_cpu"]==0 and env["defer_on"]==0:
            if test_name not in already.keys():
                test_config=configs["Test_config"]
                if test_config["throughput"]!=850 and test_config["ip_address"]!="172.16.11.3":
                    continue
                print(test_name)
                try:
                    start_test(test_name,test_config)
                except KeyboardInterrupt:
                    break
                except:
                    continue

if __name__=="__main__":
    run_exp()