# String reversal using while loop

def reverse_while(str1):
    reverse_name =""
    full_name = str1
    print len(full_name)
    i = len(full_name)
    while i > 0:
        reverse_name += full_name[i-1]
        i -=1
    print reverse_name
    return
    


# String reversal using for loop

def reverse_for(str2):
    reverse_name1 =""
    full_name = str2
    for i in range(len(full_name)-1,-1,-1):
        reverse_name1 += full_name[i]
        
    print reverse_name1
    return
    
def ReverseString():
    prompt = '>'

    print "Enter string to reverse"
    wstr = raw_input(prompt)
    print "Enter loop type: 'for' or 'while' ?"
    ltype = raw_input(prompt)
    
    if ltype == 'for':
        reverse_for(wstr);
    elif ltype == 'while':
        reverse_while(wstr);
    else:
        print "Loop Type entered incorrectly"
        print "Do you want to try again (y/n) ?"
        ans = raw_input(prompt)
        if ans == 'y':
            ReverseString();
        else:
            exit();
    return
    