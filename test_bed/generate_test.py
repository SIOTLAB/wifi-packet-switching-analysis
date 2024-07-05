import json
import time
tests={}
config_options=["iprules","fast_path","xdp","rps"]
tests["Env_config"]={}
env=tests["Env_config"]
count=1
env = {}
for i in range(4):
    binary_str = format(i, '02b')
    a,b = map(int, binary_str)
    env[str(count)] = {
        "defer_on": a,
        "seperate_cpu": b
        # "double_budget": c,
    }
    count += 1

flow_options=["ip_address","port"]
ips=["172.16.11.3","172.16.11.3","172.16.10.2","172.16.10.2"]
port=[400,500,400,500]
combination=[ips,port]
duration=40
through=[100,500,850]
# parallel=[1,5,10,20]
count=1
tests["Test_config"]={}
test=tests["Test_config"]
for l in through:
    for i in range(4):
        test[str(count)]={}
        temp=test[str(count)]
        temp["duration"]=duration
        temp["throughput"]=l
        for s in range(2):
            temp[flow_options[s]]=combination[s][i]
        count+=1
Tests={}
for i,c in env.items():
    for j,b in test.items():
        Tests[f"Test_{i}_{j}"]={}
        Tests[f"Test_{i}_{j}"]["Env_config"]=c
        Tests[f"Test_{i}_{j}"]["Test_config"]=b
with open("./tests.json","w+") as f:
    json.dump(Tests,f,indent=4)
            



