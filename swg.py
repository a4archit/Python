import random
import time

# snake,water & gun
initial_text = "You can enter 's' for snake, 'w' for water and 'g' for gun"
print(initial_text)
global result
all_element = ["s","w","g"]
user = "a"

# check user command is valid
while(user!="exit"):
   user_input = input("\n\nYour chance: ")
   user = user_input.lower().strip() # remove all white spaces and text convert to lowercase
   comp = random.choice(all_element)
   time.sleep(.3)
   print(f"\tYour input: {user}\n\tComputer input: {comp}")
   
   # check right input
   if(user in all_element):
      # compare all statements
      if( user=="s" and comp=="w" or user=="w" and comp=="g" or user=="g" and comp=="s"):
         result = "you won"
      elif(user==comp):
         result = "match draw"
      else:
         result = "you lose"
   else:
      print(initial_text)
   try:
      time.sleep(.4) 
      print("\t",result.title())
   except:
      print("Something went wrong please try again.")





