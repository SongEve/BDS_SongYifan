#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q6

n = 10   #The degree of polygon
m = 10  #The number of points
poly_points = []  #Points of polygon
segs = []  #Segments of polygon

def judge(x, y):
    cnt = 0
    for i in range(n):
        x1 = segs[i][0][0]
        y1 = segs[i][0][1]
        x2 = segs[i][1][0]
        y2 = segs[i][1][1]
        vec_x = x2 - x1 
        vec_y = y2 - y1
        if(vec_y == 0): continue  
        t = (y - y1) / vec_y
        if(t>1 or t<0): continue
        xx = x1 + t * vec_x
        if(xx<min(x1,x2) or xx>max(x1,x2)): continue
        if(xx<x): continue
        cnt = cnt + 1
    if(cnt%2==1):
        return 1
    else:
        return 0

if __name__ == '__main__':
    #Construct the polygon
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 6/input_question_6_polygon", "r")
    for i in range(n):
        Str = f.readline()
        Str = Str[:-1].split(' ')
        x = int(Str[0])
        y = int(Str[1])
        poly_points.append((x,y))    
    poly_points.append(poly_points[0])
    #Get the segments of the polygon
    for i in range(n):
        segs.append((poly_points[i],poly_points[i+1]))
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 6/input_question_6_points", "r")
    f2 = open("C://Users/47634/Desktop/NTU TEST/Question6/output_question_6.txt", "w+")
    #Get the coordinates of points
    for i in range(m):
        Str = f.readline()
        Str = Str[:-1].split(' ')
        x = int(Str[0])
        y = int(Str[1])
        #Judge
        if(judge(x,y) == 1):
            print(str(x)+' '+str(y)+' '+'inside', file=f2)
        else:
            print(str(x)+' '+str(y)+' '+'outside',file=f2)
    f2.close()


# In[ ]:




