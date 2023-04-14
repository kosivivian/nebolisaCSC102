#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Enter value for A")
A = float(input())
print("Enter value for B")
B = float(input())
print("Enter value for C")
C = float(input())

r1 = ((B + ((B**2) - (4*A*C))**(1/2)))/(2*A)
r2 = ((B - ((B**2) - (4*A*C))**(1/2)))/(2*A)
      
print(f"The first root is {r1}")
print(f"The second root is {r2}")


# In[ ]:




