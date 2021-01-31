def sqInRect(x,y):
    out=[]
    if(x==y):
        print(None)
        return
    else:
        while (x<y or y < x):
            if (x < y ):
                out.append(x)
                y=y-x
            elif(y < x):
                out.append(y)
                x=x-y
        out.append(x)
    return out
