# SOC Lab - Project 1

## Overview
Built a SOC lab with Splunk and Linux VM to detect SSH brute force attacks.

## Setup
- Windows VM: Splunk Enterprise (SIEM)
- Linux VM: Ubuntu with SSH exposed
- Splunk Universal Forwarder: Collects auth logs from Linux

## Attack Simulation
Generated 30 failed SSH login attempts and detected them in Splunk.

## Alert Generated
See SOC_TICKET_001.md for analysis and ticket.