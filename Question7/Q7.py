#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q7_a
Coord = []
Index = []
L1 = 50
L2 = 57

def solveIndex(pos):
    return (L1 * int(pos[1]) + int(pos[0]))

def solvePos(index):
    return int(index) % L1, int(index) // L1

if __name__ == '__main__':
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt", "r")
    Str = f.read().split('\n')
    for i in range(1, len(Str)-1):
        line = Str[i].split('\t')
        x1 = line[0]
        x2 = line[1]
        Coord.append((x1,x2))
    f = open("C://Users/47634/Desktop/NTU TEST/Question7/output_index_7_1.txt", "w+")
    f.write('index' + '\n')
    for pos in Coord:
        Ans = solveIndex(pos)
        f.write(str(Ans) + '\n')
        #print(Ans)
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt", "r")
    Str = f.read().split('\n')
    for i in range(1, len(Str)-1):
        line = Str[i].split('\t')
        Index.append(line[0])
    f = open("C://Users/47634/Desktop/NTU TEST/Question7/output_coordinates_7_1.txt", "w+")
    f.write('x1\tx2\n')
    for index in Index:
        x1,x2 = solvePos(index)
        f.write(str(x1) + '\t' + str(x2) + '\n')


# In[5]:


#Q7_b

Coord = []
Index = []
L1 = 4
L2 = 8
L3 = 5
L4 = 9
L5 = 6
L6 = 7

def solveIndex(pos):
    return L1 * L2 * L3 * L4 * L5 * pos[5] + L1 * L2 * L3 * L4 * pos[4] + L1 * L2 * L3 * pos[3] + L1 * L2 * pos[2] + L1 * pos[1] + pos[0]


def solvePos(index):
    index = int(index)
    x6 = index // (L1 * L2 * L3 * L4 * L5)
    index = index % (L1 * L2 * L3 * L4 * L5)
    x5 = index // (L1 * L2 * L3 * L4)
    index = index % (L1 * L2 * L3 * L4)
    x4 = index // (L1 * L2 * L3)
    index = index % (L1 * L2 * L3)
    x3 = index // (L1 * L2)
    index = index % (L1 * L2)
    x2 = index // (L1)
    x1 = index % L1
    return x1,x2,x3,x4,x5,x6

if __name__ == '__main__':
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 7/Question 7.2/input_coordinates_7_2.txt", "r")
    Str = f.read().split('\n')
    for i in range(1, len(Str)-1):
        line = Str[i].split('\t')
        x1 = line[0]
        x2 = line[1]
        x3 = line[2]
        x4 = line[3]
        x5 = line[4]
        x6 = line[5]
        Coord.append((int(x1),int(x2),int(x3),int(x4),int(x5),int(x6)))
    f = open("C://Users/47634/Desktop/NTU TEST/Question7/output_index_7_2.txt", "w+")
    f.write('index' + '\n')
    for pos in Coord:
        Ans = solveIndex(pos)
        f.write(str(Ans) + '\n')
    f = open("C://Users/47634/Desktop/NTU TEST/AY20_MBDS_questions/Question 7/Question 7.2/input_index_7_2.txt", "r")
    Str = f.read().split('\n')
    for i in range(1, len(Str)-1):
        line = Str[i].split('\t')
        Index.append(line[0])
    f = open("C://Users/47634/Desktop/NTU TEST/Question7/output_coordinates_7_2.txt", "w+")
    f.write('x1\tx2\tx3\tx4\tx5\tx6\n')
    for index in Index:
        x1,x2,x3,x4,x5,x6 = solvePos(index)
        f.write(str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\t' + str(x5) + '\t' + str(x6) + '\n')


