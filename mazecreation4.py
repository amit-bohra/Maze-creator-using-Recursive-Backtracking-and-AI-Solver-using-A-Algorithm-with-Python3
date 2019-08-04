import pygame,time
from pygame.locals import *
import random as rd
import numpy as np
from copy import deepcopy as dp
import math

goal=1
shuru=1
stacky=[[0,0]]
path=[]
pathcell=[]
pathdict={}
tnode=5#input("total nodes")
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

lines={0:['up','down','left','right']}                        
#print(davailable)
stack=[1]
i=1
covered=[1]
flag=0
listy=[True, True] # zigzag path more false more zigzag
trying=True #random starting node
if trying==True:
    q=rd.choice(range(2,tnode+1))
    stack=[q]
    covered=[q]
    i=q
while len(stack)!=0:
    '''print(stack)
    print(covered)
    print('l',len(covered))'''
    if len(covered)==tnode*tnode:
        break
    tmp=davailable[i]
    a=[x for x in tmp if x not in stack if x not in covered]
    if len(a)==0 :
        temp=stack.pop()
        i=stack[-1]
    else:
        if len(stack)>=2 and len(a)>=2:
            if abs(stack[-1]-stack[-2])==1:
                flag=1
            if abs(stack[-1]-stack[-2])==tnode:
                flag=2
        qemp=i
        i=rd.choice(a)
        r=rd.choice(listy)
        if r==True:
            flag=0
        if flag==1:
            flag=0
            while(abs(i-stack[-1])==1):
                i=rd.choice(a)
        if flag==2:
            flag=0
            while(abs(i-stack[-1])==tnode):
                i=rd.choice(a)        
        stack.append(i)
        if i not in covered:
            covered.append(i)
        ind=davailable[qemp].index(i)
        del davailable[qemp][ind]
        pathcell.append([qemp,i])
    if len(stack)==1:
        break

for i,j in pathcell:
    if i not in pathdict[j]:
        pathdict[j].append(i)
    if j not in pathdict[i]:
        pathdict[i].append(j)

#print(pathdict)

nline=tnode+1
start=((880//(tnode+2))*3)//4
startl=start//3
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
lining=[]
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
yellow=(255,255,0)
countj=0
x=start+startl
y=start+startl
gray     =  (128, 128, 128)
a1=0
b1=0
c1=0
d1=0

center={}

mid=(start)//2
counti=0
for i in range(start+startl,win,start+startl):
    countj=0
    for j in range(start+startl,win,start+startl):
        countj+=1
        cell=counti+countj
        ty=i+mid
        tx=j+mid
        center[cell]=[tx,ty]
        lines[cell]=[i,i+start+startl,j,j+start+startl]
        lining.append([i,i+start+startl,j,j+start+startl])
    counti+=tnode

total=[]
starting=[]
ending=[]

def disupdater(val,shuru,goal):
    global total,starting,ending
    disgoal=int(math.sqrt(((center[goal][0]-center[val][0])**2)+((center[goal][1]-center[val][1])**2)))
    disshuru=int(math.sqrt(((center[shuru][0]-center[val][0])**2)+((center[shuru][1]-center[val][1])**2)))
    total.append(disgoal+disshuru)
    starting.append(disshuru)
    ending.append(disgoal)

turu=1
def pathfinder():
    global pathdict,center,total,starting,ending,shuru,goal,start,screen,black,turu
    apathdict=dp(pathdict)
    disupdater(shuru,shuru,goal)
    opened=[shuru]
    closed=[]
    parent={}
    path=[]
    while True:
        ind=total.index(min(total))
        #print('ind',ind)
        #print('opened',opened)
        #print('total',total)
        #print('closed',closed)
        del total[ind]
        del starting[ind]
        del ending[ind]
        val=opened[ind]
        del opened[ind]
        closed.append(val)
        temp=apathdict[val]
        temp=[x for x in temp if x not in closed]
        counter=0
        while(len(temp)!=0):
            #print('temp',temp)
            valu=temp[0]
            del temp[0]
            counter+1
            opened.append(valu)
            disupdater(valu,shuru,goal)
            parent[valu]=val
        if val==goal:
            #print(closed)
            lastval=closed[-1]
            path.append(lastval)
            while(parent[lastval]!=shuru):
                qt=parent[lastval]
                path.append(qt)
                lastval=qt
                if lastval in pathdict[shuru]:
                    path.append(shuru)
            path.reverse()
            opened=[]
            closed=[]
            parent={}
            total=[]
            starting=[]
            ending=[]
            #disupdater(shuru,shuru,goal)
            turu=shuru
            shuru=goal
            #print(path)
            pathing=[]
            for i in path:
                ax,ay=center[i]
                pathing.append((ax,ay))
            return pathing,path,len(path)
            
            
            
        
        
pathing=[]
pathogen=[]
counting=-1
u1=0
l1=0
flagging=0
purple=(128,0,128)
while(running):
    if len(pathogen)!=0:
        counting+=1
        #print('counting',counting)
        if counting==1:
            flag=1
            #print(turu,shuru)
            u1,de1,l1,re1=lines[turu]
        up,down,left,right=lines[pathogen[counting]]
        if y>up:
            y-=start+startl
        if y<up:
            y+=start+startl
        if x<left:
            x+=start+startl
        if x>left:
            x-=start+startl
        if counting==length-1:
            pathogen=[]
            counting=0
            flagging=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if tnode in range(1,11):
        timer=9
    if tnode in range(11,26):
        timer=20
    if tnode in range(26,51):
        timer=30
    if tnode in range(51,71):
        timer=35
    if tnode>=71:
        timer=50
    clock.tick(timer)
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
    mousex,mousey=pygame.mouse.get_pos()
    counti=0
    for i in range(start+startl,win,start+startl):
        countj=0
        for j in range(start+startl,win,start+startl):
            countj+=1
            cell=counti+countj
            a=j
            c=i
            b=a+start
            d=c+start
            if mousex in range(a,b+1) and mousey in range(c,d+1):
                grect=pygame.draw.rect(screen,gray,(a,c,b-a,d-c))
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        flag=0
                        flagging=0
                        a1=a
                        b1=start
                        c1=c
                        d1=start
                        goal=cell
                        #print(goal)
        counti+=tnode
            #print('i',i,'j',j)
            #print('counti',counti,'countj',countj)
            #print('cell',cell)
            #lines[cell]=[i,i+start+startl,j,j+start+startl]
            #lining.append([i,i+start+startl,j,j+start+startl])
    if shuru!=goal:
        pathing,pathogen,length=pathfinder()
    if len(pathing)!=0 and flagging==1:
        thickness=start//5
        pygame.draw.lines(screen,black,False,pathing,thickness)
    if flag==1:
        pygame.draw.rect(screen,purple,(l1,u1,start,start))
    goalrect=pygame.draw.rect(screen,blue,(a1,c1,b1,d1))
    topline=pygame.draw.rect(screen,red,(start,start,wi,startl))
    bottomline=pygame.draw.rect(screen,red,(start,win,wi,startl))
    leftline=pygame.draw.rect(screen,red,(start,start,startl,wi))
    rightline=pygame.draw.rect(screen,red,(win,start,startl,wi))
    rect=pygame.draw.rect(screen,green,(x,y,start,start))
    pygame.display.update()
    countj=0
    
pygame.quit()
#print(lines)
