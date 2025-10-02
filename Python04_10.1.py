import sys

#indice inicia em 0, porem o valor 0 é o nome do programa, entao utliza-se os indices 1 e 2
n1 = int(sys.argv[1])
#converte-se o valor srt pra int
n2 = int(sys.argv[2])

#necessario somar mais 1 para corrigir o os valores impressos
for i in range(n1,n2+1):
    print(i)
