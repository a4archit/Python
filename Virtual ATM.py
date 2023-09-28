# Virtual ATM
import time

name = input("Your name: ").lower().strip()

# Take number and return 5 if user will provide wrong number for running the while loop of ____taking_input____ function 
def take_num(text):
   try: return int(input(text))
   except: return 5

# This contain a loop that execute when user provide wrong value
def taking_input():
   print("\n\n1. Withraw money\n2. Check Bank Balance\n3. History\n4. Exit")
   num = take_num("Enter number: ")
   while(num>4 or num<1):
      num = take_num(f"{name} you are fool!\nYou can enter 1,2,3, or 4 only: ")
   return num

global amount
amount = 100000

num = taking_input()

history = []
while (num != 4):
   if num == 1:# Cash withdrawl block
      history.append("cash withdraw")
      try:
         user_amount = int(input(f"{50*'-'}\nEnter amount for withdraw: "))
      except:
         print("Invalid!")
         
      if user_amount <= amount:
         amount -= user_amount
         print("Processing...")
         time.sleep(2)
         print("---------- Transaction Complete ----------")
         time.sleep(1)
         print("Horray!")
         print(f"\tName: {name.title()}\n\tAccount no: XXXXXXXXXX78\n\tIFSC Code: XXXXXXXXXX62")
         print(f"\tBalance: ₹{amount}/-")
         time.sleep(2)
      
      else:
         print(f"\tInvalid: Insufficient Amount\nTry again {name}\n\n")
      
   elif num == 2:# Check Bank Balance Block
      history.append("check bank balance")
      print("\n\nPlease wait...")
      time.sleep(1)
      print(f"Your Account Balance: ₹{amount}/-")
   else:# History
      for index, value in enumerate(history):
         print(f"{index+1} --> {value.title()}")
      
   num = taking_input()

print(f"\nThanks {name.title()} for using ATM machine.")

