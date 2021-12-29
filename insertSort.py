def insertion_sort(A) :
    for i in range(1,len(A)):
        j=i-1
        while A[j]>A[j+1] and j>=0 :
            A[j] ,A[j+1]=A[j+1],A[j]
            j-=1
    return A



#o(n) in compli
#si la petit val se trouve a la fin de la liste !!!
print(insertion_sort([98,56,45,54,2,1,0]))



