def combat(): 
    if (person == 'greg'): #checks what person's quiz to use
        print("Ah, so you think you can beat me in a battle of wits. We'll just see about that.")
        quiz_answer = input("What character do you play as in Wario's Woods for the NES:\nA)Mario B)Wario C)Toad") 
        if (quiz_answer.lower() != 'a' and quiz_answer.lower() != 'b' and quiz_answer.lower() != 'c'): #checks if answer valid
            print("Wow, that wasn't even a real answer. Are you even trying?")
        elif (quiz_answer.lower() == 'a' or quiz_answer.lower() == 'b'): 
            print("wow, ur bad")
        elif (quiz_answer.lower() == 'c'):
            print("dang, you win")
            #I'm going to add a bit here that adds 1 to the players score in the db

    elif(person =='fred'):
        pass


person = 'greg'
combat()