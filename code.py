#!/bin/python3

import sys
from collections import defaultdict


# Function to compute Longest common subsequence
# Using this max matching character subsequence can be found
# which would give good results on entry level correction of words
# also.
def lcs(X, Y): 
    
    m = len(X) 
    n = len(Y) 

    # 2-D list for storing the longest subsequence
    
    L = [[0]*(n+1) for i in range(m+1)] 

    # Loop and find the lengths
    # the longest value will be at end cell
    
    for i in range(1,m+1): 
        for j in range(1, n+1): 
            
            if X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+ 1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
                    
    # return the longest subsequence
    
    return L[m][n]

    
def work(file, word):

    # A dictionary to store word and it's longest match
    d = defaultdict(int)

    

    # Loop through each word in file
    for i in file.readlines():

        v = i.split(",")[0]
        
        d[v] = lcs(v.lower(), word.lower())

        
            
        # If more than 5 elements in dictionary remove the smallest
        # Since we need top 5
        if len(d.keys())>5:
            # finding  the smallest matched word and its length
            small = len(word)+1
            small_key = -1
            for j in d.keys():
                if d[j]<small:
                    small = d[j]
                    small_key = j
                    
            d.pop(small_key,None)

    # Sort the key value pair based on length
    res = [k for k, v in sorted(d.items(), key=lambda item: item[1])]

    # return a reversed list to get the longest match first
    return reversed(res)
            
    

if __name__ == "__main__":

    # Check if arguments wrong print error
    if len(sys.argv)!=3:
        print("Wrong Input: Look into documentation for proper format")
        exit(0)

    # To prevent error during file read
    # Note: File type is not checked here
    try:
        f_name = sys.argv[1]
        word = sys.argv[2]

        file = open(f_name,'r')

        res = work(file, word)

        # Print output
        for i in res:
            print(i)
            
    except FileNotFoundError:
        print("File Not Found, Kindly check file path and name")
    except Exception:
        print("Error Occured: ",Exception)
