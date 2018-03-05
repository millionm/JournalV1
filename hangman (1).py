hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")

hangman_word = input("Enter the secret word: ")
hangman_list = list(hangman_word)


answer = list()
for i, c in enumerate(hangman_list):
    answer.append("___")

correct_answers = 0
wrong_answers = 0
print(hangman[0])
print()
print(" ".join(answer))
while correct_answers != len(hangman_list) and wrong_answers < 7:
    letter = input("Type in a letter: ")
    correct_guess = 0
    for i, c in enumerate(hangman_list):
        if letter == c:
            answer[i] = "_" + letter + "_"
            correct_answers = correct_answers + 1
            correct_guess = 1
    if correct_guess == 0:
        wrong_answers = wrong_answers + 1
    print(hangman[wrong_answers])
    print(" ".join(answer))
print()
if correct_answers == len(hangman_list):
    print("CONGRATZ, you rock.")
else:
    print("You are charged with manslaughter.")



