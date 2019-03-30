
#in bubble sort i iterate items in an array and compare them  then swap if a condition is true
def bubble_sort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    print(a)



if __name__== '__main__':
    bubble_sort([4,1,6,85,2,3])
