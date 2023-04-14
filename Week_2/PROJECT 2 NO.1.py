#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Enter the value for A")
A = float(input())
print("Enter the value for B")
B = float(input())
print("Enter the value for C")
C = float(input())
print("Enter the value for D")
D = float(input())
f = B**2
g = B**3

Q = ((3*C) - f)/9
R = ((9*B*C) - (27*D) - (2*g))/54
j = R**2
k = j**(1/2)
S = (R + (Q**3) + k)**(1/3)
T = (R - (Q**3) + k)**(1/3)
     
i = (-1)**(1/2)

r1 = S + T - (1/3 * B)
r2 = (-1/2)*(S + T) - (1/3 * B) + ((1/2*i)*(3**(1/2))*(S - T))
r3 = (-1/2)*(S + T) - (1/3 * B) - ((1/2*i)*(3**(1/2))*(S - T))
     
print(f"the first root = {r1}")
print(f"the second root = {r2}")
print(f"the third root = {r3}")



# In[ ]:




