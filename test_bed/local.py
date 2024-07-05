import re
import json
import os
import math
cpu_list=["cpu","cpu0","cpu1","cpu2","cpu3"]
eth_inter_list=["36:","37:","sum:"]
# iwl_inter_list=["40:","41:","42:","43:","44:","45:","sum:"]
iwl_inter_list=["53:","54:","55:","56:","57:","58:","sum:"]
# iwl_inter_list=["130:","131:","132:","133:","134:","135:","sum:"]
eth_list=["rx_packets:","tx_packets:"]
irq_list=["NET_TX:","NET_RX:"]

def parse_to_json(txt):
    lines = txt.strip().split('\n')
    json_list = []
    current_time = None
    current_obj = None

    for line in lines:
        if line.startswith('Current time: '):
            if current_obj is not None:
                json_list.append(current_obj)
            current_time = int(re.search(r'(\d+)', line).group(1))
            current_obj = {'Current time': current_time}
        else:
            parts = line.split()
            if len(parts)>0:
                key = parts[0]
                values=[]
                for val in parts[1:]:
                    if val.isdigit():
                        values.append(int(val))
                # values = [int(val) for val in parts[1:]]
                current_obj[key] = values

    if current_obj is not None:
        json_list.append(current_obj)

    return json.dumps(json_list, indent=2)

def calculate_cpu_utilization(json_data):
    cpu_utilizations = {}
    prev_cpu_stats = [None]*5

    for entry in json.loads(json_data):
        current_time = entry["Current time"]
        i=0
        cpu_utilizations[current_time]={}
        if len(entry)!=6:
            continue
        # print(entry)
        for i in range(5):
            cpu_stats = entry[cpu_list[i]]
            if prev_cpu_stats[i] is not None:
                # print(prev_cpu_stats)
                
                prev_idle = prev_cpu_stats[i][2] + prev_cpu_stats[i][5]+prev_cpu_stats[i][6]
                curr_idle = cpu_stats[2] + cpu_stats[6]+cpu_stats[5]

                prev_total = sum(prev_cpu_stats[i])
                curr_total = sum(cpu_stats)

                total_elapsed = curr_total - prev_total
                idle_elapsed = curr_idle - prev_idle
                if total_elapsed==0:
                    break
                cpu_utilization = idle_elapsed / total_elapsed * 100
                cpu_utilizations[current_time][cpu_list[i]]= "{:.2f}".format(cpu_utilization)


            prev_cpu_stats[i] = cpu_stats
    
    return cpu_utilizations

def calculate_eth_interrupts(json_data,eth_inter_list,need_sum,s,t):
    print(eth_inter_list,need_sum)
    cpu_utilizations = {}
    l1=len(eth_inter_list)
    # print(l1)
    prev_cpu_stats = [None]*l1
    for entry in json.loads(json_data):
        # print(entry)
        current_time = entry["Current time"]
        # print(current_time)
        i=0
        cpu_utilizations[current_time]={}
        if need_sum:
            l=l1-1
        else:
            l=l1
        isbreak=False
        for i in range(l):
            try:
                eth_inter_stats = entry[eth_inter_list[i]]
                # if l==2:
                #     print(eth_inter_stats)
            except:
                isbreak=True
                break
            if prev_cpu_stats[i] is not None:
                prev_idle = prev_cpu_stats[i]
                curr_idle = sum(eth_inter_stats[s:t])
                temp=curr_idle-prev_idle
                cpu_utilizations[current_time][eth_inter_list[i]]= temp

            prev_cpu_stats[i] =sum(eth_inter_stats[s:t])
        if isbreak:
            print("yes")
            continue
        if need_sum:
            if prev_cpu_stats[l] is not None:
                temp=0
                for i in range(l):
                    temp+=cpu_utilizations[current_time][eth_inter_list[i]]
                cpu_utilizations[current_time][eth_inter_list[l]]=temp
            else:
                prev_cpu_stats[l] = 1
    return cpu_utilizations

def parse(test_name,file_name,folder):
    if file_name in ["eth_softirqs", "wlan_softirqs"]:
        with open(f"./results/{test_name}_softirqs.txt", 'r') as f:
            file_content = f.read()
    else:
        with open(f"./results/{test_name}_{file_name}.txt", 'r') as f:
            file_content = f.read()
    parsed_json = parse_to_json(file_content)
    cpu_data={}
    if file_name=="cpu":
        cpu_utilization=calculate_cpu_utilization(parsed_json)
        # print(cpu_utilization)
    elif file_name=="eth_interrupts":
        cpu_utilization=calculate_eth_interrupts(parsed_json,eth_inter_list,True,0,1)
    elif file_name=="iwlwifi_interrupts":
        cpu_utilization=calculate_eth_interrupts(parsed_json,iwl_inter_list,True,0,1)
    elif file_name=="eth" or file_name=="wlan":
        cpu_utilization=calculate_eth_interrupts(parsed_json,eth_list,False,0,1)
    elif file_name=="eth_softirqs":
        cpu_utilization=calculate_eth_interrupts(parsed_json,irq_list,False,0,1)
    elif file_name=="wlan_softirqs":
        cpu_utilization=calculate_eth_interrupts(parsed_json,irq_list,False,0,1)
    # elif file_name=="softirqs":
    #     cpu_utilization=calculate_eth_interrupts(parsed_json,irq_list,False,0,4)
    else:
        cpu_utilization=file_content
    cpu_data[test_name]=cpu_utilization
    f.close()
    print("one")
    with open(f"./{folder}/{file_name}.json","r") as f:
        print("four")
        data=json.load(f)
    print("two")
    data[test_name]=cpu_data[test_name]
    with open(f"./{folder}/{file_name}.json","w") as f:
        json.dump(data, f, indent=4)
    print("three")


def parse_power(test_name,folder):
    parts = test_name.split("_")
    x=int(parts[-1])-100
    # Step 1: Read the text file and parse the data
    # with open(f"./results/{test_name}_power.txt", 'r') as file:
    with open(f"./paper/{x}.txt", 'r') as file:
        lines = file.readlines()
    # Step 2: Calculate the power for each row and store in a list
    time_power_dict = {}
    average_power_dict = {}
    for line in lines[1:]:  # Skip the header line
        parts = line.strip().split("\t")
        if len(parts)==6:
            time_sec = int(parts[1])
            current = float(parts[5])
            bus_voltage = float(parts[4])
            power = current * bus_voltage
            if time_sec in time_power_dict:
                time_power_dict[time_sec]['total_power'] +=power
                time_power_dict[time_sec]['count'] += 1
            else:
                time_power_dict[time_sec] = {}
                time_power_dict[time_sec]['total_power'] = power
                time_power_dict[time_sec]['count'] = 1
        elif len(parts)==1:
            end_time=int(parts[0].split(":")[1])
            average_power_dict["end_time"]=end_time

        else:
            continue

    average_power_dict["power"]=[]
    for time_sec, data in time_power_dict.items():
        average_power_dict["power"].append(data['total_power'] / data['count'])
        # average_power_dict[time_sec] = data['total_power'] / data['count']
    average_power_dict["power"]=sum(average_power_dict["power"])/len(average_power_dict["power"])
    with open(f"./{folder}/power.json","r") as f:
        data=json.load(f)
    data[test_name]=average_power_dict
    with open(f"./{folder}/power.json","w") as f:
        json.dump(data, f, indent=4)

def parse_iperf(test_name,folder):
    # print(folder)
    # Step 1: Read the text file and parse the data
    parts = test_name.split("_")
    x=int(parts[-1])
    print(x)
    # Read all lines from the file
    # with open(f"./results/iperf_results.json", 'r') as file:
    #     lines = file.readlines()

    # # Remove the last 11 lines
    # new_lines = lines[:-11]

    # # Write the modified content back to the file
    # with open(f"./iperf_64_rpi_one_core/new_iperf_results.json", 'w') as file:
    #     file.writelines(new_lines)

    with open(f"./results/iperf_results_{test_name}.json", 'r') as json_file:
        
        iperf = json.load(json_file)

        # iperf= json.load(file)
    # print(len(iperf))
    # iperf=iperf[0]
    # Step 2: Calculate the power for each row and store in a list
    throughput_list=[]
    # drop_list=[]
    retry_list=[]
    rtt_list=[]
    rttvar_list=[]
    snd_cwnd_list=[]


    for i in iperf["intervals"]:
        throughput_list.append(i["sum"]["bits_per_second"]//(10**6))
        # retry_list.append(i["sum"]["retransmits"])
        # rtt_list.append(i["streams"][0]["rtt"])
        # rttvar_list.append(i["streams"][0]["rttvar"])
        # snd_cwnd_list.append(i["streams"][0]["snd_cwnd"])
    print("finished reading")

    results = {
            "throughput": throughput_list,
            # "drop_rate": drop_rate,
            # "retry_rate": retry_list,
            # "rtt_list":rtt_list,
            # "rttvar_list":rttvar_list,
            # "snd_cwnd_list":snd_cwnd_list,
            "start_timestamp": iperf["start"]["timestamp"]["timesecs"],
            "end_timestamp":iperf["start"]["timestamp"]["timesecs"]+len(iperf["intervals"])
        }
    print(f"./{folder}/iperf.json")
    with open(f"./{folder}/iperf.json","r") as f:
        data=json.load(f)
    print("success!")
    data[test_name]=results
    print("success!")
    with open(f"./{folder}/iperf.json","w") as f:
        json.dump(data, f, indent=4)


def parse_data(test_name,folder):
    files=['eth_interrupts', 'eth', 'cpu','wlan','iwlwifi_interrupts','eth_softirqs',"wlan_softirqs","iperf"]

    for i in files:
        print(i)
        if i=="test":
            parse_power(test_name,folder)
        elif i=="iperf":
            parse_iperf(test_name,folder)
        else:
            parse(test_name,i,folder)
            print(f"finished_{i}")


def parse_softnet(test_name):
    # Step 1: Read the text file and parse the data
    with open(f"./rpi_results/{test_name}_softnet.txt", 'r') as file:
        lines = file.read()
    # print(lines)
    lines = lines.split('\n')

    # Initialize an empty dictionary to store the results
    result_dict = {}
    current_time = None
    byte_values = []
    first_time=-1
    for line in lines:
        # Check for the "Current time:" line
        if line.startswith("Current time:"):
            # If there is a previous set of byte values, store them in the result dictionary
            if current_time is not None and byte_values:
                if first_time==-1:
                    first_time=int(current_time)
                result_dict[current_time] = byte_values
            # Extract the current time from the line
            current_time = line.split(":")[1].strip()
            # Initialize an empty list for the new set of byte values
            byte_values = []
        else:
            # If it's not a "Current time:" line, process the byte values
            # Split the line and convert hexadecimal values to integers
            byte_values.extend(int(value, 16) for value in line.split() if value)

    # Store the last set of byte values in the result dictionary
    if current_time is not None and byte_values:
        result_dict[current_time] = byte_values
    last_time=int(current_time)
    current_value=result_dict[str(first_time)]
    
    new_result={}
    new_result[str(first_time)]=current_value
    first_time+=1
    while first_time<=last_time:
        temp_data=result_dict[str(first_time)]
        new_data=[]
        for i in range(len(temp_data)):
            new_data.append(temp_data[i]-current_value[i])
        current_value=temp_data
        new_result[str(first_time)]=new_data
        first_time+=1

    with open(f"./data2/softnet4.json","r") as f:
        data=json.load(f)
    print("success!")
    data[test_name]=new_result
    print("success!")
    with open(f"./data2/softnet4.json","w") as f:
        json.dump(data, f, indent=4)
# for i in range(0,10):
#     try: 
#         parse_data(f"Test_12_10{i}","rpi2_data2_different_core_onetx")
#     except:
#         continue