-------------------------------------------- Arrays - Sparse Arrays. --------------------------------------------

There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.

def matchingStrings(strings, queries):
    # Write your code here
    res = []
    
    for i in range(len(queries)):
        counter = 0
        for j in range(len(strings)):
            if queries[i]==strings[j]:
                counter+= 1
        res.append(counter)
    return res 




Problem Solving:https://www.hackerrank.com/domains/algorithms
