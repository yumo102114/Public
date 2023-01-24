# 平文
print("Enter plantext >")
PLAIN = input()
PLAINchar = list(PLAIN)
#print(PLAINchar)

# 鍵
print("Enter key > ")
KEY = input()
Kchar = list(KEY)
KEYchar = []

# 暗号文
CIPER = []

# 鍵の冗長化
while len(KEYchar) < len(PLAINchar):
    KEYchar += Kchar

# 暗号文の生成
for i in range(len(PLAINchar)):
    ASCII_PLAIN = ord(PLAINchar[i])
    num_PLAIN = ASCII_PLAIN - 97
    ASCII_KEY = ord(KEYchar[i])
    num_KEY = ASCII_KEY - 97
    num_CIPER = (num_PLAIN + num_KEY) % 26
    ASCII_CIPER = num_CIPER + 97
    CIPER.append(chr(ASCII_CIPER))

# listからstrへの変換
CIPER = ''.join(CIPER)

# 暗号文の表示
print("\nDisplay cipertext > ")
print(CIPER.upper())