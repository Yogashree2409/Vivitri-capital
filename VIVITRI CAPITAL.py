#!/usr/bin/env python
# coding: utf-8

# <H1>
# Question 1
# <H1>

# In[2]:


import operator 

text_line = input("Type in: ") 

freq_dict = {} 

for i in text_line.split(' '):
    
    if i.isalpha():
        
        if i not in freq_dict: 
            freq_dict[i] = 1 
        
        elif i in freq_dict: 
            freq_dict[i] = freq_dict[i] + 1 
        
        else:
            pass 

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))

print(sorted_freq_dict) 

for i in sorted_freq_dict: 
    print(i[0], i[1])


# <H1>
# Question 2
# <H1>

# In[4]:


import re
passwords = input("Type in: ")
passwords = passwords.split(",")
accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))


# <h1>
# Question 3
# <H1>

# In[6]:


m=int(input("Row:"))

n=int(input("Column:"))

matrix=[[0 for col in range(n)] for row in range(m)]

for row in range(m):
    
    for col in range(n):
        
        matrix[row][col]=row*col

print(matrix)


# <H1>
# Question 4
# <H1>

# In[7]:


def string_a(a, str):
     
    string = []
     
    text = str.split(" ")
     
    for x in text:
         
        
        if len(x) > a:
             
            string.append(x)
             
    return string
 
 

a = 6
str ="learn programming at include help"
print(string_a(a, str))


# <H1>
# Question 5
# <H1>

# In[10]:


from re import sub

def camel_case(s):
  
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])

print(camel_case('Hello world'))


# <H1>
# Question 6
# <H1>

# In[14]:


def uncommon(s1,s2):
  s1=s1.split()
  s2=s2.split()
  k=set(s1).symmetric_difference(set(s2))
  return k

a = input()
b = input()
print(list(uncommon(a,b)))


# <h1>
# Question 7
# <H1>

# In[15]:


for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()


# <h1>
# Question 8
# <H1>

# In[11]:


rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(1, i - 1):
        print(j, end=' ')
        if(j<i-2):
            print("*",end=' ')
    print(" ")


# <H1>
# Question 9
# <H1>

# In[13]:


rows = 6

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
print("\n")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# In[ ]:




