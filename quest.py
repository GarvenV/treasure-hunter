AantalNachtenTent = 2.00 
aantaldageneten = 5.00
aantalnachtenInn  = 3.00 
aantaldagenPaard = 5.00  
tweepersoonsPaard = 8.00 
tent = 8.00 
innbezoek= 4.00
paard = 9.00 
etenperdag = 7.00 

totaalprijs = (AantalNachtenTent*tent*2)+(aantaldagenPaard*tweepersoonsPaard*2)+(aantalnachtenInn*innbezoek*4)+(aantaldageneten*etenperdag)
print (format(totaalprijs,'.2f'))

inversteerder = 1
ranger = 2
genezer = 3
dief = 4


# inversteerder 

sparen =input("kan je goed met geld omgaan j/n")
uitdagingen = input ("durf je een risico te nemen? j/n")
print(uitdagingen)
gulzig = input("kan je zuinig omgaan met geld? j/n")
print (gulzig)
leeftijd = (input("hoe oud ben je?"))
print (leeftijd)
dragen =  input("hoeveel geld kan je meenemen?")
print (dragen)
rekenen = input ("ben je goed met hoofdrekenen? j/n")
print (rekenen)

if sparen == "n" or uitdagingen == "n" or leeftijd  >= 16: 

    print ("helaas is er geen functie open voor inversteerder")    

else:  

    print ("GELUKKIG is er wel functie open voor inversteerder")


# ranger

navigeren = input ('kan je navigeren door de bos? j/n')
sporen = input  ('ben je goed met sporen traceren? j/n') 
leeftijd = input  ('ben je ouder dan 16?')
sneller = input  ('kan je de reis korter maken? j/n')  
kennis = input  ('heb je een goede kennis over de natuur?')
bessen = input ('heb je kennis over bessen? j/n')

if sneller == 'n':
    print ('dat is niet er, je voldoen wel aan de andere eisen. Gefeliciteerd je bent aangenomen Turreen')

else:
    print ('Gefeliciteerd Turreen je bent aangenomen')

#genezer

bessen = input ('heb je kennis van bessen? j/n')
genezen = input ('kan je wonden behandelen? j/n') 
leeftijd = input ('ben je ouder dan 16?') 
snelheid = input ('kan je iemand spoedig behandelen?j/n')
certificaat = input ('ben je hiervoor getraind?')
EHBO = input ('heb je ook ehbo?j/n')

if bessen == 'n':
    print ('dat is niet erg, je voldoet wel aan de andere eisen. Oxana je bent aangenomen als genezer')

else:
    print ('Gefeliciteerd Oxana je bent aangenomen als genezer')

#dief

lockpick =  ('kan je sloten open maken? j/n')
leeftijd = ('ben je ouder dan 16?')
stilheid = ('ben je goed met sluipen? j/n')
militair = ('zat je in de leger?') 
kluis = ('kan je kluisen open maken? j/n')
specialiteit = ('heb je een speciale training ervoor gehad? j/n')

if lockpick == 'n':
    print ('dat is niet erg, je voldoet wel aan de andere eisen. Francis je bent aangenomen aks dief')

else:
    print ('Gefeliciteerd Francis je bent aangenomen als dief')

    
    
koper = 18
zilver = 7
goud = 15

schep = 2.00
lantaren = 4.00 
lampenolie = 11.00 
hengel = 2.00
tinderbox = 4.00 
rugzak = 3.00
touw = 7.00
fakkel = 3.00 
waterzak = 4.00 
halvemeter = touw 

schep = int(input('hoeveel schep heb je nodig?'))
lantaren = int(input ('hoeveel lanteen heb je nodig?'))
lamppenolie = int(input ('hoeveel lampenole heb je nodig?'))
hengel = int(input('hoeveel hengel heb je nodig?'))
tinderbox = int(input('hoeveel tinderbox heb je nodig?'))
rugzak = int(input('hoeveel rugzakken heb je nodig?'))
touw = int(input('hoeveel halve meter heb je nodig?'))
fakkel = int(input('hoeveel fakkel heb je nodig?'))
waterzak = int(input('hoeveel waterzak heb je nodig?'))

while lampenolie > 0:
    koper += 11
    lampenolie -= 1

while touw > 0:
    koper += 7
    touw -= 1
    halvemeter * 7
    
while tinderbox > 0:
    zilver += 4
    tinderbox -= 3

while fakkel > 0:
    zilver += 3
    fakkel -= 1

while koper > 5:
    koper -= 5 
    zilver += 1
    if koper < 5:
        break
     

while zilver > 10:
    zilver -= 10
    goud += 1
    if zilver <10:
        break
    
print (format(koper,".2f"))  
print (format(zilver,".2f"))
print (format(goud,".2f"))

import time
time.sleep(1)

Q1 = input('whats really easy to get into and hard to get out of?')
if Q1 == 'timeout':
    time.sleep(1)
    print ("answer is right")
else:
    print("your answer is wrong")
    quit()

Q2 = input('tom father has three sons jim john and whats the third ones name?')
if Q2 == 'tom':
    time.sleep(1)
    print ("answer is right ")
else:
    print("your answer is wrong")
    quit()

Q3 = input('a girl fell off 20-foot ladder she wasnt hurt why?')
if Q3 == 'safety first':
    time.sleep(1)
    print ("answer is right")
else:
    print("your answer is wrong")
    quit()

kroon = 93 
robijn = 9 
ring = 46.50 
armband = 23.25
aantalrobijn = 3 
aantalring = 6
aantalarmband = 8 
aantalkroon = 1 
aantalpersonen = 4 


totaalschat = (aantalkroon*kroon)+(aantalrobijn*robijn)+(aantalring*ring)+(aantalarmband*armband)/aantalpersonen

discount = ( 20 / 100 ) * totaalschat

print (format(discount,'.2f'))
print (format(totaalschat - discount, '.2f'))


# totaalprijs = (AantalNachtenTent*tent*2)+(aantaldagenPaard*tweepersoonsPaard*2)+(aantalnachtenInn*innbezoek*4)+(aantaldageneten*etenperdag)
# totaalschat = (aantalkroon*kroon)+(aantalrobijn*robijn*3)+(aantalring*ring*6)+(aantalarmband*armband*8)/aantalpersonen

eindresult = (totaalprijs + totaalschat)
print (format(eindresult, '.2f'))