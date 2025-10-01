#inicia as variaveis para o fatorial e o contador
count = 1
fact = 1

#define ate que numero vai o contador, no caso ate 1000
while count<= 1000:
    count += 1
    fact *= count

print(fact)
