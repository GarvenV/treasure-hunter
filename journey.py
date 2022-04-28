# 3 persoons tent is 8 goud per stuk
# 2 persoons paard 8 zilver per dag 
# 1 inn bezoek 4 zilver per persoon 9 koper per paard
# eten 7 koper per persoon per dag
# 2 nachten in tent  3 nachten in Inn

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