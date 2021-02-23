import random
import string

#Warn the User what he/she/it is allowed to input as dimensions
print("The values you are allowed to input are between 3 and 10 for both of the rectangle's dimensions, this is because of the window size of the console :)")

#This input_switch variable checks the values that have been input by the user
input_switch = 1

#The Summary is what we will need later on, in order to calculate the summary of matches and present the average
Summary = 0

#This bit controls the values that the user inputs, it will loop until the user puts the correct values as previsouly mentioned,
#or until the user interrupts the program himself/herself/itself
while bool(input_switch):
    height = int(input("Input the rectangle's height: "))
    length = int(input("Input the rectangle's length: "))
    if 3 <= height and length <= 10:
        input_switch = 0
    else:
        print("The numbers that have been inputed are off the course.")


#This bit is a method that creates the list, fills half of it with 'S's and the other half with 'O's
#After the filling it shuffles it so the elements can take random positions on the 'board'
def ListCreation():
    myList = []
    List_Elements = height*length
    Halving = List_Elements//2
    y=0
    #I control both cases, odd dimensions and even dimensions
    if (height*length) % 2 != 0:
        for i in range(Halving):
            myList.append('S')
            y=i
        for y in range(Halving+1):
            myList.append('O')
    else:
        for i in range(Halving):
            myList.append('S')
            y=i
        for y in range(Halving):
            myList.append('O')
    random.shuffle(myList)
    return myList

#This method splits the list in sublists so I can create the illusion of a game board in the console,
#it returns the new "list of lists"
def ListSplitting(list, length):
    n=length
    newList=[list[i*n:(i+1)*n] for i in range((len(list)+n-1)//n)]
    return newList

#This method is where I calculate and count the S-O-S,
#It returns the summary so I can calculate the average later on
def SoSCalculation(list,Summary):
    match=0
    for y in range(len(list)):
        for x in range(len(list[y])):
            if list[y][x] == 'S':

                #This condition limits the horizontal index boundaries so the compiler can relax and stop whining :)
                if x<len(list[y])-2:
                    if list[y][x+1] == 'O' and list[y][x+2] == 'S':
                        #I calculate the horizontal SOS's here (it also counts the double, triple etc. SOSOS's)
                        match+=1

                #This condition limits the vertical index boundaries so the compiler can relax and stop whining :)
                if  y<len(list)-2:
                    if list[y+1][x] == 'O' and list[y+2][x] == 'S':
                        #I calculate the vertical SOS's here (it also counts the double,triple etc. SOSOS's)
                        match+=1

                #This condition limist both the vertical and horizontal index boundaries so the compiler can relax and stop whining :)
                if (x<len(list[y])-2) and (y<len(list)-2):
                    if list[y+1][x+1] == 'O' and list[y+2][x+2] == 'S':
                        #I calculate the diagonal SOS's here (it also counts the double, triple etc. SOSOS's)
                        match+=1
    Summary+=match
    return Summary

#This is my main code, I loop 100 times, i create and fill my list through my ListCreation() method and split it with my ListSplitting() method
#I print sublist after sublist so I can create the game board and i calculate the S-O-S's with my SoSCalculation() method that returns my Summary
for i in range(0,99):
    list = []
    list = ListCreation()
    a  = ListSplitting(list,length)
    for i in range(height):
        print (a[i])

    Summary = SoSCalculation(a,Summary)
    print('Current Summary is: ', Summary)

#Here I print the Average to the user
print('The average is: ',Summary/100)
