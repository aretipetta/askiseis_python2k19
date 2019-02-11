 #Python toe
import random
pinakas=[0,1,2,3,4,5,6,7,8]
i=0
tmp1=0
tmp2=0
print (pinakas[0] , pinakas[1] , pinakas[2])
print (pinakas[3] , pinakas[4] , pinakas[5])
print (pinakas[6] , pinakas[7] , pinakas[8])

def A(s,s1,s2,s3):
     if s==pinakas[s1] and s==pinakas[s2] and s==pinakas[s3]:
        return True
#elegxei tous sunduasmous pou kerdizoun
def B(s):
    if A(s,0,1,2):
        return True
    if A(s,3,4,5):
        return
    if A(s,6,7,8):
        return True
    if A(s,0,3,6):
        return True
    if A(s,1,4,7):
        return True
    if A(s,2,5,8):
        return True
    if A(s,0,4,8):
        return True
    if A(s,2,4,6):
        return True

#o megistos arithmos epanallipseon einai < 4 giati o upologistis paizei "tautoxrona" me ton xristi
#kai epipleon oso den uparxei nikitis to paixnidi sunexizetai
while i<4 and tmp1==0 and tmp2==0:
    i +=1
    #zitaei na dothei arithmos efoson den uparxei nikitis
    if tmp1==0 and tmp2==0:
        a = int(input ("give a number: "))
        #elegxei an kerdizei o xristis
    if B("x"):
        tmp1=1
        break;
    #elegxei gia kenes theseis ston pinaka tis trilizas 
    #o upologistis paizei akrivos meta ton xristi
    if pinakas[a]!= "x" and pinakas[a]!= "o":
        pinakas[a]="x"
        #elegxei an kerdizei o xristis
        if B("x"):
            tmp1=1
            break;
        #epilegei o upologistis tuxaio arithmo...
        b = random.randint(0,8)
        found = "no"
        #kai elegxei an einai diathesimi auti i kinisi
        while found=="no":
            if pinakas[b] !="x" and pinakas[b]!= "o":
                pinakas[b]="o"
                found = "yes"
                #elegxei an kerdizei o upologistis efoson mporei na kanei tin epano kinisi...
                if B("o"):
                    tmp2=1
                    break;
            #allios dialegei allon tuxaio arithmo mexri na vrei diathesimo        
            else:
                b = random.randint(0,8)
        #ektuponei ton pinaka se kathe guro tou paixnidiou
        print (pinakas[0] , pinakas[1] , pinakas[2])
        print (pinakas[3] , pinakas[4] , pinakas[5])
        print (pinakas[6] , pinakas[7] , pinakas[8])
    #se periptosi pou o xristis den epileksei diathesimo arithmo epanalamvanei ti diadikasia
    else:
        found2="no"
        while found2=="no":
            a=int(input("give another number: "))
            if pinakas[a]!="x" and pinakas[a]!="o":
                pinakas[a]="x"
                found2="yes"
                if B("x"):
                    tmp1=1
                    break;
                b = random.randint(0,8)
                found1="no"
                while found1=="no":
                    if pinakas[b]!="x" and pinakas[b]!="o":
                        pinakas[b]="o"
                        found1="yes"
                        if B("o"):
                            tmp2=1
                            break;
                if tmp2==1:
                    break;

        print (pinakas[0] , pinakas[1] , pinakas[2])
        print (pinakas[3] , pinakas[4] , pinakas[5])
        print (pinakas[6] , pinakas[7] , pinakas[8])


print (pinakas[0] , pinakas[1] , pinakas[2])
print (pinakas[3] , pinakas[4] , pinakas[5])
print (pinakas[6] , pinakas[7] , pinakas[8])
#vriskei ton nikiti an uparxei
if tmp1==0 and tmp2==0:
    print("there is no winner!")
elif tmp1==1 and tmp2==0:
    print("the winner is x!")
elif tmp1==0 and tmp2==1:
    print ("the winner is o!")
else:
    print ("there is no winner!")