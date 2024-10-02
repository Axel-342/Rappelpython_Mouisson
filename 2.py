nombre = float(input("saisissez votre nombre "))
if nombre > 0 :
    print("votre nombre est positif")
elif nombre < 0:
    print("votre nombre est négatif")
else :
    print("votre nombre est nul")#

i = 1
while i <= 5:
    print(i)
    i=i+1

somme = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        somme = somme + i
    i = i+1
print(somme)