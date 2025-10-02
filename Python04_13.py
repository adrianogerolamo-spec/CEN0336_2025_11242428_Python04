list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#compreensao de lista que cria uma lista de tuplas com base no comprimento de cada string
t_list = [(len(i),i) for i in list]
for i in t_list:
    #incluida a posicao do elemento na lista
    print("{}\t{}\t{}\n".format(list.index(i[1]),i[0],i[1]))
