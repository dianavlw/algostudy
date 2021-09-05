Problem Solving:https://www.hackerrank.com/domains/algorithms

----------------------------------------------- Reapeated String ------------------------------------------------
""" Source: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

There is a string, s , of lowercase English letters that is repeated infinitely many times. 
Given an integer, n , find and print the number of letter a's in the first n letters of the infinite string.

Sample Input 0

aba
10
Sample Output 0

7
"""

------------------------------------------------ SOLUTION --------------------------------------------------------------

    def repeatedString(s, n):
    # SOLUTION 1: https://www.youtube.com/watch?v=v4v2GLHivx0&list=PLe_c5cyDuuSDl7VcoDzpC_tRbADQ1xs9T&index=32&t=617s
    l = len(s)
    
    res = (s.count('a') * (n//l)) + s[:n%l].count('a')
    
    return res
    # len_rep = n // l
    # rem = s[:n%l]
    # rep_str =  ((s * len_rep) +rem)
    # count_a = rep_str.count('a')
    # return count_a

    # SOLUTION 2: https://www.youtube.com/watch?v=XWG58qrcB50&t=478s
    l = len(s)
    rep_str = (n//l)
    
    a_count = s.count('a')
    x1= a_count * rep_str  
    x2 = s[:n%l].count('a')
    
    return x1 +x2

    #SOLUTION 3:https://www.youtube.com/watch?v=-PbKDdyo3VY
    total = 0
    for i in s:
        if i == "a":
            total += 1
    
    total = n//len(s) * total
    l = len(s)
    for i in s[:n%l]:
        if i == 'a':
            total += 1
    
    return total     
    
    
    
    """
    s = aba
    n = 10
    char_sum = 0
    for char in s:
        char += s[char]
        char_sum += 1
        if char <= len(n):
            return char_sum
     
    """
    

