'''
    auther: Sammie Henderson
    date:17/11/20
    version:1
    description: Full game
    improvements: Created
'''


area = 0 #starting point

areas = ['0,0','0,1','0,2','0,3','1,0','1,1','1,2','1,3','2,0','2,1','2,2','2,3','3,0','3,1','3,2','3,3','1','2','3','4']

desc = ['Bottom left ','Lower left','Upper left','Top left','bottom middle left','lower middle left','Upper middle left','Top middle left','Bottom middle right','Lower middle right','Upper middle right','Top middle right','Bottom right','Lower right','Upper right','Top right','Entrance room','Battle room','Entrance room','Battle room']

n = [1,2,3,16,5,6,7,'NO',9,10,11,'NO',13,14,15,18,17,'NO',19,'NO']
s = ['NO',0,1,2,'NO',4,5,6,'NO',8,9,10,'NO',12,13,14,3,16,15,18,]
e = [4,5,6,7,8,9,10,11,12,13,14,15,'NO','NO','NO','NO','NO','NO','NO','NO']
w = ['NO','NO','NO','NO',0,1,2,3,4,5,6,7,8,9,10,11,'NO','NO','NO','NO']
#checks what rooms can be moved to


def intro():
    #opening message
    print('''
 __          __         _                                       _             
 \ \        / /        | |                                     | |            
  \ \  /\  / /    ___  | |   ___    ___    _ __ ___     ___    | |_    ___    
   \ \/  \/ /    / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \   
    \  /\  /    |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |  
     \/  \/      \___| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/
    ____            _                                        _   
   / __ \          (_)                                      | |  
  | |  | |  _   _   _   ____     __ _   _   _    ___   ___  | |_ 
  | |  | | | | | | | | |_  /    / _` | | | | |  / _ \ / __| | __|
  | |__| | | |_| | | |  / /    | (_| | | |_| | |  __/ \__ \ | |_ 
   \___\_\  \__,_| |_| /___|    \__, |  \__,_|  \___| |___/  \__|
                                   | |                           
                                   |_|
In this game you will partake in a battle of wits in order to free this kingdom from the evil that has corrupted it.''')
    name = input('Please enter your name:')
    #putting name into database
    #c.execute("INSERT INTO players VALUES ({''})".format(name))
    print('Welcome ', name, '''. In this game you will be asked questions, and will be expected to answer them.
When you are asked a question, there will be a list of options lettered A-Z. If you wish to select an option you simply type the letter.''',sep='')
    while(True):
        t_question = input('Heres an example: Do you prefer a) Tomato Sauce b) Mayonnaise')
        if(t_question.lower() != "a" and t_question.lower() != "b"):
            print('Try again')
            continue
        elif(t_question.lower() == 'a' or t_question.lower() == 'b'):
             break
    print('Well done.\nYou are now ready to learn about the movement system. When you are not in combat or conversation, you will be told what directions you can move. You move by typing the first letter of the direction (N for North). Lets try') 
    while(True):
        t_question = input('You can go North\nYou can go East\nEnter [n] [s] [e] [w]:')
        if(t_question.lower() != 'n' and t_question.lower() != 's' and t_question.lower() != 'e' and t_question.lower() != 'w'):
            print('Try again')
            continue
        elif(t_question.lower() == 'n' or t_question.lower() == 'e'):
            print('You did it.You beat the tutorial')
            break
        elif(t_question.lower() == 's' or t_question.lower() == 'w'):
            print("So close, but you can't move that way here")
            continue
    

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
        if (area == '2'): #checks what room you're in
            person = 'greg' #sets who to talk to
            combat(person)
        elif(area == 4):
            person = 'steve' #set's who to talk to if not greg
            combat(person)
        else:
            person = 'null' #sets person just in case
        print (person) #testing if person is changed properly



#def variable for text
def dialoge(person):
    if (person == 'greg'):
        print('"Welcome to my home. What would you like to ask me."')
        while(True):
            chat_option = input("Would you like to [A]Ask about his day, [B]Ask about his personal life, [C]Quiz battle!")
            if (chat_option.lower() != 'a' and chat_option.lower() != 'b' and chat_option.lower() != 'c'): #checks if answer is valid
                print ("Try again")
                continue
            elif (chat_option.lower() == 'a'):
                print('"Well it was actually quite nice, thanks for asking"')
            elif (chat_option.lower() == 'b'):
                print('"Id rather not get into that, seeing as I just met you"')
            elif (chat_option.lower() == 'c'):
                print('"Ah, I see what you want. Well, no sense in delaying this. Have at the!"')
                #combat(person):
                #break
    elif (person == 'steve'):
        print('"Welcome to my home. What would you like to ask me."')
        while(True):
            chat_option = input("Would you like to [A]Ask about his day, [B]Ask about his personal life, [C]Quiz battle!")
            if (chat_option.lower() != 'a' and chat_option.lower() != 'b' and chat_option.lower() != 'c'): #checks if answer is valid
                print ("Try again")
                continue
            elif (chat_option.lower() == 'a'):
                print('"Its been rather agrovating, what with all these adventurers showing up at my house and challenging me to quiz battles "')
            elif (chat_option.lower() == 'b'):
                print('"Between you and me, I acutally dont exist outisde this conversation"')
            elif (chat_option.lower() == 'c'):
                print('"Really? Fine. Have at the or whatever"')
                #combat(person):
                #break

            
    else:
        print("How did you break the game like this? Sorry, but Youll have to restart your run :(")



