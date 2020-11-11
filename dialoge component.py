person = 'steve'

#set variable for who's speaking



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


dialoge(person)




