# Project Name

Understanding and Enhancing Linux Kernel-based Packet Switching on WiFi Access Points

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage for perf and flamegraph](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This github page provides all testbed scripts and detailed data analysis scripts for Understanding and Enhancing Linux Kernel-based
Packet Switching on WiFi Access Points paper.

## Features

List the main components of this project:
- testbed (performance matrix) : 1.The meassurement process conducted automatelly. 2.The data from different servers retrieved automatically. 3.Testbed runs the first check for data validation. 4.Testbed will restart the testbed from the endpoint or unfinished tests

- Data_analysis: 1. Data analysis process find and use the valid time interval data. 2.Data analysis process will process the data for better visualization

- Figures

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/SIOTLAB/wifi-packet-switching-analysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd wifi-packet-switching-analysis/testbed
    ```
3. add configuration for all servers:
    ```sh
    vim ssh.json
    # add necessary server ip and passwd
    ```
4. start test.
    ```sh
    python3 ./pipeline.py
    ```
5. adjust the parameter of test if necessary

## Usage for perf and flamegraph

1. Use perf to get the data of processor cycles
    ```sh
    perf record -e cycles:k -C 0,1 sleep 10
    ```
2. git clone Flamegraph
    ```sh
    git clone https://github.com/brendangregg/FlameGraph  # or download it from github
    ```
3. get the flamegraph
   ```sh
    perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded
    ./FlameGraph/flamegraph.pl out.perf-folded > perf.svg # view this graph in Firefox or chrome
    ```

## Configuration

1. set Processor CPU affinity 
    ```sh
    cat /proc/interrupts    #check the IRQ number of ethernet or wireless
    sudo su
    echo 2 > /proc/irq/xx/smp_affinity
    ```

2. other configurations that we needed in test
    ```sh
    sudo sysctl -w net.ipv4.ip_forward=1
    sudo iw wlan0 set power_save off
    sudo tc qdisc add dev eth1 root fq_codel
    sudo ethtool -K eth1 generic-segmentation-offload off
    sudo ethtool -K eth1 generic-receive-offload off
    sudo ethtool -K wlan0 generic-segmentation-offload off
    sudo ethtool -K wlan0 generic-receive-offload off
    sudo sysctl -w net.core.netdev_budget=300
    sudo sysctl -w net.core.netdev_budget_usecs=8000
    sudo sysctl -w net.core.dev_weight=64
    ```

3. use perf for l1-dcache invalidation and content-switching
    ```sh
    perf stat -e l1d-cache-invalidation -C 0,1 sleep 10
    perf stat -e context-switches -C 0,1 sleep 10
    ```
## Contacts
Shiqi Zhang  szhang9@scu.edu
Mridul Gupta  magupt@scu.edu
Behnam Dezfouli bdezfouli@scu.edu
 