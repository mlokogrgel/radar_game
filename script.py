import random
import sys
X=40
Y=40

RANGE=10
TRESURE_COUNT=3
def simplyfi_list(list_):
    copy=[]
    L=[]
    for i in list_ :
        copy.append(i)
    while len(copy)>0:
        for i in copy:
            if type(i)== list and len(i)==2:
                L.append(i)
                copy.remove(i)
            else:
                for I in i :
                    copy.append(I)
                copy.remove(i)
                
    return L          

def copy_list(list_) :
    copy=[] 
    for i in list_:
        copy.append(i)
    return copy
      
def convert_to_int(list_) :
    list_copy=[] 
    for i in list_:
        list_copy.append(i)
    for i in range(len(list_copy)) :
        list_copy[i] =int(list_copy[i]) 
    return list_copy
def plus_1(list_) :
    copy=[] 
    for x in list_ :
        try:
            copy.append(x+1)             
        except TypeError:
            copy.append([])
            for y in x:
                copy[-1].append(y+1)
                
    return copy
    
def up(num) :
    if num > int(num)+.5:
        return int(num)+1
    return int(num)        
def vector_lenght(A,B):
    if A==None or B==None:
        return None
    a1,b1=A
    a2,b2=B
    lenght=(a2-a1)*(a2-a1)+(b2-b1)*(b2-b1)
    return (lenght**.5) 
def up(num) :
    if num > int(num)+.5:
        return int(num)+1
    return int(num)


def ask_(question,T_ansver):
    return input(question). lower().startswith(T_ansver)
def make_memory(list_) :
    M=[] 
    for i in list_:
        M.append([])
    return M
        
       
def get_ansver(X,Y):
    dumb=False
    nums="1 2 3 4 5 6 7 8 9 0".split()
    while True:
        wrong=False 
        gess=input("Where do you want to put radar?"). split() 
        
        
        while True:
            if len(gess) >6:
                print("No, please, don't talk to me, just enter the coordinates. ")
                break 
            for i in gess:
                if not i.isdigit():            
                    wrong=True
                    print("Make sure that your coordinates are digits. " ) 
                    break 
            if wrong:
                break        
            
            if len(gess) > 2 :
                print("In case you didn't notice, this is a 2D game so you need exactly TWO coordinates to make this work. ")
                break
            if len(gess) == 1:
                print("Make sure that your coordinates have one space in between. ")
                break
            if int(gess[0]) >500 or int(gess[1]) >500:                
                if dumb:
                    print("Congratulation you find secret ending!") 
                    sys. exit()
                else:
                    print("If you willing to place the radar into the mine field do not count on me." ) 
                    dumb=True
                    break
                    
            if not 0 < int(gess[0]) <= X or not 0 < int(gess[1]) <= Y :
                print("Make sure your coordinates are on play-board")
                break
            
            else:
                gess=convert_to_int(gess)
                return[gess[0]-1,gess[1]-1]  
        
def board_list(X, Y):
    list_=[]
    for i in range(X) :
        list_.append([])
        for s in range(Y) :
            list_[i].append(random.choice(["+ "])) 
    return list_
def osx(X):
    x=X/10
    x1=int(x)
    osx1="  "
    osx2="   "
    nums="1 2 3 4 5 6 7 8 9 0 "       
    for i in range(x1):
        if i<10:
            osx1+=" " 
        osx1+=(" "*18+str(i+1)) 
        if X/10==int(X/10): 
            osx2+=nums   
        else:
            x=str(x)
            cut=int(x[len(x) - 1]) 
            osx2+=nums
            if x1-1==i:
                osx2+=nums[:cut*2]
    return [osx1, osx2]    
def draw_board(list_, X, Y, osx):
    osx1, osx2=osx
    print("%s\n%s" % ( osx1, osx2)) 
    for y in range(Y) :
        string="" 
        space="" 
        if y<9:
            space=" "  
        for x in range(X):
            string+=list_[x][y]
        print("%s%s %s%s"% (space, y+1,string,y+1) )
    print("%s\n%s" % ( osx2, osx1)) 
    
def tresure(X, Y,TRESURE_COUNT,RANGE):
    list_=[[random.randrange(X),random.randrange(Y)]]
    while True:
        #print("M",)
            
        pos=[random.randrange(X),random.randrange(Y)]
        for i in list_:
            if vector_lenght(i, pos)<(3)or pos in list_:
                wrong=True
                break            
            else:
                #print(vector_lenght(i, pos))
                #print(list_)
                wrong=False
        if not wrong:
            list_.append(pos)
            if len(list_)==TRESURE_COUNT:
                break
       
    return list_
def closest_(radar, tresure_list, Y, X, RANGE) :    
    closest_tresure=[100000000,100000000]
    multyple=[]
    
    for tresure in tresure_list:
        if up(vector_lenght(radar, tresure)) <=RANGE:
            multyple.append(tresure)
            if up(vector_lenght(radar, tresure)) <up(vector_lenght(radar, closest_tresure)) :
                closest_tresure=tresure
    
    for i in multyple:
        if up(vector_lenght(radar, i)) !=up(vector_lenght(radar, closest_tresure)) :
            multyple.remove(i)
    if len(multyple)>1:
        print("Warming radar detected %s tresures et same distance!" %(len(multyple)))       
        return up(vector_lenght(radar, closest_tresure)),multyple
    return up(vector_lenght(radar, closest_tresure)),closest_tresure       
def appli_move(list_,move, X, Y, distance, RANGE, tresure_list, closest, MEMORY) :
    num=0
    num_=0
    tf=True
    limit=len(closest)
    if move in tresure_list:
        list_[move[0]][move[1]]="X " 
        return
    else:
        list_[move[0]][move[1]]="R " 
    for y in range(Y) :
            for x in range(X) :
                tile=[x, y] 
                if distance >1000:
                    if up(vector_lenght(tile, move)) <=RANGE:
                        list_[x][y]="n "
                else: 
                    if up(vector_lenght(tile, move)) <distance :
                        if list_[x][y] != "R ":
                            list_[x][y]="n "
                    
                    if up(vector_lenght(tile, move)) ==distance:                            
                        closest1,closest2=closest
                        if type(closest1)==int:
                            closest1=closest
                            closest2=closest
                            limit=1
                        if tile not in simplyfi_list(MEMORY):                            
                            MEMORY[tresure_list.index(closest1)].append(tile)                                                                                                           
                            MEMORY[tresure_list.index(closest1)].append(move)
                            if closest1!=closest2:
                                MEMORY[tresure_list.index(closest2)].append(tile)                                                                                                           
                                MEMORY[tresure_list.index(closest2)].append(move)
                        if tile not in MEMORY[tresure_list.index(closest1)] and tile not in MEMORY[tresure_list.index(closest2)]:
                            list_[x][y]="n "
        
                        elif list_[x][y]=="n ":
                            continue 
                        elif list_[x][y]=="t ":
                            list_[x][y]="T "
                            num_+=1
                            xt=x
                            yt=y
                        elif list_[x][y]=="T ":
                            xT=x
                            yT=y
                            num+=1
                                             
                        elif list_[x][y]=="R ":
                            continue
                        else:
                            list_[x][y]="t "     
    if num_==limit or num==limit:
        MEMORY.remove(MEMORY[tresure_list.index(closest_tresure)])
        
        if list_[x][y]!="X ":               
            list_[x][y]="n "    
        if [xt, yt] in tresure_list:        
            tresure_list.remove([xt, yt])
            list_[xt][yt] ="X "
        else:            
            tresure_list.remove([xT, yT])
            list_[xT][yT] ="X "
    for y in range(Y) :
            for x in range(X) :
                tile=[x, y]
                if list_[x][y] !="+ " and tile not in simplyfi_list(MEMORY) and list_[x][y] !="X ":
                    list_[x][y]="n "
def rules():
    pass

if ask_("Write R to see rules and controls,fi you alredy know them press enter to start the game.","r"):
    print_rules()
while True:
   
    RADAR_COUNT=10
    list_=board_list(X, Y)
    draw_board(list_ , X, Y, osx(X))
    tresure_list=tresure(X, Y, TRESURE_COUNT,RANGE)
    string="" 
     
    MEMORY=make_memory(tresure_list) 
    
    while RADAR_COUNT != 0:
        if len(tresure_list) ==0:
                string="We found them all lets get out of here!"  
                break
        more_then_one=True
        RADAR_COUNT-=1
        move =get_ansver(X, Y)
        distance, closest_tresure=closest_(move , tresure_list, Y, X,RANGE)  
        appli_move(list_,move, X, Y, distance, RANGE, tresure_list, closest_tresure, MEMORY)
        draw_board(list_ , X, Y, osx(X))
        
        if move in tresure_list:
            tresure_list.remove(move)
            if len(tresure_list)!=0:
                print("You found a tresure!(%s of %s)" % (-len(tresure_list)+TRESURE_COUNT, TRESURE_COUNT)) 
            
        if RADAR_COUNT==0:
            if len(tresure_list) ==TRESURE_COUNT:
                string="Lack wasn't on our side. May be next time."
    print("%s\n%s of %s tresures found." % (string,-len(tresure_list)+TRESURE_COUNT, TRESURE_COUNT))  
    if ask_("Do you vant to play egen?\nyes or no: ","n"):
        break 
   
