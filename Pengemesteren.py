import time

print("Velkommen til Pengemesteren! I dette spillet vil kun de beste gamblerene vinne!")
time.sleep(5)
print("Reglene er som følger: \n Du begynner med 200 kr. Målet med spillet er å nå 1000 kr før spillets slutt. Går du tom har du tapt.")
time.sleep(3)
print("Pengemesteren består av 10 runder, og du har i hver runde mulighet til å tjene penger.")
time.sleep(3)


print("Er du klar? \n Runde 1 er i ferd bed å begynne")
a=int(200)
time.sleep(3)

if a==1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

første=input("Du møter en mann som utfordrer deg til et veddemål. \n Hvis du vinner tjener du 300 kr, hvis du taper mister du hundre. \n Tar du utfordringen?")
if første=="NEI":
    print("Du har avslått tilbudet.")
elif første=="JA":
    print("Du har takket ja til tilbudet.")
    time.sleep(3)
    import random
    for x in range(1,2):
        c=random.randint(1,2)
    if c==1:
        a-=100
        print("Du tapte veddemålet, ny saldo er",a,"kr.")
    elif c==2:
        a+=300
        print("Gratulerer, du vant veddemålet! Ny saldo er",a,"kr")
time.sleep(3)

if a>=1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

andre=input("Du vurderer å kjøpe et flaxlodd for 25 kr. \n Vil du kjøpe loddet?")
if andre=="NEI":
    print("Du har avslått salget. Din saldo er",a,"kr")
elif andre=="JA":
    print("Du har takket ja til salget.")
    time.sleep(3)
    import random
    for x in range(1,3):
        d=random.randint(1,3)
    if d==1:
        a-=25
        print("Du vant dessverre ikke på flaxloddet, ny saldo er",a,"kr.")
    elif d==2:
        a+=25
        print("Gratulerer, du vant 50 kr på flaxloddet! Ny saldo er",a,"kr")
    else:
        a+=75
        print("Gratulerer, du vant 100 kr på flaxloddet! Ny saldo er",a,"kr")
time.sleep(3)

if a>=1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

tredje=input("En venn ber om å låne 80 kr. Han sier han vil gi tilbake det dobbelte. \n Stoler du på vedkommende?")
if tredje=="NEI":
    print("Du er gnien og låner ikke bort penger til vennen din. Din saldo er",a,"kr.")
elif tredje=="JA":
    print("Du lånte bort pengene og håper du får dem igjen.")
    time.sleep(3)
    import random
    for x in range(1,2):
        e=random.randint(1,2)
    if e==1:
        a-=80
        print("Du fikk ikke tilbake pengene, ny saldo er",a,"kr.")
    elif e==2:
        a+=160
        print("Vennen din betalte tilbake raskt og var veldig glad du hjalp ham. Ny saldo er",a,"kr")
time.sleep(3)

if a==1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

fjerde=input("En venn sier du kan kjøre bilen hans og hente ham og tjene 100 kr. \n Men du har ikke lappen. Tar du sjansen?")
if fjerde=="NEI":
    print("Du tar ikke sjansen.")
elif fjerde=="JA":
    print("Du henter vennen din.")
    time.sleep(3)
    import random
    for x in range(1,2):
        f=random.randint(1,2)
    if f==1:
        a-=250
        print("Politiet tok deg og du fikk en saftig bot på kr 250, ny saldo er",a,"kr.")
    elif f==2:
        a+=100
        print("Heldigvis tok ikke politiet deg, du hentet vennen og tjente 100kr. Ny saldo er",a,"kr")
time.sleep(3)

if a==1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

femte=input("Du er ute på tur og kommer til et kryss. Her kan du velge mellom en grusvei eller en sti. \n Vil du gå grusveien?")
if femte=="NEI":
    print("Du valgte stien.")
    time.sleep(3)
    a+=45
    print("På stien finner du 45 kr, heldige deg! Ny saldo er",a,"kr")
elif femte=="JA":
    print("Du valgte grusveien.")
    time.sleep(3)
    a-=50
    print("På grusveien går du forbi noen skumle folk som robber deg for 50 kr. Heldigvis gjemte du resten av pengene i skoen din. \n Ny saldo er",a,"kr.")
time.sleep(3)

if a==1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")

sjette=input("Liverpool skal spille hjemmekamp mot Chelsea, og du kan tippe 100 kr på kampens utslag. Valgene er uavgjort (U), hjemmeseier (H), eller borteseier (B). \n Hva tipper du?")
if sjette=="U":
    print("Du tipper uavgjort.")
    time.sleep(3)
    import random
    for x in range(1,2):
        g=random.randint(1,2)
    if g==1:
        a-=100
        print("Kampen ble ikke uavgjort, ny saldo er",a,"kr.")
    elif g==2:
        a+=200
        print("Gratulerer, kampen ble uavgjort! Ny saldo er",a,"kr")
elif sjette=="B":
    print("Du tipper at Chelsea vinner.")
    time.sleep(3)
    import random
    for x in range(1,2):
        g=random.randint(1,2)
    if g==1:
        a-=100
        print("Chelsea tapte, ny saldo er",a,"kr.")
    elif g==2:
        a+=200
        print("Gratulerer, Chelsea vant! Ny saldo er",a,"kr")
elif sjette=="H":
    print("Du tipper at Liverpool vinner.")
    time.sleep(3)
    import random
    for x in range(1,2):
        g=random.randint(1,2)
    if g==1:
        a-=100
        print("Liverpool tapte, ny saldo er",a,"kr.")
    elif g==2:
        a+=200
        print("Gratulerer, Liverpool vant! Ny saldo er",a,"kr")
time.sleep(3)

if a==1000:
    print("Gratulerer, du er en ekte pengemester!")
if a<=0:
    print("Bedre lykke neste gang.")