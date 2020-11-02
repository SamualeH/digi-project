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
    print('Well done./n You are now ready to learn about the movement system.') 
    
    


#---------main---------

intro()
