'''
    auther: Sammie Henderson
    date:27/08/20
    version:1
    description: Movement system for my game
    improvements: Boundries set
'''

area = 0 #starting point

areas = ['0,0','0,1','0,2','0,3','1,0','1,1','1,2','1,3','2,0','2,1','2,2','2,3','3,0','3,1','3,2','3,3']

desc = ['Bottom left ','Lower left','Upper left','Top left','bottom middle left','lower middle left','Upper middle left','Top middle left','Bottom middle right','Lower middle right','Upper middle right','Top middle right','Bottom right','Lower right','Upper right','Top right']

n = [1,2,3,'NO',5,6,7,'NO',9,10,11,'NO',13,14,15,'NO']
s = ['NO',0,1,2,'NO',4,5,6,'NO',8,9,10,'NO',12,13,14]
e = [4,5,6,7,8,9,10,11,12,13,14,15,'NO','NO','NO','NO','NO']
w = ['NO','NO','NO','NO',0,1,2,3,4,5,6,7,8,9,10,11]
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
        
#code to move between rooms

#prevents error from moving out-of-bounds

#------------main area-------------
while(True):
    navigation(area)
