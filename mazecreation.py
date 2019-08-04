import random as rd
from copy import deepcopy as dp
stacky=[[0,0]]
path=[]
available={}
celltoval={}
dim=['r','r','c','c']
operator=['+','-','+','-']
tnode=10#input("total nodes")
countcell=0
for i in range(tnode):
    for j in range (tnode):
        countcell+=1
        tdim=dp(dim)
        toperator=dp(operator)
        celltoval[countcell]=[i,j]
        available[countcell]=[]
        while(True):
            if len(tdim)==0:
                break
            else:
                vd=rd.choice(tdim)
                ind=tdim.index(vd)
                vo=toperator[ind]
                del tdim[ind]
                del toperator[ind]
                ti=0
                tj=0
                #print('i',i,'j',j)
                #print('vd',vd,'vo',vo)
                if vo=='+':
                    if vd=='r':
                        ti=i+1
                        tj=j
                    elif vd=='c':
                        tj=j+1
                        ti=i
                elif vo=='-':
                    if vd=='r':
                        ti=i-1
                        tj=j
                    elif vd=='c':
                        tj=j-1
                        ti=i
                #print(ti,tj)
                if ti in range(tnode) and tj in range(tnode):
                    available[countcell].append([ti,tj])
                    
countcell=0
running=True
ind=0
indu=0
davailable=dp(available)
print(davailable)
print(celltoval)
print(stacky)
flag=0
while(running):
    if len(stacky)==(tnode*tnode):
        break
    for key,vals in celltoval.items():
        if vals==stacky[indu]:
            countcell=key
            break
    if len(davailable[countcell])==0:
        indu-=1
        flag=1
        print('indu2',indu)
        path.append([stacky[indu+1],stacky[indu]])
        print('path',path)
        for key,vals in celltoval.items():
            if vals==stacky[indu]:
                countcell=key
                break
    print('countcell',countcell)
    while True:
        if len(stacky)==(tnode*tnode):
            break
        if len(davailable[countcell])!=0:
            print('stacky',stacky)
            print('countcell',countcell)
            print('davailable[countcell]',davailable[countcell])
            choice=rd.choice(davailable[countcell])
            print('choice',choice)
            i,j=choice
            if len(davailable[countcell])==1:
                print('usme')
                print('len(davailable[countcell])',len(davailable[countcell]))
                if [i,j] in stacky:
                    ind=davailable[countcell].index(choice)
                    del davailable[countcell][ind]
                    indu-=1
                    flag=1
                    print('indu2',indu)
                    for key,vals in celltoval.items():
                        if vals==stacky[indu]:
                            countcell=key
                            break
                    path.append([stacky[indu+1],stacky[indu]])
                    print('path',path)
                    break
                else:
                    ind=davailable[countcell].index(choice)
                    del davailable[countcell][ind]
                    stacky.append(choice)
                    if flag==1:
                        flag=0
                        tmp=indu
                        indu=stacky.index([i,j])
                        print('indu2',indu)
                        path.append([stacky[tmp],stacky[indu]])
                    else:
                        indu=stacky.index([i,j])
                        print('indu2',indu)
                        path.append([stacky[indu-1],stacky[indu]])
                    print('path',path)
                    break
            else:
                print('isme')
                a=[x for x in davailable[countcell] if x not in stacky]
                if len(a)==0:
                    indu-=1
                    flag=1
                    print('indu2',indu)
                    path.append([stacky[indu+1],stacky[indu]])
                    print('path',path)
                    for key,vals in celltoval.items():
                        if vals==stacky[indu]:
                            countcell=key
                            break
                if [i,j] not in stacky:
                    ind=davailable[countcell].index(choice)
                    del davailable[countcell][ind]
                    stacky.append(choice)
                    if flag==1:
                        flag=0
                        tmp=indu
                        indu=stacky.index([i,j])
                        print('indu2',indu)
                        path.append([stacky[tmp],stacky[indu]])
                    else:
                        indu=stacky.index([i,j])
                        path.append([stacky[indu-1],stacky[indu]])
                        print('path',path)
                        print('indu2',indu)
                        for key,vals in celltoval.items():
                            if vals==stacky[indu]:
                                countcell=key
                                break
        else:
            indu-=1
            flag=1
            print('indu2',indu)
            path.append([stacky[indu+1],stacky[indu]])
            print('path',path)
            for key,vals in celltoval.items():
                if vals==stacky[indu]:
                    countcell=key
                    break
            break
    
            
                
            

    
        
        


