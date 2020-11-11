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
    

person = 'greg'
combat(person)
