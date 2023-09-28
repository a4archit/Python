import tkinter as tk
from tkinter import messagebox
from tkinter import *
import numpy as np

root = tk.Tk()
class MatrixCalculator:
   def __init__(self):
      
      root.title("Matrix Calculator")
      
      # app name
      app_name = tk.Label(root,
                        font = ("bold", 15),
                        text = 'Matrix Calculator')
      app_name.place(x = 50, y = 50)
      
      # taking matrix
      self.ml1 = tk.Label(root, text="A =", font=("bold", 10)).place(x=20, y=320)
      
      self.a11 = tk.Entry(root, width=5, placeholder="a11")
      self.a11.place(x=90, y=260)
      self.a12 = tk.Entry(root, width=5, placeholder="a12")
      self.a12.place(x=200, y=260)
      self.a13 = tk.Entry(root, width=5, placeholder="a13")
      self.a13.place(x=310, y=260)
      self.a21 = tk.Entry(root, width=5, placeholder="a21")
      self.a21.place(x=90, y=320)
      self.a22 = tk.Entry(root, width=5, placeholder="a22")
      self.a22.place(x=200, y=320)
      self.a23 = tk.Entry(root, width=5, placeholder="a23")
      self.a23.place(x=310, y=320)
      self.a31 = tk.Entry(root, width=5, placeholder="a31")
      self.a31.place(x=90, y=380)
      self.a32 = tk.Entry(root, width=5, placeholder="a32")
      self.a32.place(x=200, y=380)
      self.a33 = tk.Entry(root, width=5, placeholder="a33")
      self.a33.place(x=310, y=380)
      
      # set by default values
      self.a11.insert(0, 1)
      self.a12.insert(0, 2)
      self.a13.insert(0, 3)
      self.a21.insert(0, 4)
      self.a22.insert(0, 5)
      self.a23.insert(0, 6)
      self.a31.insert(0, 7)
      self.a32.insert(0, 8)
      self.a33.insert(0, 9)
      
      # select operation label
      select_operation_label = tk.Label(root, text = 'Select Operation', font=("bold", 8))
      select_operation_label.place( x = 40, y = 500)
      select_operation_listbox_options_list = [
         'Adjoint',
         'Cofactor',
         'Determinant',
         'Metrix Method',
         'Minor',
         'Inverse of Matrix'  
      ]
      self.select_operation_listbox = tk.StringVar(root)
      self.select_operation_listbox.set(select_operation_listbox_options_list[0])
      self.select_operation_listbox_menu = tk.OptionMenu(root, self.select_operation_listbox ,*select_operation_listbox_options_list)
      self.select_operation_listbox_menu.place(x=300, y=490)
      
      
      # next button
      next_btn = tk.Button(root, text="Next", width=30, command = self.next_btn_fx).place(x = 80, y=600)
      
      root.mainloop()
      
#------------------------------------- fx -----------------------------------------     
      
   def next_btn_fx(self):
      try: 
         A11 = float(self.a11.get())
         A12 = float(self.a12.get())
         A13 = float(self.a13.get())
         A21 = float(self.a21.get())
         A22 = float(self.a22.get())
         A23 = float(self.a23.get())
         A31 = float(self.a31.get())
         A32 = float(self.a32.get())
         A33 = float(self.a33.get())
         
      except:
         messagebox.showerror("Error Occured", "Enter numbers only")
         return None
         
      a = np.array([[A11,A12,A13],[A21,A22,A23],[A31,A32,A33]])
      operator = self.select_operation_listbox.get()
         
      # |A| - Determinant of A
      det_of_a = np.linalg.det(a)
      
      # Am - Minor of A
      
      
      # OPERATOR ANALYSIS
      if operator == 'Minor':
         pass
      
      messagebox.showinfo('', 'done')
         
   def minor(self, array):
      for i in range(1, 4):
         for j in range(1, 4):
            
      

if __name__ == "__main__":
   MatrixCalculator()





