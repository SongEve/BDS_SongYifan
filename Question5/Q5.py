#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Q5_a
R_num = 11
B_num = 14

L = 5

Ans = [['0' for i in range(L)] for j in range(L)]
#Choose color
def Color(x, y):
    global R_num, B_num
    if(B_num>0):
        Ans[x][y] = 'B'
        B_num = B_num - 1
    elif(R_num>0):
        Ans[x][y] = 'R'
        R_num = R_num - 1

if __name__ == '__main__':
#Fill all the position with odd and even coordinates 
    for i in range(L):
        for j in range(L):
            if(i % 2 == 0 and j % 2 == 0):
                Color(i,j)
            if(i % 2 == 1 and j % 2 == 1):
                Color(i,j)
#Fill the rest
    for i in range(L):
        for j in range(L):
            if(i % 2 == 0 and j % 2 == 1):
                Color(i,j)
            if(i % 2 == 1 and j % 2 == 0):
                Color(i,j)
    vout = ''
    for i in range(L):
        for j in range(L):
            vout += Ans[i][j] + ' '
        vout += '\n'
    f=open('C://Users/47634/Desktop/NTU TEST/Question5/output_question_5a.txt', 'w+', encoding='utf8')
    print(vout)
    f.write(vout)
    f.close()
    


# In[13]:


#Q5_b
R_num = 139
B_num = 1451
G_num = 977
W_num = 1072
Y_num = 457

L = 64

Ans = [['0' for i in range(L)] for j in range(L)]

def Color(x, y):
    global R_num, B_num, G_num, W_num, Y_num
    if(R_num>0):
        Ans[x][y] = 'R'
        R_num = R_num - 1
    elif(B_num>0):
        Ans[x][y] = 'B'
        B_num = B_num - 1
    elif(G_num>0):
        Ans[x][y] = 'G'
        G_num = G_num - 1
    elif(W_num>0):
        Ans[x][y] = 'W'
        W_num = W_num - 1
    else:
        Ans[x][y] = 'Y'
        Y_num = Y_num - 1

if __name__ == '__main__':
    for i in range(L):
        for j in range(L):
            if(i % 2 == 0 and j % 2 == 0):
                Color(i,j)
            if(i % 2 == 1 and j % 2 == 1):
                Color(i,j)
    for i in range(L):
        for j in range(L):
            if(i % 2 == 0 and j % 2 == 1):
                Color(i,j)
            if(i % 2 == 1 and j % 2 == 0):
                Color(i,j)
    vout = ''
    for i in range(L):
        for j in range(L):
            vout += Ans[i][j] + ' '
        vout += '\n'
    f=open('C://Users/47634/Desktop/NTU TEST/Question5/output_question_5b.txt', 'w+', encoding='utf8')
    print(vout)
    f.write(vout)
    f.close()
    


# In[ ]:




