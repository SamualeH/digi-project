'''
    auther: Sammie Henderson
    date:27/08/20
    version:1
    description: Movement system for my game
    improvements: Boundries set
'''

area = 0 #starting point

areas = ['0,0','0,1','0,2','0,3','1,0','1,1','1,2','1,3','2,0','2,1','2,2','2,3','3,0','3,1','3,2','3,3','1','2','3','4']

desc = ['Bottom left ','Lower left','Upper left','Top left','bottom middle left','lower middle left','Upper middle left','Top middle left','Bottom middle right','Lower middle right','Upper middle right','Top middle right','Bottom right','Lower right','Upper right','Top right','Entrance room','Battle room','Entrance room','Battle room']

n = [1,2,3,16,5,6,7,'NO',9,10,11,'NO',13,14,15,18,17,'NO',19,'NO']
s = ['NO',0,1,2,'NO',4,5,6,'NO',8,9,10,'NO',12,13,14,3,16,15,18,]
e = [4,5,6,7,8,9,10,11,12,13,14,15,'NO','NO','NO','NO','NO','NO','NO','NO']
w = ['NO','NO','NO','NO',0,1,2,3,4,5,6,7,8,9,10,11,'NO','NO','NO','NO']
#checks what rooms can be moved to

def navigation(area):
    while(True):
        print (areas [area],desc[area])
        if (n[area] != 'NO'):
            print("You can go North")
        if (s[area] != 'NO'):
            print("You can go South")
        if (e[area] != 'NO'):
            print("You can go East")
        if (w[area] != 'NO'):
            print("You can go West")

        move = input("Enter [n] [s] [e] [w]:")
        if(move == 'n' and n[area] != 'NO'):
            area = n[area]
        elif(move == 's' and s[area] != 'NO'):
            area = s[area]
        elif(move == 'e' and e[area] != 'NO'):
            area = e[area]
        elif(move == 'w' and w[area] != 'NO'):
            area = w[area]
        else:
            print('You cannot go there')
            continue
        if (area == '1' or area == '2'): #checks what room you're in
            person = 'greg' #sets who to talk to
        else:
            person = 'steve' #set's who to talk to if not greg
        print (person) #testing if person is changed properly
#code to move between rooms

#prevents error from moving out-of-bounds

#------------main area-------------
while(True):
    navigation(area)
