#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

k1=100    #um/min
k2=600
k3=150
E_ini=1  #um
S_ini=10
ES_ini=0
P_ini=0

h=0.0008
Pv_ini = 0

def fun_E(t,E,S,ES):
    Ve = -k1*E*S+(k2+k3)*ES
    return Ve

def fun_S(t,E,S,ES):
    Vs = -k1*E*S+k2*ES
    return Vs

def fun_ES(t,E,S,ES):
    Ves = k1*E*S-(k2+k3)*ES
    return Ves

def fun_P(t,ES):
    Vp = k3*ES
    return Vp

def RK_4(t,E_ini,S_ini,ES_ini,P_ini,h,Pv_ini):
    E_list=[]
    E_list.append(E_ini)
    S_list=[]
    S_list.append(S_ini)
    ES_list=[]
    ES_list.append(ES_ini)
    P_list=[]
    P_list.append(P_ini)
    Pv_list=[]
    Pv_list.append(Pv_ini)
    
    t =1
    n =0
    Pv_max = 0
    while(n < 500):
        t= t + h
        
        k1_E = fun_E(t,E_ini,S_ini,ES_ini)
        k1_S = fun_S(t,E_ini,S_ini,ES_ini)
        k1_ES = fun_ES(t,E_ini,S_ini,ES_ini)
        k1_P = fun_P(t,ES_ini)
        
        k2_E = fun_E(t+h/2,E_ini+k1_E*h/2,S_ini+k1_S*h/2,ES_ini+k1_ES*h/2)
        k2_S = fun_S(t+h/2,E_ini+k1_E*h/2,S_ini+k1_S*h/2,ES_ini+k1_ES*h/2)
        k2_ES = fun_ES(t+h/2,E_ini+k1_E*h/2,S_ini+k1_S*h/2,ES_ini+k1_ES*h/2)
        k2_P = fun_P(t+h/2,ES_ini+k1_ES*h/2)
        
        k3_E = fun_E(t+h/2,E_ini+k2_E*h/2,S_ini+k2_S*h/2,ES_ini+k2_ES*h/2)
        k3_S = fun_S(t+h/2,E_ini+k2_E*h/2,S_ini+k2_S*h/2,ES_ini+k2_ES*h/2)
        k3_ES = fun_ES(t+h/2,E_ini+k2_E*h/2,S_ini+k2_S*h/2,ES_ini+k2_ES*h/2)
        k3_P = fun_P(t+h/2,ES_ini+k2_ES*h/2)
      
        k4_S = fun_S(t+h/2,E_ini+k3_E*h,S_ini+k3_S*h,ES_ini+k3_ES*h)
        k4_E = fun_E(t+h/2,E_ini+k3_E*h,S_ini+k3_S*h,ES_ini+k3_ES*h)
        k4_ES = fun_ES(t+h/2,E_ini+k3_E*h,S_ini+k3_S*h,ES_ini+k3_ES*h)
        k4_P = fun_P(t+h/2,ES_ini+k3_ES*h)
        
        E = E_ini  + h*(k1_E  + 2*k2_E + 2*k3_E + k4_E) / 6
        S = S_ini  + h*(k1_S  + 2*k2_S + 2*k3_S + k4_S) / 6
        ES= ES_ini + h*(k1_ES + 2* k2_ES + 2 * k3_ES + k4_ES) / 6
        P = P_ini  + h*(k1_P  + 2*k2_P + 2*k3_P + k4_P) / 6
           
        E_ini = E
        E_list.append(E)
        S_ini = S
        S_list.append(S)
        ES_ini = ES
        ES_list.append(ES)
        P_ini = P
        P_list.append(P)
        Pv_list.append(fun_P(t,ES_list[n+1]))
        Pv_temp = Pv_list[-1]
      
        if(t == 0):
            Pv_max = Pv_list[-1]
        if(t > 0 and Pv_temp > Pv_max):
            Pv_max = Pv_list[-1]     
        n = n + 1 
        
    return E_list,S_list,ES_list,P_list,Pv_list,Pv_max
        
if __name__ == '__main__':
    E_list,S_list,ES_list,P_list,Pv_list,Pv_max = RK_4(0,E_ini,S_ini,ES_ini,P_ini,h,Pv_ini)
    plt.figure(figsize=(12, 8))
    plt.plot(E_list,label='E') 
    plt.plot(S_list,label='S') 
    plt.plot(ES_list,label='ES') 
    plt.plot(P_list,label='P') 
    plt.title('Enzyme Reaction')
    plt.xlabel('n')
    plt.ylabel('Concentration')
    plt.legend()
    plt.show()
    plt.figure(figsize=(12, 8))
    plt.plot(S_list,Pv_list,color='red') 
    plt.title('Velocity of P')
    plt.xlabel('concentration of S')
    plt.ylabel('Vp')
    plt.show()
    print( Pv_max) 
    





