import subprocess
import re
import json
from datetime import datetime
def run_iperf3(server_ip, duration=10,port=300):
    command = f"iperf3 -c {server_ip} -t {duration} -p {port}"
    try:
        # Run iperf3 command and capture the output
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error running iperf3 command: {e}")
        return None

def parse_iperf3_output(output):
    # Extract throughput and drop rate from the iperf3 output
    throughput = re.findall(r"([\d.]+ \w+/s)", output)
    drop_rate = re.findall(r"([\d.]+%)", output)
    retry_rate = re.findall(r"\d+\s+Mbits/sec\s+(\d+)", output)

    return throughput, drop_rate,retry_rate

def iperf_test(test_name):
    with open('tests.json') as file:
        data = json.load(file)
    results = {}
    test_info=data["Tests_config"][test_name]
    ip_address = test_info["ip_address"]
    port = test_info["port"]
    duration = test_info["duration"]
    output_file = test_info["out_put_file"]
    name=f"Test_{test_name}"
    current_time = datetime.now().isoformat()
    iperf_output = run_iperf3(ip_address, duration)
    if iperf_output:
        throughput, drop_rate = parse_iperf3_output(iperf_output)
        results[name] = {
            "throughput": throughput,
            "drop_rate": drop_rate,
            "timestamp": current_time
        }
    with open('iperf_results.json', 'w') as output_file:
        json.dump(results, output_file, indent=4)
