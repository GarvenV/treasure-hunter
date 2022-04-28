# een grote diamant 27 platinum  1x
# een kroon 93 goud 1x
# een robijn kwart de waarde van de grote diamant 3x
# een ring de helft van de waarde van de kroon 6x
# een armband het gemmiddelde van alle ringen en robijnen samen 8x
# Op de terugweg besluit de groep niet nog meer raadsels op te lossen maar de 55 goud te betalen.
# Als de groep voor de laatste keer wakker wordt is Francis met de grote diamand verdwenen.
# Zoals afgesproken krijgt eerst Turreen, na aftrek van alle kosten, 20% van alles wat overblijft. 
# Wat er dan nog over is wordt eerlijk en gelijkmatig over de groep (inclusief Turreen) verdeeld.


kroon = 93 
robijn = 9 
ring = 46.50 
armband = 23.25
aantalrobijn = 3 
aantalring = 6
aantalarmband = 8 
aantalkroon = 1 
aantalpersonen = 4 


totaalschat= (aantalkroon*kroon)+(aantalrobijn*robijn*3)+(aantalring*ring*6)+(aantalarmband*armband*8)/aantalpersonen

discount = ( 20 / 100 ) * totaalschat

print (format(discount,'.2f'))
print (format(totaalschat - discount, '.2f'))























#percentage = quotient * 100