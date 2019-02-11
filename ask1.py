#Python sumIntervals

import math
def sumIntervals(lista):
    print(lista)
    f="no"
    fin=0
    while f=="no":
        L=len(lista)
        #mazi me tin for-j elegxei ana duo ta diastimata kai an uparksoun allages metaksu auton
        #vgainei apo to 2o loop sunexizontas me ti nea-pleon-lista
        for i in range(0,L-1):
            tmp1=lista[i]
            #pairnei ta akra tou protou diastimatos pou tha sugkrinei
            a=tmp1[0]
            b=tmp1[1]
            brk=0
            for j in range(i+1,L):
                tmp2=lista[j]
                #pairnei ta akra tou deuterou diastimatos pou tha sugkrinei
                c=tmp2[0]
                d=tmp2[1]
                print("a=",a,"b=",b,"c=",c,"d=",d)
                #elegxei oles tis periptoseis me ta akra ton diastimaton
                if L==1:
                    fin=1
                    break;
                if a<c<d<b:
                    lista.pop(j)
                    brk=1
                    break;
                elif c<a<b<d:
                    lista.pop(j)
                    brk=1
                    break;
                elif a<c<b<d:
                    lista.append([a,d])
                    lista.pop(i)
                    brk=1
                    break;
                elif c<a<d<b:
                    lista.append([c,b])
                    lista.pop(j)
                    brk=1
                    break;
                elif a==c and b<d:
                    print("edo prepei na teleiosei kanonika",a,b,c,d)
                    lista.pop(j)
                    brk=1
                    break;
                elif a==c and b>d:
                    lista.pop(j)
                    break;
                elif b==d and a<c:
                    lista.pop(j)
                    break;
                elif b==d and a>c:
                    lista.pop(i)
                    brk=1
                    break;
                elif a==c and b==d:
                    lista.pop(j)
                    brk=1
                    break;
                elif b==d and a<d:
                    lista.append([a,d])
                    lista.pop(j)
                    brk=1
                    break;
                elif b==d and a>d:
                    lista.append([d,a])
                    lista.pop(j)
                    brk=1
                    break;
                elif a==d and c<b:
                    lista.append([c,b])
                    lista.pop(j)
                    brk=1
                    break;
                elif a==d and c>b:
                    lista.append([b,c])
                    lista.pop(j)
                    brk=1
                    break;


            if fin==1:
                f="yes"
                break;
            if brk==1:
                break;
        L=len(lista)
        if brk==0:
            f="yes"
    #elegxei an exei meinei mono ena diastima sti lista
    if L==1:
        x=lista[0]
        y=lista[1]
        #elegxei ta akra gia na vrei to megisto athroisma
        if x>0:
            sum=y-x
        elif y<0:
            sum=math.fabs(x-y)
        elif x<0 and y>0:
            sum=math.fabs(x)+y

    else:
        sum=0
        for i in range(0,len(lista)):
            tmp=lista[i]
            x=tmp[0]
            y=tmp[1]
            if x>0:
                s=y-x
            elif y<0:
                s=math.fabs(x-y)
            elif x<0 and y>0:
                s=math.fabs(x)+y

            sum=sum+s

    A=sum
    return A


print(sumIntervals())
