from time import sleep
import socket
ip = input('\n\033[0:36m===>Digite o endereço ALVO-> \033[m')
print('\033[1;35m Scaneando a rede...\033[m')
sleep(0.6)

ports = [21,22,23,25,28,443,80,8080]

for port in ports:
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(0.7)
   codding = client.connect_ex((ip, port))
   if codding == 0:
      print('\033[1;31m*\033[m', port, '\033[2;32mOPEN\033[m')

print('\n\033[0;36m===>SCAN FINALIZADO.\033[m')