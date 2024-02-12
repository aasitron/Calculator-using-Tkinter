from tkinter import *
import ast 
root = Tk()

#This will allow us to print our number's entry in the display screen:
i = 0
def get_number(num):
    global i # To access i outside the function
    display.insert(i,num) #i beacuse we don't know the index yet
    i += 1 #Increment So that the number is placed next to the previous number

#This will allow us to print our operation's entry in the display screen:
def get_operations(operator):
    global i
    length = len(operator) # we are getting length of the operator first and then incrementing because some operators have more than 1 space
    display.insert(i,operator)
    i += length

#This will allow us to clear our entire entry in the display screen:
def clear_all():
    display.delete(0,END) # It clears all the output starting from 0th index till the end
    
#This will take the entry output and parse into the evaluation to display the result:
def calculate():
    entire_string = display.get() # This will give the entire mathematical operation in the entry screen
    #Using AST module which parses and evaluates mathematical equations
    try:
        node = ast.parse(entire_string, mode='eval') #eval will perform the evaluation
        result = eval(compile(node,'<string>','eval')) #entry widget gives output in string format
        clear_all() # To clear Out existing operations for e.g we type 2 + 2 now to get 4 we need to clear 2 + 2
        display.insert(0, result) #Display the result in index 0
    except Exception:
        clear_all()
        display.insert(0,"Error")

# Create an Undo Button
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1] #Deleting last value using negative slicing
        clear_all()
        display.insert(0,new_string) # DIsplaying the new string in index 0
    else:
        clear_all()
        display.insert(0,"") # Adding an empty string after clearing


#Display Screen:
display = Entry(root)
display.grid(row=1,columnspan=6)

#Creating Buttons Using Loop:
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0 
for x in range(3):
    for y in range(3):
        button_text = numbers[counter] #Counting From the 0th index
        button = Button(root,text=button_text,width=4,height=2,command= lambda text=button_text:get_number(text))
        button.grid(row=x+2,column=y) #Staring From Row 2 Becaus in Row 1 we have the display screen
        counter += 1

        """
        Explanation Of the above Code
        Suppose we Click the button 1
        For Button 1 the text is going to be button_text
        So it means number[0] that is 1
        And the get_number Function is called
        It accepts the value 1 
        and insert the value 1 at index position 0 
        and everytime get_number Function is called it increments the value of i by 1       
        """

#Creating 0 Button seperately:
button = Button(root,text="0",width=4,height=2,command= lambda :get_number(0))
button.grid(row=5,column=1)

#Creating Button for Operations:
count = 0
operations = ['+','-','*','/','*3.14','%','(',')','**','**2']
for x in range(4):
    for y in range(3): 
        if count < len(operations):
            button = Button(root,text=operations[count],width=4,height=2,command= lambda text=operations[count]:get_operations(text)) # As we loop value of count goes from 0 to 10 and the values get extracted
            count += 1
            button.grid(row=x+2,column=y+3) # Till Column 2 Its already Utilized

#Creating All Clear (AC) button:
button = Button(root,text="AC",width=4,height=2,command=clear_all)
button.grid(row=5,column=0)

#Creating Equal to (=) button:
button = Button(root,text="=",width=4,height=2,command=calculate)
button.grid(row=5,column=2)

#Creating Backspace (<--) button:
button = Button(root,text="<--",width=4,height=2,command= lambda :undo())
button.grid(row=5,column=4)
root.mainloop()