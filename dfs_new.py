import pygame,time
from pygame.locals import *
import random as rd
import numpy as np
from copy import deepcopy as dp
stacky=[[0,0]]
path=[]
pathcell=[]
pathdict={}
tnode=6#input("total nodes")
for i in range(1,(tnode*tnode)+1):
    pathdict[i]=[]
county=0
celltoval={}
for i in range(tnode):
    for j in range(tnode):
        county+=1
        celltoval[county]=[i,j]
available={}

dim=['r','r','c','c']
operator=['+','-','+','-']
tk={}
countcell=0
davailable={}
for i in range(tnode):
    for j in range (tnode):
        countcell+=1
        tdim=dp(dim)
        toperator=dp(operator)
        available[countcell]=[]
        davailable[countcell]=[]
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
                    for key,vals in celltoval.items():
                        if vals==[ti,tj]:
                            davailable[countcell].append(key)
                            break
                        
flag=0
stack=[1]
count=1
last=tnode*tnode
covered=[]
hold=0
tmp=0
while(True):
    if len(davailable[count])==0:
        count=stack.pop()
        continue
    r=[x for x in davailable[count] if x not in stack]
    if len(r)!=0:
        a=rd.choice(r)
        if len(r)>1:
            while(a==last):
                a=rd.choice(r)
        if len(covered)!=(tnode*tnode)-1:
            if len(r)==1:
                if a==last:
                    tmp=stack[-1]
                    hold=last
                    ind=davailable[count].index(a)
                    del davailable[count][ind]
                    count=stack.pop()
                    continue
        ind=davailable[count].index(a)
        del davailable[count][ind]
        path.append([count,a])
        covered.append(count)
        count=a
        stack.append(a)
    else:
        count=stack.pop()
    if len(covered)==(tnode*tnode)-1:
        path.append([tmp,hold])
        break



for i in path:
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
start=30
startl=10
window=(tnode*start)+(nline*startl)+(2*start) #complete window
win=window-(start+startl)#ignoring 1 space
wi=window-(2*start) #ignoring both space outside
w=wi-(2*startl) # ignoring both side boundaries
w1=wi-(startl) #ignoring 1 boundary
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
    countj=1
    for i in range(start,(window-(2*(start+startl)))+1,start+startl):
        counti=countj
        countj+=1
        for j in range(start+start+startl,(window-(2*(start+startl)))+1,start+startl):
            counti+=tnode
            tmp=counti-tnode
            if tmp in pathdict.keys():
                if counti in pathdict[tmp]:
                    #print('counti',counti,'tmp',tmp)
                    hor=pygame.draw.rect(screen,white,(i,j,(start+startl),startl))#horizontal
                    #print('green')
    counti=0
    countj=0
    tmp=0
    for i in range(start,(window-(2*(start+startl)))+1,start+startl):
        counti+=1
        for j in range(start+start+startl,(window-(2*(start+startl)))+1,start+startl):
            counti+=1
            tmp=counti-1
            #print('counti',counti,'tmp',tmp)
            #print('i',i,'j',j)
            if tmp in pathdict.keys():
                if counti in pathdict[tmp]:
                    tor=pygame.draw.rect(screen,white,(j,i,startl,(start+startl)))
        #print('dond')
    #print('done')
    topline=pygame.draw.rect(screen,red,(start,start,wi,startl))
    bottomline=pygame.draw.rect(screen,red,(start,win,wi,startl))
    leftline=pygame.draw.rect(screen,red,(start,start,startl,wi))
    rightline=pygame.draw.rect(screen,red,(win,start,startl,wi))
    pygame.display.update()
    countj=0   
pygame.quit()
        
    
    


    
    
