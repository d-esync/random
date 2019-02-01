import time

while True:
    userinput = input("Name of file: ")
    f=open(userinput+".txt","r")
    aList = f.read().splitlines()
    def heapsort( aList ):
      # convert aList to heap
      length = len( aList ) - 1
      leastParent = length // 2
      for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )
     
      # flatten heap into sorted array
      for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
          swap( aList, 0, i )
          moveDown( aList, 0, i - 1 )
     
     
    def moveDown( aList, first, last ):
      largest = 2 * first + 1
      while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
          largest += 1
     
        # right child is larger than parent
        if aList[largest] > aList[first]:
          swap( aList, largest, first )
          # move down to largest child
          first = largest;
          largest = 2 * first + 1
        else:
          return # force exit
     
     
    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp

    def quickSort(alist2):
       quickSortHelper(alist2,0,len(alist2)-1)

    def quickSortHelper(alist2,first,last):
       if first<last:

           splitpoint = partition(alist2,first,last)

           quickSortHelper(alist2,first,splitpoint-1)
           quickSortHelper(alist2,splitpoint+1,last)


    def partition(alist2,first,last):
       pivotvalue = alist2[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and alist2[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist2[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist2[leftmark]
               alist2[leftmark] = alist2[rightmark]
               alist2[rightmark] = temp

       temp = alist2[first]
       alist2[first] = alist2[rightmark]
       alist2[rightmark] = temp

    


       return rightmark

    def mergeSort(alist3):
        if len(alist3)>1:
            mid=len(alist3)//2
            lefthalf = alist3[:mid]
            righthalf = alist3[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist3[k]=lefthalf[i]
                    i=i+1
                else:
                    alist3[k]=righthalf[j]
                    j=j+1
                k=k+1
            while i < len(lefthalf):
                alist3[k]=lefthalf[i]
                i=i+1
                k=k+1
            while j < len(righthalf):
                alist3[k]=righthalf[j]
                j=j+1
                k=k+1
    alist2= aList
    alist3 = aList
    before = time.time()
    quickSort(alist2)
    now = time.time()
    print("Running time: ", str(round(1000*(now-before))) + "ms" + " QUICK SORT")
    before=time.time()
    heapsort(aList)
    now=time.time()
    print("Running time: ", str(round(1000*(now-before))) + "ms" + " HEAP SORT")
    before = time.time()
    mergeSort(alist3)
    now=time.time()
    print("Running time: ", str(round(1000*(now-before))) + "ms" + " MERGE SORT")
    print("\n\n\n\n")

    
    
    
