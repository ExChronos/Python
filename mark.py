def rsum(L):
    if not L:
        return 0
    else:
        return L[0] + rsum(L[1:])
    
print(rsum([1,2,3,4,5]))

def csum(L, sum):

    for i in L:
        sum += i

csum([1,2,3,4], 0)
print(sum)