def combat(person): 
    future_db = 0 #placeholder for db functionality
    future_dbsteve = 0
    if (person == 'greg'): #checks what person's quiz to use
        print("Greg: Ah, so you think you can beat me in a battle of wits. We'll just see about that.")
        
        while(True):
            quiz_answer = input("What character do you play as in Wario's Woods for the NES:\nA)Mario B)Wario C)Toad") 
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Greg: Wow, that wasn't even a real answer. Are you even trying?")
                continue
            elif (quiz_answer.lower() == 'a' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Greg: wow, ur bad")
            elif (quiz_answer.lower() == 'c'): #checks if answer correct
                print("Greg: Hmm, you're pretty smart, but what about this!")
                future_db = future_db + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        while(True):
            quiz_answer = input("What kind of uranium is commonly used in nuclear fuel:\nA)Uranium 235 B)Uranium 238 C)Uranium lite")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Greg: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'c' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Greg: PLACEHOLDER WRONG ANSWER COMMENT")
            elif (quiz_answer.lower() == 'a'): #checks if answer correct
                print("Greg: Hmm")
                future_db = future_db + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        while(True):
            quiz_answer = input("What kind of vegetable is a potato:\nA)Tuber B)Leafy 238 C)It's actually a fruit")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Greg: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'c' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Greg: PLACEHOLDER WRONG ANSWER COMMENT")
            elif (quiz_answer.lower() == 'a'): #checks if answer correct
                print("Greg: Hmm")
                future_db = future_db + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break
        
        if (future_db == 3):
            print("Greg: You're pretty good. Take this key and go on to the next fortress")
        else:
            print("Greg: That was pretty bad, just take the key for the next fortress and leave")
    

    elif(person =='steve'):
        print('Be prepared to lose')
        while(True):
            quiz_answer = input("Who do you play as in the portal series of video games:\nA)Chell B)Mell C)Well")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Steve: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'c' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Steve: Have you not played portal before? If not you should, it's pretty fun")
            elif (quiz_answer.lower() == 'a'): #checks if answer correct
                print("Steve: Finally, someone knows that one")
                future_dbsteve = future_dbsteve + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        while(True):
            quiz_answer = input("What economic model does the U.S. use:\nA)Communism B)Capitalism C)Socialism")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Steve: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'c' or quiz_answer.lower() == 'a'): #checks if answer correct
                print("Steve: Man, and I thought this was an easy question")
            elif (quiz_answer.lower() == 'b'): #checks if answer correct
                print("Steve: They sure do love their money")
                future_dbsteve = future_dbsteve + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        while(True):
            quiz_answer = input("What year was the Treaty of Waitangi signed:\nA)1850 B)1846 C)1840")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Steve: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'a' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Steve: You should reaqlly polish up on your NZ history")
            elif (quiz_answer.lower() == 'c'): #checks if answer correct
                print("Steve: Good to see you know at least a little about NZ history")
                future_dbsteve = future_dbsteve + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        while(True):
            quiz_answer = input("What country is the biggest producer of bananas:\nA)India B)China C)Madagascar")
            if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
                print("Steve: Wow, that wasn't even a real answer. Are you even trying?")
            elif (quiz_answer.lower() == 'a' or quiz_answer.lower() == 'b'): #checks if answer correct
                print("Steve: Bananas are a serious subject")
            elif (quiz_answer.lower() == 'c'): #checks if answer correct
                print("Steve: I'm glad you realise that bananas are a serious subject ")
                future_dbsteve = future_dbsteve + 1 #I'm going to add a bit here that adds 1 to the players score in the db
            break

        if (future_db == 4):
            print("Steve: You're pretty good. Take this key and go on to the next fortress")
        else:
            print("Steve: That was pretty bad, just take the key for the next fortress and leave")



#---------main---------

intro()

while(True):
    navigation(area)
