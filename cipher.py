'''
    Program: Cipher
    Version: 1.1
    Author : Meghraj Goswami
    Github : github.com/megz15/cipher
'''

def get_key(val,d): 
    for k,v in d.items(): 
        if val == v: 
            return k

Morse = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

Cipher = {'A': 1, 
        'B': 2, 
        'C': 3, 
        'D': 4, 
        'E': 5, 
        'F': 6, 
        'G': 7, 
        'H': 8, 
        'I': 9, 
        'J': 10, 
        'K': 11, 
        'L': 12, 
        'M': 13, 
        'N': 14, 
        'O': 15, 
        'P': 16, 
        'Q': 17, 
        'R': 18, 
        'S': 19, 
        'T': 20, 
        'U': 21, 
        'V': 22, 
        'W': 23, 
        'X': 24, 
        'Y': 25, 
        'Z': 26}

lst=[]
while True:
    choice=int(input('\n\n1. Encode\n2. Decode\n3. Create Cipher\n4. Exit\nYour choice: '))
    if choice==1:
        c=int(input('\n1. Morse\n2. Caesar\n3. Custom\nYour choice: '))
        if c==1:
            txt=input("\nEnter: ")
            for i in txt:
                i=i.upper()
                print(Morse[i],end=' ')
        elif c==2:
            txt=input("\nEnter: ")
            num=int(input('Change by: '))
            for i in txt:
                i=i.upper()
                if Cipher[i]+num>26:
                    a=(Cipher[i]+num)-26
                else:
                    a=Cipher[i]+num
                print(get_key(a,Cipher),end='')
        elif c==3:
            txt=input("\nEnter: ")
            for i in txt:
                i=i.upper()
                print(custom[i],end='')
    elif choice==2:
        c=int(input('\n1. Morse\n2. Caesar\n3. Custom\n4. Dont know?\nYour choice: '))
        if c==1:
            txt=input("\nEnter: ")
            dec=txt.split()
            for i in dec:
                print(get_key(i,Morse),end='')
        elif c==2:
            txt=input("\nEnter: ")
            num=int(input('Change by: '))
            for i in txt:
                i=i.upper()
                if Cipher[i]+num<1:
                    a=26-(Cipher[i]+num)
                else:
                    a=Cipher[i]+num
                print(get_key(a,Cipher),end='')
        elif c==3:
            txt=input("\nEnter: ")
            for i in txt:
                print(get_key(i,custom),end='')
        elif c==4:
            txt=input("\nEnter: ")
            list_change=[]
            for k in range(26):
                for i in txt.upper():
                    if i==' ':
                        continue
                    a = Cipher[i]+k
                    if a>26:
                        a-=26
                    elif a<1:
                        a+=26
                    list_change.append(a)
                list_change.append(' ')
            for i in list_change:
                if i==' ':
                    print('\t',end='')
                    continue
                print(get_key(i,Cipher),end='')
    elif choice==3:
        custom={' ':' '}
        for i in list(Cipher.keys()):
            custom[i]=input('Enter changed letter for '+i+': ')
    elif choice==4:
        break