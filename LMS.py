import numpy as np
import pandas as pd
import sys
import os
import time
import datetime

head_txt = '''Welcome in LMS 1.0.8 (Library Management System)
'''

input_txt = '''
Select an option:
1. Add a book
2. Search a book
3. Show all books
4. Take excel file
5. Exit
'''

# decorator
def linedesign(fx):
    def mfx(*args, **kwargs):
        print('-'*40)
        fx(*args, **kwargs)
        print('-'*20)
    return mfx

# main class 
class LMS:
    def __init__(self):
        print(head_txt)
        # creating a numpy array for storing whole information
        self.books = np.empty((0,3)) 
        self.books = np.append(self.books, np.array([['maths class-viii', 'ncert', 385]]), axis=0)
        self.books = np.append(self.books, np.array([['hindi class-vi', 'ncert', 847]]), axis=0)
        self.booksdf = pd.DataFrame(self.books)
        self.booksdf.columns = ['TITLE', 'AUTHOR', 'PAGES']
        while True:
            op = self.taking_user_main_input()
            if op == 1: self.add_a_book()
            elif op == 2: self.search_a_book()
            elif op == 3: self.show_all_books()
            elif op == 4: self.take_excel_file()
            else:
                sys.exit()

    
    def taking_user_main_input(self):
        time.sleep(.5)
        while True:
            print(input_txt)
            try:
                option = int(input('Enter here: '))
            except:
                print('Wrong Option Try Again!')
                continue
            if option > 0 and option < 6:
                return option
            else:
                print(f"'{option}' - is invalid (0-5), Try Again!")
 
    
    def add_a_book(self):
        
        while True:
            # taking inputs
            title = input("Enter title: ").lower().strip()
            author = input("Enter author: ").lower().strip()
    
            if title == '' or author == '':
                print('Title or Author never be Empty')
    
            # taking a valid no. of pages
            try:
                pages = int(input("Enter no. of pages: "))
            except:
                print('!!! Enter a valid number !!!')
                continue
    
            # add book to database
            self.books = np.append(self.books, np.array([[title, author, pages]]), axis=0)
            print('Book added Successfully!')
            self.booksdf = pd.DataFrame(self.books)
            self.booksdf.columns = ['TITLE', 'AUTHOR', 'PAGES']
            if (permission:=input("\n\nDo you want to add a new book(Y/N): ").lower().strip() == 'n'):
                break
 
    def search_a_book(self):
        results = []
        print('\nEnter \'exit\' for exiting. ')
        while True:
            results.clear()
            usearch = input('\n\n>>> ').lower().strip()
            if usearch == 'exit': break
            for book_title in list(self.books[:,0]):
                if book_title.startswith(usearch):
                    results.append(book_title)
            if len(results) != 0:
                # print searcheable results
# here some changes need (i am give columns list but it needs index)                resultsdf = self.booksdf.loc[results,:]#pd.DataFrame(results)
                resultsdf.columns = ['BOOKS']
                print(f"\nThere are {len(results)} book(s) found for '{usearch}'\n")
                print(resultsdf)
            else:
                print(f"\n\tNo Book found for '{usearch}'\n")
            
    def show_all_books(self):
        print(self.booksdf)

    def take_excel_file(self):
        datetime_now = datetime.datetime.now()
        filename = f'Book Data {datetime_now}.csv'
        self.booksdf.to_csv(filename)
        print(f'\n\n\'{filename}\'\n\tFile Saved Successfully!\n\n')
        
if __name__ == "__main__":
    LMS()


