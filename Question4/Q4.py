#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q4_4_Connectivity
n = 10
m = 20
cnt = 1
map = [[0 for i in range(m)] for j in range(n)]
vis = [[0 for i in range(m)] for j in range(n)]
dx = [0,1,0,-1] 
dy = [1,0,-1,0]

def dfs(x, y, num):
    #Using the vis to avoid the double mark
    if vis[x][y] == 1: return
    vis[x][y] = 1
    map[x][y] = num
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if(xx<0 or xx>=n): continue
        if(yy<0 or yy>=m): continue
        if(map[xx][yy] != 0):
            dfs(xx,yy,num)

if __name__ == '__main__':
    f = open('C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 4/input_question_4', "r")
    #Assign the input to the 2D array
    for i in range(n):
        for j in range(m):
            ch = f.read(1)
            while ch == ' ': ch=f.read(1)
            while ch == '\n': ch=f.read(1)
            while ch == '\t': ch=f.read(1)
            map[i][j] = int(ch)
    #visit each element       
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and map[i][j] != 0:
                dfs(i,j,cnt)
                cnt = cnt + 1
    f = open("C://Users/47634/Desktop/NTU TEST/Question4/output_question_4.txt", "w+")
    for i in range(n):
        for j in range(m):
            f.write(str(map[i][j]) + '\t')
        f.write("\n")

