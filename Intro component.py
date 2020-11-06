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
    


#---------main---------

intro()
