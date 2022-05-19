file = open("przyklad.txt")

napis = ""
najdł = 0
co_najdł = ""
ciąg = 0
co = "DOPISZ"
s = {}
for i in range(ord('A'), ord('Z') + 1):
    s[chr(i)] = 0

def get_next_char():
    if znak == "Z":
        return "A"
    return chr(ord(znak) + 1)


for i in file:
    print('i', i)
    i = i[:-1]
    tekst = i.split()
    komenda = tekst[0]
    znak = tekst[1]
    if komenda == "DOPISZ":
        napis+=znak
        s[znak]+=1
    elif komenda == "ZMIEN":
        napis = napis.replace(napis[-1], znak, 1)
    elif komenda == "USUN":
        napis = napis[:-1]
    elif komenda == "PRZESUN":
        index = napis.find(znak)
        if index != -1:
            napis = napis.replace(znak, get_next_char(), 1)
    if co == komenda:
        ciąg+=1
    else:
        if ciąg>najdł:
            najdł=ciąg
            co_najdł = co
        co = komenda
        ciąg=1

    print('napis:', napis)
#print(len(napis))
#print(najdł,co_najdł)
#print(s)
#print(sorted(s.values()))
print(napis)



