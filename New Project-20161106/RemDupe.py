
def RemDupe():
    lst = ["a","b","c","d","e","f","g","h","i","j","b","d","h","e","e","i"];    
    output = []
    for i in lst:
        if i not in output:
            output.append(i)
            print output;
            return output
            
            

            