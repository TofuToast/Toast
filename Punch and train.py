
##########NOTE###########
#REMEMBER to change the "onygame=1" varible if you do not want to go through all the settings.
#   1= game with settings
#   2= only game
#imports
import time,random
#varablies--------------------------------------------
yes=1
level=0
health=5
option=(" ")
choose=(" ")
hit=1
onlygame=1
score=1
#pictures---------------------------------------------
start=('''
|-----------------------------------------|
|			                  |
|			                  |
|     			                  |
|   		                          |
|            Punch or Train               |
|                                         |
|                                         |
|                                         |
|-----------------------------------------|
''')
stand=('''
|-----------------------------------------|
|			                  |
|			     _<▣>_        |
|     _			    | [¤] |       |
|   _[▨]_		    | \|/ |       |
|  /|  /|                   ^ | | ^       |
|  |[_|]		      l	l         |
|  O| O|                                  |
|  /_ /_                                  |
|-----------------------------------------|
''')
train=('''
|-----------------------------------------|
|			                  |
| ■-o-■ ■-o-■      	     _<▣>_        |
|   /_	 /		    | [¤] |       |
|  /[▨]_/		    | \|/ |       |
|   \  |                    ^ | | ^       |
|   [__]		      l	l         |
|   |  |                                  |
|  /_ /_                                  |
|-----------------------------------------|
''')
ppunch=('''
|-----------------------------------------|
|			                  |
|                          0 _<▤>_        |
|                     _	   /\ [¤] \       |
|                   _[▨]_ / | \|/ |       |
|                  /|   |/  ^ / / ^       |
|                 / [__]     _\ \         |
|                 O |  |        /         |
|                  /_ /_                  |
|-----------------------------------------|
''')
mpunch=('''
|-----------------------------------------|
|	       []\	                  |
|		 |	                  |
|    _  ( ) <■>_/		          |
|  _[■]_ \-/[¤]	            	          |
| /|  |/    \|/                           |
| \[__]|    / \		                  |
|  \O \O   /   \                          |
|   \| \| _|  _|                          |
|-----------------------------------------|
''')
pdead=('''
|-----------------------------------------|
|			                  |
|			     _<▣>_        |
|     			    | [¤] |       |
|        		    | \|/ |       |
|                           ^ | | ^       |
| *POOF!*		      l	l         |
|                                         |
|                                         |
|-----------------------------------------|
''')
mdead=('''
|-----------------------------------------|
|			                  |
|			                  |
|     _			                  |
|   _[▨]_		  *POOF!*         |
|  /|  /|                                 |
|  |[_|]		                  |
|  O| O|                                  |
|  /_ /_                                  |
|-----------------------------------------|
''')
gameover=('''
|-----------------------------------------|
|			                  |
|			                  |
|     		                          |
|              GAME OVER    	          |
|                                         |
|  		                          |
|                                         |
|-----------------------------------------|
''')
#modueles---------------------------------------------
def blank():
    print('''

































''')
def start_input(level):
    blank()
    pie=random.randint(1,100)
    if pie==pie<50:
        pie=1
        print("my name is pie")
    else:
        pie=100
    print(start)
    print('Welcome to Punch or Train!')
    time.sleep(1)
    play=input('''
play?
y/n
''')
    if play==("y"):
        print("ok")
        blank()
        level=input('''
choose Level:
1=easy
2=hard
3=extreme
please type Level number:''')
        level=str(level)
        return(level)
    else:
        blank()
        print("bye")
        exit()
def game(level,health,hit,yes,score):
    level=level+4
    while health>0:
        #main
        time.sleep(0.5)
        blank()
        print(stand)
        print("a monster appered!  it has ",level,"hearts.")
        print("you have:",health,"hearts")
        print("you have",hit,"punch power")
        print("score:", score)
        choose=input("punch=p, train=t, surrender=s")
        if onlygame==0:
            print(yes)
        if choose=="t":#train
            time.sleep(0.5)
            blank()
            print(train)
            time.sleep(1)
            yes=(random.randint(1,2))
            if yes==1:#monster hit?
                blank() 
                print(mpunch)
                health=health-random.randint(1,5)
                time.sleep(0.5)
            hit=hit+1
            health+2
        if choose=="p":#punch
            time.sleep(0.5)
            blank()
            print(ppunch)
            level=level-hit
            yes=(random.randint(1,2))
            if yes==1:#monster hit?
                blank() 
                print(mpunch)
                health=health-random.randint(1,5)
                time.sleep(0.5)
        if choose=="s":
            exit()
        if choose=="pie is the best":
            health=health+100
            
        if level==level<=0:#monster dead?
            time.sleep(0.5)
            blank()
            print(mdead)
            level=(health+5)+(level*-1)
            health=health+10
            score=score+1
    blank()
    time.sleep(0.5)
    print(pdead)
    blank()
    time.sleep(0.5)
    print(gameover)
    print("GAME OVER")
def two():
    one=('wait!!!','...',"Je suis une baguette")
    two=(5,1,2)
    for i in range(0,3):
        time.sleep(two[i])
        blank()
        print(one[i])
def one():
    one=input("what is my name?(you only get one chance)")
    if one=="pie":
        names=['robux','pie','cheese','bobux','dollars','yen','yaun',
           'candies','pineapple','Candian dollars','gold',
           'Steam points','youtube subscribers','fans','computers',
           "Gb's of memory",'Lego sets','Lego pieces','pens','pencils',
           'people saying Tu es une baguette to you','ransoms',
           'jugs of milk','calculators','cups of dirt','stuffed animals',
           'head bands','clay blobs','games','movies','bleach','straw',
           'garbage','lines of code','cereal boxes',
           'boxes','crayons','Punch and train copies','pounds of air',
           'Kerbals','sheep','farms','tons of ear wax','potato chips',
           'corn chips','Christmas trees','pine trees','birch trees',
           'maple trees','eggs','pancakes','rice',
           'books','ships','space ships','gifts','name tags',
            'people','plums','peaches','note books','pounds of grass',
            "rassberry pi's",'paint brushes','computer screens',
            'old newspapers','','pictures','microphones','headphones',
            'drones','power outlets','ice','tea bags','zoom meetings',
            'phone stands','Mail','printing presses','Crtls',
            'Comments from Tofu_Toast','screen shares',
            'people throwing tomatos at you','+ time to do homework.',
            'qwerty keyboards','thicc potions from minecraft','glue',
            'super-glue','sdfhkjahsdriuaerui','Antarctic dollers',
            'Yen','Yuan','ink','printing ink','random numbers','graphite',
            'windows bottons','noting','jsdrtqcfktgrywetbvukaerut',
            'pythons(snakes)','recordings of an cow mooing','apple pi',
            'hallos from people','hellos from people','Bonjours from people',
            '你好! from people',"random.randint's"]
        print("you now will get ",random.randint(1000,100000),random.choice(names))    
        time.sleep(1)
        print('type game(level,health,hit,yes,score) to play again.')
    else:
        print("wrong")
    two()
#start game-------------------------------------------
if onlygame==1:
    start_input(level)
game(level,health,hit,yes,score)
if pie==1:
    one()
#Yay! your at the end!
