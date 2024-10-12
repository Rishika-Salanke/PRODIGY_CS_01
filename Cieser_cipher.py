"""
text='a' 
result=ord('a')+1
print(chr(result))
"""

def encrypt(text,shift):
    result=""
    for i in text:
        if i.isalpha():
            if i.isupper():
               cipher=chr((ord(i)-ord('A')+shift)%26+ord('A')) 
               #%26 is used to wrap around 
               #and keep the letters within range of 26
            elif i.islower():
               cipher=chr((ord(i)-ord('a')+shift)%26+ord('a'))
            result+=cipher
        else:
            result+=i
    print(result)

def decrypt(text,shift):
    result=""
    for i in text:
        if i.isalpha():
            if i.isupper():
               plain=chr((ord(i)-ord('A')-shift)%26+ord('A'))
            elif i.islower():
               plain=chr((ord(i)-ord('a')-shift)%26+ord('a'))
            result+=plain
        else:
            result+=i
    print(result)
        

while(True):
    choice=int(input("select :\n 1. Encryption \n 2. Decryption\n 0.Exit\n"))
    if choice==1:
     text=input("Enter the text\n")
     shift=int(input("Enter the number of shift\n"))
     encrypt(text,shift)
    elif choice==2:
     text=input("Enter the text\n")
     shift=int(input("Enter the number of shift\n"))
     decrypt(text,shift)
    elif choice==0:
       break