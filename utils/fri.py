from scipy.spatial.distance import hamming # for fri
import numpy as np
    
#Dag is never empty because a is always distinct from b
def Dag(a,b):  #disagreement set between Boolean vectors of same dimension
    dis=[]
    l=len(a[:-1])            #number of attributes
    for i in range(l):       #list_of_attributes:
        if a[i] != b[i]:     #where we test the equality of attribute value
            dis.append(i)   
    return  dis
     
def hamming_numbers(dim,i,set_of_pairs):  #output also for each hamming dist h, the number of (a,b) s.t. H(a,b)=h
    list_of_numbers=[0]*dim
    for (a,b) in set_of_pairs:         
        dag_set = Dag(a[0:dim],b[0:dim])
        if (i in dag_set):  #only the pairs differing at least on attribute
            hamming = len(dag_set)
            list_of_numbers[hamming]+=1
    return list_of_numbers,list_of_numbers.index(max(list_of_numbers))
    
def Dif_no_weight(dim,i,set_of_pairs, max_distance): #set_of_pairs = a list containing pairs of (a,b)    
    ag_att=0 # number of pairs such that: Dag={attribute} |Dif(i)|
    m_att=0  # number of pairs such that: Dag={attribute} with different label |Dif(i) - Dif_Eq(i)|
    for (a,b) in set_of_pairs: 
        dag_list = Dag(a[0:dim],b[0:dim])
        if i in dag_list: # i is in the disagreement list
            if len(dag_list) <= max_distance: #if the difference of the pair (a,b) is within the max distance
                ag_att+=1  
                if a[dim]!=b[dim]:  #this is where we test equality of label
                    m_att+=1
    #print("no weight")
    return ag_att, m_att # FRI = m_att/ag_att

def Dif_weight_hamming_distance(dim,i,set_of_pairs, max_distance): #set_of_pairs = a list containing pairs of (a,b)    
    ag_att=0 # number of pairs such that: Dag={attribute} |Dif(i)|
    m_att=0  # number of pairs such that: Dag={attribute} with different label |Dif(i) - Dif_Eq(i)|
    for (a,b) in set_of_pairs: 
        dag_set = Dag(a[0:dim],b[0:dim])
        hamming = len(dag_set)
        if i in dag_set: # i is in the disagreement list
            if len(dag_set) <= max_distance: #if the difference of the pair (a,b) is within the max distance
                ag_att+=1  
                if a[dim]!=b[dim]:  #this is where we test equality of label
                    m_att+=1/hamming      
    print("hamming distance weight")
    return ag_att, m_att # FRI = m_att/ag_att

def Dif_weight_hamming_count(dim,i,set_of_pairs,max_distance):
    ag_att=0 # number of pairs differing at least on attribute (could differ otherwise as well)
    m_att=0  # 'number' of pairs differing at least on attribute and with different label |Dif(i)s - Dif_Eq(i)s
    list_of_numbers,max_index=hamming_numbers(dim,i,set_of_pairs)
    for (a,b) in set_of_pairs:         
        dag_set = Dag(a[0:dim],b[0:dim])
        hamming = len(dag_set)
        if (i in dag_set) and (hamming <= max_distance): #lazy evaluation
            ag_att+=1
            if a[dim]!=b[dim]:
                 m_att+=1/(list_of_numbers[hamming] +0.0001) #to avoid zero      
    return ag_att, m_att # FRI = m_att/ag_att     ag_att can be 0 if max_distance is too low wrt the dimension.
    
def fri(dimension,i,set_of_pairs,max_distance):  #return FRI(i) for feature i
    ag_att, m_att = Dif_no_weight(dimension,i,set_of_pairs,max_distance) 
    if ag_att==0:   # all agree on i
        return 0.0
    return m_att/ag_att

def get_fri_scores(dimension,set_of_pairs,max_distance):  #return a list of score per feature
    list_of_numbers_a1,numbers = hamming_numbers(dimension,0,set_of_pairs)
    #print(numbers)
    fri_scores=[]
    for i in range(dimension):
        ratio = fri(dimension,i,set_of_pairs, max_distance)
        fri_scores.append(ratio)
    return fri_scores, list_of_numbers_a1