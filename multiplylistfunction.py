def lstmulti() :
    lst=(10,20,4,4,3)
    global answer
    for i in lst :
       
        answer = i * answer
        return answer
        print(answer)
lstmulti()