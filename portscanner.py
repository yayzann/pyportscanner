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

confirmGrab = input('Would you like to grab banners? (y/n)')

if confirmGrab == 'y':
    print('Grabbing banners now...')
    s = socket.socket()
    s.settimeout(2)
    s.connect((target, 80))
    s.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
    banner = s.recv(1024)
    print("\n"+banner.decode(errors='ignore')+"\n Good luck pwning!")
    s.close

else:
    print('Good luck pwning!')