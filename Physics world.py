# Physics World
import time

# Design welcome text
print("\n\n\t\t***\t *\t*",end="")
print("\n\t\t*  *\t *\t*"*2)
print("\t\t***\t *\t*")
print("\t\t*\t *   *  *")
print("\t\t*\t * *  * *\n")
print("\t\tPHYSICS_____WORLD\n\n")


print("General instructions:- \n1.Enter 'All formulas' to get all formulas in this program.\n2.Enter 'exit' for close the program")

# taking user text
def take_user_text():
   print(3*"\n\t|")
   text = input(f"\n\t{5*'-'}Search formula: ")
   return text.lower().strip()

# Except function: prints 'Invalid Input'
def invalid():
   print("Invalid Input")

# this fx worked on float and input
def take(ques):
   try:
      return float(input(f">>> {ques}"))
   except:
      print("You enter wrong value so, we take 1.0")
      return 1
   

user = take_user_text()
global result

# list that contain all available formulas 
main_formulas_list = ["speed", "average speed", "force", "gravitational force", "pressure", "relative density", "work done", "kinetic energy", "potential energy", "mechanical power", "frequency", "wavelength", "mirror formula", "magnification", "refractive index","lens formula","power of lens", "current","potential difference","resistance","resistivity","electric power"]
search_formulas = [ "velocity", "average velocity", "kinetic", "potential","mirror","lens","voltage"]
formulas_database = main_formulas_list + search_formulas
history = []
result = 123456789

# main block
while (user != "exit"):
   history.append(user)
   
#---------------- Some useful Algorithms --------------------------------------
   if(user == "history" or user == "formulas"):
      if(user == "history"):
         history.pop()
         for i in history:
            print(f"--> {i.title()}")
            time.sleep(.4)
      else:
         for index, value in enumerate(main_formulas_list):
            print(f"{index+1}. {value.title()}")
            time.sleep(.2)

#---------------- User expected inputs ----------------------------------------
   elif(user == ""):
      print("\n\tInvalid: Empty search".center(30))
      
   elif (user not in formulas_database and user != "history"):
      print(f"\n\t{user.title()}: Not Found") if user != "formulas" else ""
   
#---------------- CLASS 9 FORMULAS --------------------------------------------
   elif (user == "speed" or user == "velocity"):
      distance = take("Enter distance(km): ")
      time = take("Enter time(hr): ")
      result = distance/time
   
   elif (user == "average speed" or user == "average velocity"):
      initial_velocity = take("Enter initial velocity: ")
      final_velocity = take("Enter final velocity: ")
      result = (initial_velocity + final_velocity)/2
      
   elif (user == "force"):
      mass = take("Enter mass(kg): ")
      acc = take("Enter acceleration: ")
      result = mass*acc
   
   elif (user == "gravitational force"):
      M = take("Enter value of 'M'(kg): ")
      m = take("Enter value of 'm'(kg): ")
      d = take("Enter value of 'd'(km): ")
      result = (M*m)/(d**2)
   
   elif (user == "pressure"):
      thrust = take("Enter thrust: ")
      area = take("Enter area: ")
      result = thrust/area
   
   elif (user == "relative density"):
      density_substance = take("Enter density of substance: ")
      density_water = take("Enter density of water: ")
      result = density_substance/density_water
   
   elif (user == "work done"):
      force = take("Enter force(N): ")
      displacememt = take("Enter displacement: ")
      result = force*displacement
   
   elif (user == "kinetic" or user == "kinetic energy"):
      mass = take("Enter mass(kg): ")
      velocity = take("Enter velocity: ")
      result = (mass*(velocity**2))/2
   
   elif (user == "potential" or user == "potential energy"):
      m = take("Mass of object(kg): ")
      g = take("Gravity force: ")
      h = take("Enter height: ")
      result = m*g*h
   
   elif (user == "mechanical power"):
      work = take("Enter work: ")
      time = take("Enter time: ")
      result = work/time
   
   elif (user == "frequency"):
      time = take("Enter time: ")
      result = 1/time
   
   elif (user == "wavelength"):
      speed = take("Enter speed: ")
      frequency = take("Enter frequency: ")
      result = speed/frequency
   
#------------------- CLASS 10 FORMULAS -------------------------------------------------
   elif (user == "mirror" or user == "mirror formula"):
      u = take("Enter object distance: ")
      v = take("Enter image distance: ")
      result = 1/((1/u)+(1/v))
   
   elif (user == "magnification"):
      hi = take("Enter height of the image: ")
      ho = take("Enter height of the object: ")
      result = hi/ho
    
   elif (user == "refractive index"):
      n1 = take("Enter speed of light in medium 1: ")
      n2 = take("Enter speed of light in medium 2: ")
      n21 = n1/n2
      result = n21
   
   elif (user == "lens" or user == "lens formula"):
      u = take("Enter object distance: ")
      v = take("Enter image distance: ")
      result = 1/((1/v)-(1/u))
   
   elif (user == "power of lens"):
      f = take("Enter focal length: ")
      result = 1/f
   
   elif (user == "current"):
      q = take("Enter total charges: ")
      t = take("Time: ")
      result = q/t
   
   elif (user == "potential difference" or user == "voltage"):
      w = take("Work done: ")
      q = take("Total charge: ")
      result = w/q
   
   elif (user == "resistance"):
      v = take("Potential difference: ")
      i = take("Current: ")
      result = v/i
   
   elif (user == "resistivity"):
      r = take("Enter resistance of wire(R): ")
      l = take("Enter length of wire(l): ")
      a = take("Enter area of wire(A): ")
      result = (r*a)/l
   elif (user == "electric power"):
      v = take("Potential difference(V): ")
      i = take("Current (I): ")
      result = v*i
   
   elif (user == "amount of heat" or user == "amount of heat with ohms law"):
      i = take("Current(I): ")
      t = take("Time(t): ")
      if(user == "amount of heat"):
         v = take("Potential difference(V): ")
         result = v*i*t
      else:
         r = take("Resistance(R): ")
         result = (i**2)*r*t
   
   else: print()
   
   print(f"\nResult{30*':'}{result:.5f}") if user!="history" and user!="" and user!="formulas" and user in formulas_database else ""
      
   user = take_user_text()
   
print("\n\tBye Bye")


