
def y(x, y):
        return x == y
def n(x, y):
        return x == y and x != 3
def g(x,y):
        return x >= y
def m(x, y):
        return (x + y) % 2
def is_reflexive(A, R):
        setA = []
        for i in A:
                setA.append(i)
                s = []
        for i in setA:
                for j in setA:
                        if R(i,j):
                                s.append((i,j))
        for item in s:
                if item[0] == item[1]:
                        setA.remove(item[0])
        if len(setA) == 0:
                return True
        return False

def is_transitive(A, R):
        for a in A:
                for b in A:
                        for c in A:
                                if R(a,b) and R(b,c) and (not R(a,c)):
                                        return False

        return True


