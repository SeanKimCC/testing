O(1)

def constantTime(num):
    k = num+num
    if(k == 5):
        return k*2

    for i in range(0,3):
        k += num
        
    return k


O(N)

def linearTime(array):
    
    sumArray = 0
    N = len(array)
    
    for i in range(0, N):
        sumArray += array[i]
        if(sumArray % 3 == 0):
            print("multiple of 3")

    for i in range(0, N):
        sumArray += array[i]
        if(sumArray % 3 == 0):
            print("multiple of 3")
            
    return sumArray


def time(array):

    sumArray = 0
    N = len(array)
    
    for i in range(0,N):
        for j in range(0, N):
            sumArray += array[j]
            
    for j in range(0, N):
            sumArray += array[j]

    return sumArray

O(N^2)



O(10^N)
def ExponentialTime(password):
    N = len(password)
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    if([i,j,k,l] == password):
                        return True
    
    return False



O(log(N))























            
