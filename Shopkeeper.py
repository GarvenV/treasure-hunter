# Maak een Python programma genaamd shopkeeper.py, dit programma simuleert de blinde winkelier. Hij heeft een speciale manier van zijn winkel runnen. 
# Hij noemt 1 voor 1 zijn zijn producten en vraagt bij ieder product hoeveel de klant er van wilt?* 
# (de lijst met beschikbare producten vindt je in het bestand dat is toegevoegd). Als de winkelier klaar is met zijn lijst geeft hij de totaal prijs in goud
# (met 2 cijfers achter de komma) terug aan de klant.

# * een vraag kan zijn “Hoeveel meter touw wilt u?"

# >0 & <1 koper is 1 koper
# 5 koper is 1 zilver
# 10 zilver is 1 goud
# 24 goud is 1 platinum

# schep 2 goud per stuk - 4 nodig
# lantaren 4 goud per stuk - 1 per tent
# lampenolie 11 koper per eenheid - 1 per lanteren + 1 reserve
# hengel 2 goud per stuk - 2 stuks
# tinderbox 4 zilver per stuk - 3 stuks
# rugzak 3 goud per stuk - 1 per persoon
# touw 7 koper per halve meter - 12 meter
# fakkel 3 zilver stuk - 1 per persoon
# waterzak 4 goud per stuk - 1 per persoon + 1 reserve

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