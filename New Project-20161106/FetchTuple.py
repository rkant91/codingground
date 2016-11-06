#Program to get the 4th element from the start and 4th element from last of a tuple

def FetchTuple(tp = ["a","b","c","d","e","f","g","h","i","j","b","d","h","e","e","i"]):
    print len(tp)
    f4 = tp[3];
    strlen = len(tp)
    l4 = tp[strlen-4]
    print "Fist 4th element: ",f4 + " | Last 4th element : ",l4
    return

    

    
