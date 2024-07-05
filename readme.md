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
    '''sh
    vim ssh.json
    '''
4. start test.
    ```sh
    python3 ./pipeline
    ```
5. adjust the parameter of test if necessary
## Usage for perf and flamegraph

## Contacts
Shiqi Zhang  szhang9@scu.edu
Mridul Gupta  magupt@scu.edu
Behnam Dezfouli bdezfouli@scu.edu
 