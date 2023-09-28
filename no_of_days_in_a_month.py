# Finding number of days in a month
import time

l = ["January","February","March","April","may","june","july","august","september","october","november","december"]

def months_name():
   for i,month in enumerate(l):
      print(f"\t{i+1} : {month.title()}")
      time.sleep(.3)
   

if __name__ == "__main__":
   try:
      while((nd := int(input("\n\nEnter month number\n>>> "))) != "exit"):
         if nd > 0 and nd <= 12:
            # main block
            if nd in [1,3,5,7,8,10,12]:
               no_of_days = 31
            else:
               if nd == 2: # February
                  year = int(input("Enter year: "))
                  #no_of_days = 29 if(year%4 == 0) else no_of_days = 28
                  if year%4 == 0:
                     no_of_days = 29
                  else:
                     no_of_days = 28
               else:
                  no_of_days = 30
            print(f"{l[nd-1].title()} have {no_of_days} days")
         else: # if user not give a valid month name
               # this block will be execute
            print(f"Hey Stupid {nd} is not a valid month no., see months no. below...")
            time.sleep(2)
            months_name()
   except:
      print("Something went wrong...\n\n\tPlease Try Again\n\n")


