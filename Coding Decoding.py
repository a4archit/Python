# Text coder and decoder

# user choice
def take_text():
   return str(input("Enter 'c' for using coding and 'd' for decoding: ")).lower().strip()

def dash_line(): print("-"*50)

choice = take_text()
coding_choice = ["c","coding","code"]
decoding_choice = ["d","decoding","decode"]
choice_possibilities = coding_choice + decoding_choice

# text to char list
def to_list(text):
   text_list = [i for i in text]
   return text_list

'''
this function take a character and convert into these things
   s -> $   . -> =   a -> @   h -> #
   n -> &   r -> ₹   p -> %   l -> £
   e -> €   '' -> _
'''
def coding_change_character(char):
   if char == ".": return "0"
   elif char == "s": return "$"
   elif char == "a": return "@"
   elif char == "h": return "#"
   elif char == "n": return "&"
   elif char == "r": return "₹"
   elif char == "p": return "%"
   elif char == "q": return "?"
   elif char == "e": return "!"
   elif char == " ": return "_"
   else: return char

def decoding_change_character(char):
   if char == "0": return "."
   elif char == "$": return "s"
   elif char == "@": return "a"
   elif char == "#": return "h"
   elif char == "&": return "n"
   elif char == "₹": return "r"
   elif char == "%": return "p"
   elif char == "?": return "q"
   elif char == "!": return "e"
   elif char == "_": return " "
   else: return char


def coding(text): # Coding main code
   char_list = to_list(text)
   update_char_list = list(map(coding_change_character, char_list))
   return update_char_list

def decoding(text): # Decoding main code
   char_list = to_list(text)
   update_char_list = list(map(decoding_change_character, char_list))
   return update_char_list


while (choice != "exit"): # Valid Input
   
   if choice in choice_possibilities:
      if choice in coding_choice :# Coding block
         dash_line()
         text = input("Enter text for Coding: ")
         coded_code = coding(text)
         for i in coded_code:
            print(i, end="")
         print()
      
      else: # Decoding block
         dash_line()
         text = input("Enter text for Decoding: ")
         decoded_code = decoding(text)
         decoded_code = decoding(text)
         for i in decoded_code:
            print(i, end="")
         print()
   
   else: # Invalid Input
      print("Invalid: Empty Text") if choice=="" else print("Only 'c' or 'd' is accepted!")
   
   choice = take_text()




