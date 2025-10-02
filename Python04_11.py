list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in list:
    #metodo .format() permite organizar o output
    print('{:>3}  {:>}'.format(len(i), i))


