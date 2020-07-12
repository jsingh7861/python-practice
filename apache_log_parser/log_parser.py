###
# Log parser to count quantity of requests to your website from each ip address
###

import re 
from collections import Counter

def apache_log_reader(logfile):
    reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(logfile) as f:
        log = f.read()
        iplist = re.findall(reg,log)
        ip_count = Counter(iplist)
        for k,v in ip_count.items():
            print("IP Address" + " -->" + str(k) + "  " + "Count" + "-->" + str(v))
    

    

if __name__ == "__main__":
    logfile = "/Users/jasvindersingh/Desktop/Python_practice/apache_log_parser/logfile.txt"
    apache_log_reader(logfile)
