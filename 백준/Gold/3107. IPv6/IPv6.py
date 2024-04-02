import sys
input = sys.stdin.readline

short_ip = input().rstrip()

ips = list(short_ip.split(':'))

if '' in ips:
    while len(ips) < 8 + ips.count(''):
        ips.insert(ips.index(''),'0000')
    while len(ips) > 8:
        ips.remove('')

for ip in range(len(ips)):
    if len(ips[ip]) < 4:
        ips[ip] = '0' * (4 - len(ips[ip])) + ips[ip]
    
print(':'.join(ips))