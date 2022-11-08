def are_parts_nonoverlapping(p):
        for i in range(len(p)):
                for j in range(i+1, len(p)):
                        res = p[i].intersection(p[j])
                        if(len(res)==0):
                                return True
        return False
def do_parts_contain_element(x, p):
        for i in range(len(p)):
                if(x in p[i]):
                        return True
        return False
def do_parts_cover_set(s, p):
        for i in s:
                f = 0
                for j in range(len(p)):
                        if i in p[j]:
                                f = 1
                if f==0:
                        return False
        return True
def do_parts_have_nothing_extra(s, p):
        for i in range(len(p)):
                for j in p[i]:
                        if j not in s:
                                return False
        return True
def is_partition(s,p):
        ans=set()
        c=0
        for i in p:
                ans=ans | i
        if ans == s:
                c=1
        else:
                return False

        for i in range(0,len(p)):
                for j in range(i+1,len(p)):
                        if len(list(p[i] & p[j]))!=0:
                                return False
        return True