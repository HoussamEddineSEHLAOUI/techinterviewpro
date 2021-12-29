#identify the smalest item in the list and put in the top
#o(n2)

def selection_sort(A):
    for i in range (0 ,len(A)-1):
        minIndex =i
        for j in range(i+1,len(A)):
            if A[j]<A[minIndex]:
                minIndex=j
        if minIndex!=i :
            A[i] , A[minIndex]=A[minIndex],A[i]