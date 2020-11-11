def combat(person): 
    future_db = 0 #placeholder for db functionality
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

        if (future_db == 2):
            print("Greg: You're pretty good. Take this key and go on to the next fortress")
        else:
            print("Greg: That was pretty bad, just take the key for the next fortress and leave")
    
    elif(person =='steve'):
        pass

person = 'greg'
combat(person)
