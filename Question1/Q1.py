#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1_a


def solve(n, m, sum):
    vout = str(sum) + ' '
    res = m * (m + 1) /2 + n - 1 
    sum = sum - res 
    step = m + n - 2 
    ans = []
    #Path that needs to be adjusted
    for i in range(m - 1, 0, -1): 
        num = sum // i 
        sum = sum % i
        for j in range(int(num)):
            ans.append('R') 
        ans.append('D')
        step = step - (num + 1)
    #Path that does not need to be adjusted
    for i in range(int(step)):
        ans.append('R')
    #Output reversly 
    for i in range(len(ans), 0, -1):
        vout += str(ans[i-1])
    f.write(vout+"\n")
    
  
if __name__ == '__main__':
    f=open('C://Users/47634/Desktop/NTU TEST/Question1/output_question_1a.txt', 'w+', encoding='utf8')
    solve(9, 9, 65)
    solve(9, 9, 72)
    solve(9, 9, 90)
    solve(9, 9, 110)
    f.close()


# In[6]:


#Q1_b

def solve(n, m, sum):
    vout = str(sum) + ' '
    res = m * (m + 1) /2 + n - 1 
    sum = sum - res 
    step = m + n - 2 
    ans = []
    for i in range(m - 1, 0, -1): 
        num = sum // i 
        sum = sum % i
        for j in range(int(num)):
            ans.append('R') 
        ans.append('D')
        step = step - (num + 1)
    for i in range(int(step)):
        ans.append('R')
    for i in range(len(ans), 0, -1):
        vout += str(ans[i-1])  
    f.write(vout+"\n")
    
  
if __name__ == '__main__':
    f=open('C://Users/47634/Desktop/NTU TEST/Question1/output_question_1b.txt', 'w+', encoding='utf8')
    solve(100000, 90000, 5994891682)
    solve(100000, 90000, 87127231192)
    f.close()

