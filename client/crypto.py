import os

def get_size(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

# plain text
def plain_encode(file):
    return 

def plain_decode(file):
    return 

# Caesar cypher

def cae_encode(file):
    file_name=file.split('.')
    c=open(file_name[0]+"1"+file_name[1],'w')
    f=open(file,"r")

    C=f.read(1)
    while C:
        c.write(chr((ord(C)+2)%256))
        C=f.read(1)

    c.close()
    f.close()
    os.remove('./'+file)
    os.rename('./'+file_name[0]+"1"+file_name[1],'./'+file)


def cae_decode(file):
    file_name=file.split('.')
    c=open(file_name[0]+"1"+file_name[1],'w')
    f=open(file,"r")

    C=f.read(1)
    while C:
        c.write(chr((256+ord(C)-2)%256))
        C=f.read(1)
    c.close()
    f.close()
    os.remove('./'+file)
    os.rename('./'+file_name[0]+"1"+file_name[1],'./'+file)


    

    

# reverse

def rev_encode(file):
    file_name=file.split('.')
    c=open(file_name[0]+"1"+file_name[1],'w')
    f=open(file,"r")

    for line in f:
        words=line.split()

        for i in range(len(words)):
            word=words[i]
            c.write(word[::-1])
            if(i!=len(words)-1):
                c.write(' ')
        
        c.write('\n')



    fsize = get_size(c)
    c.truncate(fsize - 1)
    c.close()
    f.close()
    os.remove('./'+file)
    os.rename('./'+file_name[0]+"1"+file_name[1],'./'+file)