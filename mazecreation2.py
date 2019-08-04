import pygame,time
from pygame.locals import *
import random as rd
import numpy as np
from copy import deepcopy as dp
stacky=[[0,0]]
path=[]
pathcell=[]
pathdict={}
tnode=5#input("total nodes")
for i in range(1,(tnode*tnode)+1):
    pathdict[i]=[]
available={}
celltoval={}
dim=['r','r','c','c']
operator=['+','-','+','-']

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
flag=0
covered=[[0,0]]
tempo=0
while(running):
    print(countcell)
    if len(covered)==(tnode*tnode):
        break
    for key,vals in celltoval.items():
        if vals==stacky[indu]:
            countcell=key
            break
    if len(davailable[countcell])==0:
        for key,vals in celltoval.items():
            if vals==stacky[indu]:
                tempo=key
        indu-=1
        path.append([stacky[indu+1],stacky[indu]])
        stacky.append(stacky[indu])
        for key,vals in celltoval.items():
            if vals==stacky[indu]:
                countcell=key
    else:
        a=[x for x in davailable[countcell] if x not in stacky]
        if len(a)==0:
            davailable[countcell]=[]
            for key,vals in celltoval.items():
                if vals==stacky[indu]:
                    tempo=key
            indu-=1
            path.append([stacky[indu+1],stacky[indu]])
            stacky.append(stacky[indu])
            for key,vals in celltoval.items():
                if vals==stacky[indu]:
                    countcell=key
        else:
            choice=rd.choice(a)
            if choice not in covered:
                covered.append(choice)
            stacky.append(choice)
            tmp=indu
            indu=stacky.index(choice)
            path.append([stacky[tmp],stacky[indu]])
            for key,vals in celltoval.items():
                if vals==stacky[indu]:
                    countcell=key
                if vals==stacky[tmp]:
                    tempo=key

a=0
b=0
for i in path:
    for key,vals in celltoval.items():
        if vals==i[0]:
            a=key
            break
    for key,vals in celltoval.items():
        if vals==i[1]:
            b=key
            break
    pathcell.append([a,b])


for i in pathcell:
    pathdict[i[0]].append(i[1])

tathdict=dp(pathdict)
for key,i in tathdict.items():
    if len(i)<1:
        for j in i:
            pathdict[j].append(key)
    if len(i)==1:
        pathdict[i[0]].append(key)

dpath=dp(pathdict)
for i in dpath.keys():
    pathdict[i]=list(set(dpath[i]))
    
           
nline=tnode+1
start=16
startl=5
window=(tnode*16)+(nline*5)+(2*start) #complete window
win=window-(start+startl)#ignoring 1 space
wi=window-(2*start) #ignoring both space outside
w=wi-(2*startl) # ignoring both side boundaries
w1=wi-(startl) #ignoring 1 boundary


pathdict={1: [6], 2: [3], 3: [8, 2, 4], 4: [3, 5], 5: [10, 4], 6: [1, 7], 7: [12, 6], 8: [9], 9: [8], 10: [5, 15], 11: [16], 12: [17, 7], 13: [18, 14], 14: [19, 13], 15: [10, 20], 16: [11, 21], 17: [12, 22], 18: [13, 23], 19: [24, 14], 20: [25, 15], 21: [16, 22], 22: [17, 21, 23], 23: [18], 24: [25, 19], 25: [24, 20]}
import time
time.sleep(2)
print(pathdict)

pygame.init()
screen=pygame.display.set_mode((window,window))
pygame.display.set_caption('MAZE PROGRAM')
clock=pygame.time.Clock()
running=True
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
countj=0
while(running):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    clock.tick(30)
    screen.fill(black)
    rectangle=pygame.draw.rect(screen,white,(start+startl,start+startl,w1,w1))
    for j in range(start,(window-(2*(start+startl)))+1,start+startl):
        if j!=start:
            tor=pygame.draw.rect(screen,red,(j,start,startl,wi))
    for j in range(start,(window-(2*(start+startl)))+1,start+startl):
        if j!=start:
            hor=pygame.draw.rect(screen,red,(start,j,wi,startl))
    counti=0
    countj=0
    for i in range(start,(window-(2*(start+startl)))+1,start+startl):
        counti+=1
        countj=counti
        for j in range(start,(window-(2*(start+startl)))+1,start+startl):
            if i!=start:
                print('counti',counti)
                tmp=counti-1
                print('tmp',tmp)
                if tmp in pathdict.keys():
                    if counti in pathdict[tmp]:
                        print(tmp,countj)
                        print('I',i,'J',j)
                        tor=pygame.draw.rect(screen,green,(i,j,startl,(start+startl))) 
                        print('blue') 
            if j!=start:
                print('countj',countj)
                tmp=countj-tnode
                print('tmpr',tmp)
                print('path',pathdict.keys())
                print('i',i,'j',j)
                if tmp in pathdict.keys():
                    if countj in pathdict[tmp]:
                        print('r',tmp,countj)
                        hor=pygame.draw.rect(screen,blue,(i,j,(start+startl),startl))#horizontal
                        print('green')
            countj+=tnode
    topline=pygame.draw.rect(screen,red,(start,start,wi,startl))
    bottomline=pygame.draw.rect(screen,red,(start,win,wi,startl))
    leftline=pygame.draw.rect(screen,red,(start,start,startl,wi))
    rightline=pygame.draw.rect(screen,red,(win,start,startl,wi))
    pygame.display.update()
    countj=0   
pygame.quit()
    
            
    
                        
                    
            
    
            
                
            

    
        
        


