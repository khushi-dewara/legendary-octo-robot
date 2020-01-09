#AIM:Take a sample of 10 phishing e-mails and find the most common words.
# from data set 
from collections import Counter 

#data_set = "phished emails"  
def most_common(dataset , n=10):   
    # split() returns list of all the words in the string 
    split_it = data_set.split() 
    
    # Pass the split_it list to instance of Counter class. 
    count = Counter(split_it) 
    
    # most_common() produces  frequently encountered 
    # input values and their respective counts. 
    most_occur = count.most_common(n) 
    
    print(most_occur)
