
def reverse_array(a):
    #take the size of the array minus one because array starts at zero
    right = len(a)- 1

    #initializing left as 0
    left = 0

    while left<right:
        #perform swapping
        # left is zero in a[left] which means first item of the array
        # right is 4 as its index of the last item 5
        # performing swapping ie 1,5 = 5,1 then increment
        a[left],a[right]= a[right], a[left]
        left+=1
        right-=1
    print(a)


if __name__ == "__main__":
    reverse_array([1,3,4,5])