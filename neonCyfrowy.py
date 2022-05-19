file = open("przyklad.txt")

napis = ""
najdł = 0
co_najdł = ""
ciąg = 0
co = "DOPISZ"
s = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"Q":0,"P":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
for i in file:
    i = i[:-1]
    tekst = i.split()
    komenda = tekst[0]
    znak = tekst[1]
    if komenda == "DOPISZ":
        napis+=znak
        s[znak]+=1
    elif komenda == "ZMIEN":
        napis.replace(napis[-1],znak)
    elif komenda == "USUN":
        napis = napis[:-1]
    elif komenda == "PRZESUN":
        l = 0
        for x in napis:
            if x == znak:
                wyraz = napis[l]
                if znak == "Z":
                    nowy = "A"
                else:
                    nowy = chr(ord(znak)+1)
                napis.replace(znak[l],nowy)
                break
            l+=1
    if co == komenda:
        ciąg+=1
    else:
        if ciąg>najdł:
            najdł=ciąg
            co_najdł = co
        co = komenda
        ciąg=1
#print(len(napis))
#print(najdł,co_najdł)
#print(s)
#print(sorted(s.values()))
print(napis)



