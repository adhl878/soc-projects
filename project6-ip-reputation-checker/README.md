\# IP Reputation Checker



Python script that checks IP addresses against the AbuseIPDB API and labels each one CLEAN, SUSPICIOUS or MALICIOUS based on its abuse confidence score. Automates the IP enrichment step of SOC alert triage.



\## How it works

\- Reads IPs from ips.txt (one per line)

\- Queries the AbuseIPDB API for each IP

\- Prints the score, report count, country and verdict

\- Saves all results to results.csv



\## Verdict thresholds

\- 75 and above: MALICIOUS

\- 25 to 74: SUSPICIOUS

\- below 25: CLEAN



\## Usage

1\. pip install requests

2\. Put your AbuseIPDB API key in api\_key.txt

3\. Add IPs to ips.txt

4\. Run: python checker.py



\## Skills demonstrated

Python, REST API usage, threat intelligence enrichment, IOC checking, CSV reporting

