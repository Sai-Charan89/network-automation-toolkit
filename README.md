# Network Automation & Troubleshooting Toolkit
A lightweight Python toolkit for network engineers to automate common troubleshooting and validation tasks in enterprise environments.

## Overview
This repository contains practical scripts for validating DNS resolution, testing TCP reachability, and parsing firewall logs. It is aimed at supporting faster incident response and repeatable network diagnostics.

## Features
- DNS validation for hostnames
- TCP connectivity testing for IP and port pairs
- Palo Alto firewall deny log parsing
- Simple CLI-based workflow
- Easy to extend for future automation use cases

## Use Cases
- Troubleshooting application connectivity issues
- Verifying DNS resolution during incidents
- Testing whether a service port is reachable
- Reviewing firewall logs for deny events
- Building a foundation for network automation tasks

## Repository Structure
- `dns_checker.py` — resolve a hostname to an IP
- `tcp_checker.py` — test TCP connectivity to a target
- `paloalto_log_parser.py` — extract deny events from log files

## Technologies
- Python
- TCP/IP
- DNS
- Log parsing
- Network troubleshooting

## Future Improvements
- Add support for multiple host checks
- Export results to CSV
- Parse structured firewall log formats
- Add API integrations for firewall platforms
- Add Cisco and Palo Alto operational checks

## Author
Sai Charan Kandunuri

Initial release - Network Automation Toolkit
