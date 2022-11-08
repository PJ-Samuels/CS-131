

def s(x1, x2, x3):
    if(x1 or x2 or x3):
        print("True")
        return True

def n(x1,x2,x3):
    if (x1 and (not x2) and (not x3))or(not x1 and x2 and not x3)or(not x1 and not x2 and x3)or(x1 and x2 and x3):
        print("True")

def ns(x1,x2,x3):
    if (x1 and not x2 and not x3)or(not x1 and x2 and not x3)or(not x1 and not x2 and x3):
        print("True")

def c(x1,x2,x3,y1,y2,y3):
    if(x1 and y1) or (x2 and y2) or (x3 and y3):
        return False
    print("True")
    return True


def isValid(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3):
    if(c(a1,a2,a3,b1, b2, b3)and c(a1, a2, a3,c1, c2, c3,)and c(a1, a2, a3,e1, e2, e3)and c(b1, b2, b3, d1, d2, d3) and 
            c(c1, c2, c3,e1, e2, e3) and c(c1, c2, c3,d1, d2, d3)and c( d1, d2, d3,f1, f2, f3) and c(e1, e2, e3, f1, f2, f3)):
        print("True")
        return True
    return False
