#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install mecab_python-0.996_ko_0.9.2_msvc-cp36-cp36m-win_amd64.whl')


# In[3]:


import MeCab
m=MeCab.Tagger()
OUTPUT =m.parse("MeCab 설치를 확인합니다.")
print(OUTPUT)


# In[5]:


get_ipython().system(' pip install JPype1-1.0.2-cp36-cp36m-win_amd64.whl')


# In[3]:


get_ipython().system(' pip install konlpy')


# In[7]:


from konlpy.tag import Kkma
Kkma_pos =Kkma()
out=Kkma_pos.nouns('코엔엘파이 설치를 확인합니다.')


# In[8]:


out


# In[1]:


from konlpy.tag import Mecab
m=Mecab()

# 경로 오류 해결을 위해서 # 가상환경(envs) 속 mecab 경로 변경


# In[2]:


m


# In[ ]:




