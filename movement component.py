'''
    auther: Sammie Henderson
    date:27/08/20
    version:1
    description: Movement system for my game
    improvements: Exists
'''

area = 0 #starting point

areas = ['0,0','0,1','0,2','1,0','1,1','1,2','2,0','2,1','2,2']

desc = ['0','1','2','3','4','5','6','7','8','9']

n = [1,2,'NO',4,5,'NO',7,8,'NO']
s = ['NO',0,1,'NO',3,4,'NO',6,7]
e = ['NO','NO','NO',1,2,3,4,5,6]
w = [4,5,6,7,8,9,'No','NO','NO']
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
        elif(move == 'e'):
            area = e[area]
        elif(move == 'w'):
            area = w[area]

        
#code to move between rooms

#prevents error from moving out-of-bounds

#------------main area-------------
navigation(area)