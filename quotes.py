# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "quotes.py" program of the Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).

import tkinter
import tkinter.messagebox
import json

from uritemplate import expand


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of quotes.py" section of the assignment brief.          
        self.master = tkinter.Tk()
        self.data = self.get_JSONdata()

        self.master.title('Quote Dialogue')
        self.master.minsize(width=1200, height=600)
        self.master.config(padx=100, pady=200)

        frame = tkinter.Frame(self.master)
        frameBtn = tkinter.Frame(self.master)

        self.current_quote = 0
        self.skip_btn = tkinter.Button(frameBtn, text='Skip', command=lambda: self.rate_quote('skip'))
        self.like_btn = tkinter.Button(frameBtn, text='Like', command=lambda: self.rate_quote('likes'))
        self.love_btn = tkinter.Button(frameBtn, text='Love', command= lambda: self.rate_quote('loves'))
       
        self.labelQuote = tkinter.Label(frame,font=('Arial', 26, 'bold'))
        self.labelAuthor = tkinter.Label(frame,font=('Times New Roman Baltic', 22, 'italic'),bd=2)
        frame.pack()
        frameBtn.pack()
        self.show_quote()
        self.master.mainloop()



    def show_quote(self):
        # This method is responsible for displaying the details of the current quote in the GUI.
        # See Point 1 of the "Methods in the GUI class of quotes.py" section of the assignment brief.
        index = self.current_quote
        quote = f'"{self.data[index]["quote"]}"'
        author = f"- {self.data[index]['author']}"
        if 'year' in self.data[index]:
            year = self.data[index]['year']
        else:
            year = None
        if year:
            author = f'{author}, {year}'

        self.labelQuote.config(text=quote)
        self.labelAuthor.config(text=author)

        self.labelQuote.grid(column=1, row=0) 
        self.labelAuthor.grid(column=1,row=1)

        self.skip_btn.grid(column=0, row=5)
        self.like_btn.grid(column=1, row=5)
        self.love_btn.grid(column=2, row=5)
        

    def rate_quote(self, rating):   
        # This method is responsible for recording the rating of the quote when a button is clicked.
        # See Point 2 of the "Methods in the GUI class of quotes.py" section of the assignment brief.
        if rating == 'skip':
            if self.current_quote == len(self.data) - 1:
                tkinter.messagebox.showinfo("End of Quotes","That was the last quote. The program will now end.")
                self.master.destroy()
                return
            else:
                self.current_quote += 1
                tkinter.messagebox.showinfo("Rating Skipped","You have skipped rating this quote.")
                self.show_quote()
        
        else:
            index = self.current_quote
            self.data[index][rating] += 1
            with open('data.txt', 'w') as f:
                data = json.dumps(self.data, indent=4)
                f.write(data)
            tkinter.messagebox.showinfo("Rating Recorded","Your rating has been recorded.")

            if self.current_quote == len(self.data) - 1:
                tkinter.messagebox.showinfo("End of Quotes","That was the last quote. The program will now end.")
                self.master.destroy()
                return
            
            self.current_quote += 1
            self.show_quote()

    def get_JSONdata(self):
        try:
            f = open('data.txt', 'r')
            data = json.load(f)
            f.close()
        except:
            tkinter.messagebox.showerror('Error','Missing/Invalid file')
            self.master.destroy()
            return
        return data

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()