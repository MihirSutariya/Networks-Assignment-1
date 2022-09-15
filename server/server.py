import crypto
import socket
import os
import pickle
#socket object
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#creating different port for this particular application
port=7778

#bind to the port
s.bind(('',port))

s.listen()

while True:
    conn, addr = s.accept()

    while True:
        arguments = conn.recv(2048)
        if(not arguments):
            conn.close() 
            break
        arguments = pickle.loads(arguments)

        if(arguments[0]=="CWD"):
            conn.sendall(os.getcwd().encode())
        
        if(arguments[0]=="LS") :
            conn.sendall(pickle.dumps(os.listdir(os.getcwd())))

        if(arguments[0]=="CD") :
            try:
                os.chdir(' '.join(arguments[1:]))
                conn.sendall("Sucess".encode())
            except:
                conn.sendall("Error".encode())

        if (arguments[0]=="DWD") :
            if((arguments[1] in os.listdir(os.getcwd())) and len(arguments[1].split('.'))>=2) :
                 conn.sendall("Sucess".encode())
                 crypto.rev_encode(arguments[1])

                 f=open(arguments[1],"rb")
                 l=f.read(2**20)
                 while l:
                    conn.send(l)
                    l=f.read(2**20)
                 f.close()
                 crypto.rev_encode(arguments[1])

            else :
                conn.sendall("Error".encode())

        if arguments[0]=="UPD" :
            f=open(arguments[1],"wb")
            f2=open(arguments[1],"rb")

            l = conn.recv(1024)
            f.write(l)
            l2=f2.read(1024)
            while (l2):
                f.write(l)
                l = conn.recv(1024)
                l2=f2.read(1024)
            f.close()
            f2.close()
            crypto.rev_encode(arguments[1])