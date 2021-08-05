#function to accept values
def accept():
    num1=int(input('ENTER NUMBER 1: '))
    num2=int(input('ENTER NUMBER 2: '))
    return num1,num2
#function for add
def add():
    x,y=accept()
    return x+y


#function for sub
def sub():
    x, y = accept()
    return x-y

#function for div
def div():
    x, y = accept()
    return x/y

#function for mul
def mul():
    x, y = accept()
    return x*y

#for users list
print('operations : \n'
      '1.add\n'
      '2.sub\n'
      '3.div\n'
      '4,mul\n'
      '5.exit\n')

def errorhandle():
    print('wrong option')

#used as do while
while True:
    operations ={
        1:add,
        2:sub,
        3:div,
        4:mul,
        5:exit
    }
    # to take choice from user
    choice = int(input('ENTER YOUR CHOICE:'))

    output=operations.get(choice,errorhandle)()
    #output=operations[choice]()
    print(output)