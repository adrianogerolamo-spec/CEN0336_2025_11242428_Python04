list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#compreensao de lista que cria uma lista de tuplas com base no comprimento de cada string
t_list = [(len(i),i) for i in list]
for i in t_list:
    print("{}\t{}\n".format(i[0],i[1]))
