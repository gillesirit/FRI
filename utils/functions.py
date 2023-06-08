############# UTILITIES
def xor(x,y): 
    if (x!=y):
        return 1
    return 0
############# 5 FUNCTIONS TO BE TESTED - ANY DIMENSION >= 20 - arr is an array of values   
#previous name: g5
def g1(arr):
    if ((arr[0]!=0) or (arr[1]!=0) or (arr[2]!=0)) and ((arr[3]!=0) or (arr[4]==0) or (arr[5]!=0)):
        return 1
    return 0

def g2(arr): # generalized XOR - to be different
    if (arr[0]!=arr[1]):
        return 1
    return 0
    
def g3(arr): # XOR combination
    return xor(xor(arr[0],arr[1]),arr[2])

def g4(arr): # using all attributes - all of them have the same FRI
    if sum(arr)==3:
        return 1
    return 0
        
def g5(arr): #using arr[9] to arr[18] - 10 middle features - easy to verify
    return xor(xor(xor(arr[9],arr[10]),xor(arr[11],arr[12])),xor(arr[13],arr[14])) or                    xor(xor(arr[15],arr[16]),xor(arr[17],arr[18]))

def g4_new(arr): # using all attributes - all of them have the same FRI
    if sum(arr)>=3:
        return 1
    return 0

def get_list_relevant_features(f,dimension):
    if f == g1:
        return [1,2,3,4,5,6]
    elif f == g2:
        return [1,2]
    elif f == g3:
        return [1,2,3,4,5,6]
    elif f == g4:
        l=[]
        for i in range(dimension):
            l.append(i+1)
        return l
    elif f == g4_new:
        l=[]
        for i in range(dimension):
            l.append(i+1)
        return l
    else:
        return [10,11,12,13,14,15,16,17,18,19]
    
def get_k_best_features(l,k,real_list):
    sorted_list = sorted(range(len(l)), key=lambda i: l[i], reverse=True)
    # sorted_list will contain the indices of my_list sorted in descending order based on their values
    sorted_my_list = [l[i] for i in sorted_list]
    # sorted_my_list will contain the values of my_list sorted in descending order
    best_k_features=[]
    number_of_correct=0
    for i in range(k):
        best_k_features.append("a_{"+str(sorted_list[i]+1)+"}")   #+1 to get the real attribute name
        if (sorted_list[i]+1) in real_list:
            number_of_correct+=1
    return best_k_features,number_of_correct