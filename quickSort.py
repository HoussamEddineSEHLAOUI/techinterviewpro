def quick_sort(A):
    if len(A)==0 :return
    m=len(A)/2+1
    piv=A[m]
    l_upper=[]
    l_small=[]
    for i in range (len(A)):
        if A[i]<=piv : l_small.append(A[i])
        elif A[i]>piv :l_upper.append(A[i])
    return quick_sort(l_small)+piv+quick_sort(l_upper)



print(quick_sort([8,5,4,7,4,5,8,5,4,6,6,2,2,2,0]))

##makhedaaamch