import socket
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('pyPORT SCANNER'))

target = input("Please input a target address: ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3306, 3389, 8080]
print('Starting...')
try:
    ip = socket.gethostbyname(target)
except:
    print('Hostname could not be resolved. Please try again.')
    exit()

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} OPEN")
    s.close()
print('All done. Good luck pwning!')