import re

previous = 0
run = True

def performmath():
    global run
    global previous
    eq=""
    if previous==0:
        eq=input("Enter equation")
    else:
        eq=input(str(previous))
    if eq == 'quit':
        run = False
    else :
        run=True
        eq = re.sub('[a-zA-Z,.:()]','',eq)
        if  previous==0:
            previous =eval(eq)
        else:
            previous = eval(str(previous) + eq)
        print(previous)


while(run):
    performmath()
