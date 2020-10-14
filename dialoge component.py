person = 'greg'

#set variable for who's speaking



#def variable for text
def dialoge(person):
    if (person == 'greg'):
        print('"Welcome to my [PLACEHOLDER TEXT]"')
        while(True):
            chat_option = input("Would you like to [A]Ask about his day, [B]Ask about his personal life, [C]Quiz battle!")
            if (chat_option.lower() != 'a' and chat_option.lower() != 'b' and chat_option.lower() != 'c'):
                print ("Try again")
            if (chat_option.lower() == 'a'):
                print("Well it was actually quite nice, thanks for asking")

    elif (person == 'phillip'):
        pass


dialoge(person)




