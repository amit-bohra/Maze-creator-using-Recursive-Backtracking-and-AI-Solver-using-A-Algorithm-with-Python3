import pygame,time
from pygame.locals import *
import random as rd
import numpy as np
from copy import deepcopy as dp
stacky=[[0,0]]
path=[]
pathcell=[]
pathdict={}
tnode=10#input("total nodes")
for i in range(1,(tnode*tnode)+1):
    pathdict[i]=[]
available={}
celltoval={}
dim=['r','r','c','c']
operator=['+','-','+','-']
tk={}
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
hold=[[tnode-1,tnode-1]]
flag=0
while(running):
    #print(countcell)
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
        '''if countcell==tnode*tnode and len(davailable[(tnode*tnode)])!=1:
            indu-=1
            path.append([stacky[indu+1],stacky[indu]])
            stacky.append(stacky[indu])
            for key,vals in celltoval.items():
                if vals==stacky[indu]:
                    countcell=key ''' 
        if len(a)==0:
            davailable[countcell]=[]
            '''if flag==1:
                flag=0
                davailable[countcell].append([tnode-1,tnode-1])'''
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
    #print(len(covered))
    if(len(covered)==(tnode*tnode)-1) and countcell==1:
        ktmp=list(tk.keys())[-1]
        valu=tk[ktmp]
        del stacky[valu-1:]
        stacky.append([tnode-1,tnode-1])
        path.append([stacky[ktmp],stacky[-1]])
        covered.append([tnode-1,tnode-1])
        

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
    pathdict[i[1]].append(i[0])

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
start=20
startl=5
window=(tnode*start)+(nline*startl)+(2*start) #complete window
win=window-(start+startl)#ignoring 1 space
wi=window-(2*start) #ignoring both space outside
w=wi-(2*startl) # ignoring both side boundaries
w1=wi-(startl) #ignoring 1 boundary


#pathdict={1: [6], 2: [3], 3: [8, 2, 4], 4: [3, 5], 5: [10, 4], 6: [1, 7], 7: [12, 6], 8: [9], 9: [8], 10: [5, 15], 11: [16], 12: [17, 7], 13: [18, 14], 14: [19, 13], 15: [10, 20], 16: [11, 21], 17: [12, 22], 18: [13, 23], 19: [24, 14], 20: [25, 15], 21: [16, 22], 22: [17, 21, 23], 23: [18], 24: [25, 19], 25: [24, 20]}
#pathdict={1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 14], 5: [6, 15], 6: [5, 7], 7: [8, 6], 8: [7], 9: [10, 19], 10: [9, 20], 11: [12, 21], 12: [11, 13], 13: [12, 23], 14: [24, 4], 15: [25, 5], 16: [17, 26], 17: [16, 18], 18: [17, 19], 19: [9, 18], 20: [10, 30], 21: [11, 31], 22: [32], 23: [24, 13], 24: [14, 23], 25: [26, 15], 26: [16, 25], 27: [28, 37], 28: [27, 29], 29: [28, 30], 30: [40, 20, 29], 31: [41, 21], 32: [33, 42, 22], 33: [32, 43], 34: [35], 35: [34, 36, 45], 36: [35, 37], 37: [27, 36], 38: [48], 39: [40, 49], 40: [30, 39], 41: [51, 31], 42: [32, 52], 43: [33, 44], 44: [43, 45], 45: [35, 44], 46: [47], 47: [48, 57, 46], 48: [38, 47], 49: [50, 39], 50: [49, 60], 51: [41, 61], 52: [42, 62], 53: [54, 63], 54: [53, 55], 55: [56, 54], 56: [66, 55], 57: [58, 47], 58: [57, 68], 59: [60, 69], 60: [50, 59], 61: [51, 71], 62: [52, 63], 63: [64, 53, 62], 64: [65, 63], 65: [64], 66: [56, 67], 67: [66, 77], 68: [58, 78], 69: [59, 79], 70: [80], 71: [72, 61], 72: [82, 71], 73: [74, 83], 74: [73, 75], 75: [74, 76], 76: [75, 77], 77: [67, 76], 78: [88, 68], 79: [89, 69], 80: [90, 70], 81: [91], 82: [72, 92], 83: [73, 93], 84: [85, 94], 85: [84, 86], 86: [85, 87], 87: [88, 86], 88: [98, 78, 87], 89: [99, 79], 90: [80, 100], 91: [81], 92: [82, 91, 93], 93: [83, 92], 94: [84, 95], 95: [96, 94], 96: [97, 95], 97: [96], 98: [88, 99], 99: [89, 98, 100], 100: [90, 99]}
import time
time.sleep(2)
#print(pathdict)

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
x=start+startl
y=start+startl
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
            #print('counti',counti)
            tmp=counti-tnode
            if tmp in pathdict.keys():
                if counti in pathdict[tmp]:
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
    rect=pygame.draw.rect(screen,green,(x,y,start,start))
    pygame.display.update()
    countj=0   
pygame.quit()
    
            
    
                        
                    
            
    
            
                
            

    
        
        


