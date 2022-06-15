# Un nombre est multiple de 3 si le reste de la division de ce nombre par 3 est égal à 0
nombre = int (input("Nombre : "))
reste3 = nombre%3
reste2 = nombre%2
if reste2 == 0 :
 print ("Ce nombre est pair")
elif reste3 == 0 :
 print ("Ce nombre est impair, mais est multiple de 3")
else :
 print ("Ce nombre n'est ni pair ni multiple de 3")
