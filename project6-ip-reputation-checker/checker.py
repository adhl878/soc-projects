import csv
import requests


def load_key():
    with open("api_key.txt", encoding="utf-8-sig") as f:
        return f.read().strip()


def check_ip(ip, key):
    r = requests.get(
        "https://api.abuseipdb.com/api/v2/check",
        headers={"Key": key, "Accept": "application/json"},
        params={"ipAddress": ip, "maxAgeInDays": 90},
        timeout=10,
    )
    r.raise_for_status()
    d = r.json()["data"]
    return d["abuseConfidenceScore"], d["totalReports"], d.get("countryCode"), d.get("isp")


def verdict(score):
    if score >= 75:
        return "MALICIOUS"
    if score >= 25:
        return "SUSPICIOUS"
    return "CLEAN"


def main():
    key = load_key()
    with open("ips.txt", encoding="utf-8-sig") as f:
        lines = f.readlines()
    ips = []
    for line in lines:
        line = line.strip()
        if line:
            ips.append(line)
    rows = []
    for ip in ips:
        try:
            score, reports, country, isp = check_ip(ip, key)
            v = verdict(score)
            print(f"{ip:16} score={score:3} reports={reports:4} {country} {v}")
            rows.append([ip, score, reports, country, isp, v])
        except Exception as e:
            print(f"{ip:16} error: {e}")
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ip", "score", "reports", "country", "isp", "verdict"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
