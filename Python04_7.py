list = [101,2,15,22,95,33,2,27,72,15,52]
par = 0
impar = 0

#transforma a lista num iteravel e então a ordena em ordem crescente
for n in sorted(iter(list)):
    print(n)
    if n%2 == 0:
        par += n
    else:
        impar += n

print("Soma dos números pares: "+ str(par))
print("Soma dos números ímpares: "+ str(impar))

