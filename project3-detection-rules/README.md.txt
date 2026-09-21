# Project 3: Detection Rules (SPL)

## Overview
Created three detection rules in Splunk to catch:
1. SSH brute force attacks
2. Phishing emails with malware
3. Credential stuffing attacks

## Rules Included
- SSH Brute Force: Detects 5+ failed logins from same IP
- Phishing Detection: Catches typosquatted domains + malware attachments
- Credential Stuffing: Detects attacks on multiple accounts

See DETECTION_RULES_001.md for full queries and threshold explanations.