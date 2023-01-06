# 平文
print("Enter plantext >")
PLAIN = input()
char = list(PLAIN)

# 鍵
KEY = int(input("Enter key > "))

# 暗号文
CIPER = []

# 暗号化
for i in range(0,len(char)-1):
    if char[i] != ' ' or char[i] != ',' or char[i] != '.' or char[i] != "'":
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

# listからstrへの変換
CIPER = ''.join(char)

# 表示
print("\nDisplay cipertext > ")
print(CIPER)