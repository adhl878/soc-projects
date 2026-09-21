TICKET ID: SOC-2026-001
DATE: September 21, 2026
SEVERITY: Medium
STATUS: Closed/Resolved

ALERT TITLE: Brute Force SSH Attack Detected

DESCRIPTION:
Multiple failed SSH login attempts detected on Linux server (192.168.2.10).
Attack Duration: ~15 seconds
Total Attempts: 30+

EVIDENCE - Splunk Search:
index=main sourcetype=linux_secure "Failed password"

Log Entries:

2026-09-21T03:20:32.391058+05:30 soc-VMware-Virtual-Platform sshd[8655]: Failed password for invalid user baduser from 127.0.0.1 port 53122 ssh2


2026-09-21T03:20:28.517467+05:30 soc-VMware-Virtual-Platform sshd[8655]: Failed password for invalid user baduser from 127.0.0.1 port 53122 ssh2


2026-09-21T03:18:29.474424+05:30 soc-VMware-Virtual-Platform sshd[8608]: Failed password for invalid user baduser from 127.0.0.1 port 41424 ssh2


2026-09-21T03:18:23.097173+05:30 soc-VMware-Virtual-Platform sshd[8608]: Failed password for invalid user baduser from 127.0.0.1 port 41424 ssh2

ANALYSIS:
1. High frequency of failed attempts (30 in 15 seconds) indicates automated attack
2. All attempts targeting same user (baduser)
3. No successful authentication occurred
4. Attack pattern consistent with brute force attempt

ACTIONS TAKEN:
1. Reviewed authentication logs in Splunk
2. Confirmed brute force attack pattern
3. Verified no unauthorized access
4. Alert resolved

RECOMMENDATION:
Implement SSH rate limiting or fail2ban to prevent brute force attacks.

CLOSED BY: SOC Analyst