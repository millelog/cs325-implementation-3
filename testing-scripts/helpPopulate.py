from random import randint,uniform
from pickle import load, dump

#Creates a data set with issued math function
#Alters the data slightly, in order to be discovered with
# LP algorythm to test its effectiveness.
#
def populateUsing(math_function, num_data=100):
    data = []
    for i in range(num_data):
        y = math_function(i)
        # this is to add deviation, but it should still resemble original
        # y = y + ( uniform(-1,1) * y*5/100) #10%*number * (x/100)% so deviation ranges from 0 to 5% of y value
        y = y + ( uniform(-1,1)*5 ) #10%*number * (x/100)% so deviation ranges from 0 to 5% of y value
        data.append([i,y]) # appedn the altered point
    return data

# 10% of number = number*10/100


def pickleOut(data,file_name):
    file = open(file_name,'w')
    dump(data,file) # dumps the file
    return

def pickleIn(file_name):
    file = open(file_name,"r")
    data = load(file)
    return data
