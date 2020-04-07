def LinearSearch(sortedList, target):
    for i in range(0, len(sortedList)):
        print(sortedList, sortedList[i])
        if(sortedList[i] == target):
            return
        

def BinarySearch(sortedList, target):
    print("Start binary search")
    
    while(True):
        middle = len(sortedList)//2
        print(sortedList, sortedList[middle])
        if(sortedList[middle] == target):
            return True
        elif(sortedList[middle] < target):
            sortedList = sortedList[(middle+1):]
        else:
            sortedList = sortedList[:middle]

numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]



LinearSearch(numList, 17)
BinarySearch(numList, 17)
