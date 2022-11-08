def collatz_function(a):
        if a%2 == 0:
                return a//2
        else:
                return 3*a+1

def collatz_sequence(a):
        b = a
        arr = [b]
        while(b>1):
                b = collatz_function(b)
                arr.append(b)
        return arr
def smallest_int_with_collatz_length(n):
        length = 0
        a = 0
        while(length < n):
                a = a+1
                arr = collatz_sequence(a)
