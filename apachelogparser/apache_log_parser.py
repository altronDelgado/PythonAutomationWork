import re
from collections import Counter
import csv
import argparse

my_parser = argparse.ArgumentParser(description='Reading the log file')
my_parser.add_argument("logfile", help='Please enter the logfile to parse',type=argparse.FileType('r'))
args = my_parser.parse_args()

logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # IP'leri bulur,sayıları bulur.

with args.logfile as f:
    log = f.read()
    ip_list = re.findall(logreg, log)
    with open("ipnewcount.csv","w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_Address", "Count"])
        for a, b in Counter(ip_list).items():
            fwritercsv.writerow([a, b])
