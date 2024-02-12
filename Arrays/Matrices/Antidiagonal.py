def antidiagonal(arr):
    length=len(arr)

    #visualize the code of result=[[]]*(2*length-1) 
    #there is a difference in this execution
    
    result=[0]*(2*length-1) 
    print(result)
    for i in range(2*length-1):
        result[i]=[]
    

    for i in range(length):
        for j in range(length):
            result[i+j].append(arr[i][j])
            print(result)
    for i in range(2*length-1):
        while len(result[i])<length:
            result[i].append(0)
    print(result)



def temp(A):
    p = len(A[0])
    res = [0]*(2*p-1)
    for i in range((2*p)-1):
        res[i] = []
    for i in range(p):
        for j in range(p):
            res[i+j].append(A[i][j])
    for i in range(2*p-1):
        while len(res[i]) < p:
            res[i].append(0)
    return res

if __name__=="__main__":
    arr=[[1,2,3],[4,5,6],[7,8,9]]
    antidiagonal(arr)
    print(temp(arr))