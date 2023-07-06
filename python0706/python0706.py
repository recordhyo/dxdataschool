#!/usr/bin/env python
# coding: utf-8

# In[1]:
#키워드 확인 가능
import keyword
print(keyword.kwlist)


# In[2]:
import sys
print(sys.path)


# In[3]:
year = 2023 
#윤년의 조건 - 둘중 하나만 true이면 true
#1. 4의 배수이고 100의 배수가 아닌경우 
#2. 400의 배수인 경우
if (year%100!=0 and year%4==0) or year%400 == 0 :
    print(year, "는 윤년")
else :
    print(year, "는 윤년이 아님")


# In[4]:
year = 2024 
#윤년의 조건 - 둘중 하나만 true이면 true
#1. 4의 배수이고 100의 배수가 아닌경우 
#2. 400의 배수인 경우
if (year%4==0 and year%100!=0) or year%400 == 0  :
    print(year, "는 윤년")
else :
    print(year, "는 윤년이 아님")


# In[5]:
help(print)


# In[6]:
help(input)


