# 平文
PLAIN = input("Enter plantext: ")
#PLAIN = "It is sunny today."
char = list(PLAIN)

# 秘密鍵
KEY = int(input("Enter key: "))

# 以下に、記述してください。
CIPER = []

# listの初期値
#i = 1

#char.replace(" ","space")  # .replaceは、strだけ
for i in range(0,len(char)-1):
    if char[i] != ' ' or char[i] != ',' or char[i] != '.':
        if 96 < ord(char[i]) < 123:
            ASCII = ord(char[i])
            num = ASCII - 97
            num = (num + KEY) % 26
            ASCII = num + 97
            char[i] = chr(ASCII)
        elif 64 < ord(char[i]) < 91:
            ASCII = ord(char[i])
            num = ASCII - 65
            num = (num + KEY) % 26
            ASCII = num + 65
            char[i] = chr(ASCII)
    #elif char[i] == ' ':
    #    CIPER.append(' ')
    #elif char[i] == ',':
    #    CIPER.append(',')
    #elif char[i] == '.':
    #    CIPER.append('.')

# listからstrへの変換
CIPER = ''.join(char)

print(CIPER)



#print(char.index(" "))
#while i < len(char):
#    if  char[i]

#print(PLAIN)
#print(len(PLAIN))
#print(char)
#print(len(char))

#print(ord("a"))print(ord("b"))print(ord("c"))print(ord("x"))print(ord("y"))Iprint(ord("z"))

#for char in PLAIN:
#    ASCII = ord(char)
#    print(ASCII)
#    num = ASCII - 97
#    num = (num + KEY) % 26
#    ASCII = num + 97
#    enc += chr(ASCII)

#print(enc)