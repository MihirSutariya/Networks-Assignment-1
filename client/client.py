import os
import socket
import pickle
import crypto

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='127.0.0.1'
port=7778


s.connect((host,port))    

while True:
    type_inst= input()
    type_inst=type_inst.split()
    s.sendall(pickle.dumps(type_inst))

    if(type_inst[0]=="CWD"):
        directory = s.recv(2048).decode()
        print(directory)

    if(type_inst[0]=="LS"):
        directory_list= pickle.loads(s.recv(2048))
        print(directory_list)

    if(type_inst[0]=="CD"):
        answer = s.recv(2048).decode()
        print(answer)

    if(type_inst[0]=="DWD") :
        answer = s.recv(2048).decode()
        print(answer)

        if(answer=="Sucess"):
            f=open(type_inst[1],"wb")
            f2=open(type_inst[1],"rb")

            l = s.recv(1024)
            f.write(l)
            l2=f2.read(1024)
            while (l2):
                f.write(l)
                l = s.recv(1024)
                l2=f2.read(1024)
            f.close()
            f2.close()
            crypto.rev_encode(type_inst[1])

    if(type_inst[0]=="UPD") :
        if(type_inst[1] in os.listdir(os.getcwd())) and len(type_inst[1].split('.'))>=2:
            print("Sucess")
            crypto.rev_encode(type_inst[1])

            f=open(type_inst[1],"rb")
            l=f.read(1024)
            while l:
                s.send(l)
                l=f.read(1024)
            f.close()
            crypto.rev_encode(type_inst[1])

        else :
            print("Error")