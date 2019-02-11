#Python Askisi 3 Afairesi Sxolion

def check(a,b): #a=tmp[j] kai b=j
    m=len(a)
    f="no"
    for k in range(b+1,m):
        if k=="#":
            f="yes"
            break;


with open('example.txt','r') as f:
    f1=f.readlines()
    print(f1)
    L=len(f1)
    finish="no"
    while finish=="no":
       L=len(f1)
       #pernaei mia mia tis grammes
       for i in range(0,L):
           tmp=f1[i]
           l=len(tmp)
           count=0
           found="no"
           found2="no"
           #pernaei ena ena ta stoixeia kathe grammis
           for j in range(0,l):
               if tmp[j]=="'" or tmp[j]=='"':
                   count+=1
               elif tmp[j]=="#":
                   #ean vrei '#' elegxei an einai sxolio me to count
                   if count%2==0:
                       #se periptosi pou einai sxolio olokliris grammis
                       if j==0:
                           found="yes"
                           f1.pop(i)
                           break;
                           #ean einai sxolio deksia tou kodika
                       else:
                           found2="yes"
                           f1[i]=tmp[:j]
                           break;
            #vgainei apo tin epanalipsi an exei afairethei to sxolio kai pigainei stin epomeni grammi
           if found=="yes" or found2=="yes":
               break;
        #elegxei an exei oloklirothei o elegxos olon ton grammon
       if found=="no":
           finish="yes"


    print("new f1= ",f1)

#epeidi i askisi zitouse programma exo sumperilavei kai to txt arxeio 