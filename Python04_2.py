#string
taxa = "sapiens, erectus, neanderthalensis"

#imprime a string
print(taxa)

#imprime o segundo caractere da string, pois o indice começa em 0
print(taxa[1])

#imprime o tipo da variavel, no caso string
print(type(taxa))

#converte a string em uma lista, usando a virgula como ponto para separar os argumentos
species = taxa.split(", ")

#imprime a lista
print(species)

#imprime o segundo elemento da lista, pois em uma lista cada valor entre as virgulas é um elemento
print(species[1])

#imprime o tipo da variavel, no caso list
print(type(species))

#imprime a lista ordenada, por padrão, em ordem alfabetica
print(sorted(species))

#define que o fator determinante da ordenação da lista é o comprimento de cada string
print(sorted(species, key=len))
