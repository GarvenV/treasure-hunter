inversteerder = 1
ranger = 2
genezer = 3
dief = 4


# inversteerder 

sparen =input("kan je goed met geld omgaan j/n")
uitdagingen = input ("durf je een risico te nemen? j/n")
print(uitdagingen)
gulzig = print ("kan je zuinig omgaan met geld? j/n")
print(gulzig)
leeftijd = int(input("hoe oud ben je?"))
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