


def one():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    hold=""
    for i in mylist:
        i[0]=" "
        i[1]=" "
        hold = hold+"".join(i)+"\n"
    return(hold)
        
def two():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[1][0] =" "
    mylist[1][1] =" "
    mylist[3][1] =" "
    mylist[3][2] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
    

def three():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[1][0] =" "
    mylist[1][1] =" "
    mylist[3][0] =" "
    mylist[3][1] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
    
def four():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[0][1] =" "
    mylist[1][1] =" "
    mylist[3][0] =" "
    mylist[3][1] =" "
    mylist[4][0] =" "
    mylist[4][1] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
def five():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[1][2] =" "
    mylist[1][1] =" "
    mylist[3][1] =" "
    mylist[3][0] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
        
def six():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[1][2] =" "
    mylist[1][1] =" "
    mylist[3][1] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
    
def seven():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[1][0] =" "
    mylist[1][1] =" "
    mylist[2][0] =" "
    mylist[2][1] =" "
    mylist[3][0] =" "
    mylist[3][1] =" "
    mylist[4][0] =" "
    mylist[4][1] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
        
def eight():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)

def nine():
    mylist = [['#' for i in range(0,3)] for i in range(0,5)]
    mylist[1][1]=" "
    mylist[3][1]=" "
    mylist[3][0] =" "
    mylist[3][1] =" "
    hold=""
    for i in mylist:
        hold = hold+"".join(i)+"\n"
    return(hold)
def switch(lang):
        lang=int(lang)
        if lang == 1:
            return one()
        elif lang == 2:
            return two()
        elif lang == 3:
            return three()
        elif lang == 4:
            return four()
        elif lang == 5:
            return five()
        elif lang == 6:
            return six()
        elif lang == 7:
            return seven()
        elif lang == 8:
            return eight()
        elif lang == 9:
            return nine()
        
      
            
number = input("enter number")
hold=[]
for n in number:
    hold.append(switch(n))
for i in hold:
    i.rstrip('\n')
print("".join(hold))