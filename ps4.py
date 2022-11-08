def subset(A,B):
        for x in A:
                if x not in B:
                        return False
        return True
def sd(A, B):
        temp = (B.union(A)) - B.intersection(A)
        return temp
