def check(expression):

    open_tup = tuple('({[')
    close_tup = tuple(')}]')

    map = dict(zip(open_tup,close_tup))

    queue = []

    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i!=queue.pop():
                return "Unbalanced"
            
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"
    

string = "{[]{()}}"
print(string,"-",check(string))