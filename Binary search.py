pos=-1

def search(list,n):

    i=0
    u=len(list)-1

    while i<=u:
        mid=(1+u) //2

        if list(mid) == n:
            globals()['pos']=mid
            return True
        else:
            if list(mid)<n:
              i=mid+1
            else:
              u=mid-1
    return False


list=[4,7,8,12,45,99,7388,9238,3898,2888]
n=3
if search(list , n):
    print('found at ', n)
else:
    print('not found')