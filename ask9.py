#python maxSequence
def maxSequence(lista):
    L=len(lista)
    athroismata=list()
    lista2=list()
    #elegxei olous tous sundiasmous athroismaton kai ta kataxorei se mia lista athroismata
    #kathos kai tin upolista sti lista2
    for k in range (0,L-1):
        #ousiastika athroizei 1o+2o,meta 1o+2o+3o... kok 
        l=k+1
        for i in range(k+1,L):
            tmp_sum=0
            tmp_lista=list()
            for j in range(k,l):
                tmp_sum=tmp_sum+lista[j]
                tmp_lista.append(lista[j])

            l=l+1
            athroismata.append(tmp_sum)
            lista2.append(tmp_lista)
    #vriskei to megisto athroisma kai tin antistoixi upolista
    max_sum=athroismata[0]
    upolista=lista2[0]
    n=len(athroismata)
    for i in range(0,n):
        if max_sum<athroismata[i]:
            max_sum=athroismata[i]
            upolista=lista2[i]

    X=[max_sum,upolista]
    return X

#klisi sunartisis

print(maxSequence())
