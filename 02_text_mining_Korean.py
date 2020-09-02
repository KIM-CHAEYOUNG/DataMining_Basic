#!/usr/bin/env python
# coding: utf-8

# ### 텍스트 전처리
# - 텍스트를 자연어 처리를 위해 용도에 맞도록 사전에 표준화하는 작업
# - 텍스트 내 정보를 유지, 중복 제거를 통해 분석 효율성을 높이기 위한 전처리 수행과정

# # 1. 토큰화
# - 텍스트 자연어 처리를 위해 분리
# - 단어별 분리를 하는 '단어토큰화(Word Tokenization)'과 문장별 분리 '문장토큰화(Sentenct Tokenization)'
# - 실습에선 단어 토큰화를 "토큰화"로 통일

# In[1]:


# 모든 형태소 분석기 호출
from konlpy.tag import *


# In[4]:


text="인생은 모두가 함께하는 여행이다. 매일매일 사는 동안 우리가 할 수 있는 것 최선을 다해 이 멋진 여행을 만끽하는 것이다."
print(text.split(' '))


# In[6]:


#코모란

from konlpy.tag import Komoran

#선언
komoran =Komoran()

#토큰화 : morphs

komoran_tokens = komoran.morphs(text)
print(komoran_tokens)


# In[9]:


# 한나눔

from konlpy.tag import Hannanum
hannanum = Hannanum()
hannanum_tokens=hannanum.morphs(text)
print(hannanum_tokens)


# In[10]:


#Okt (Twitter tokenizer가 v0.5.0.부터 Okt로 변경)

from konlpy.tag import Okt
okt=Okt()
okt_tokens =okt.morphs(text)
print(okt_tokens)


# In[12]:


#Kkma
from konlpy.tag import Kkma
kkma=Kkma()
kkma_tokens=kkma.morphs(text)
print(kkma_tokens)


# # 2.품사 부착(Pos Tagging)
# - 각 토큰에 품사정보 추가
# - 분석시 불필요한 품사 제거 및 필요한 품사 필터링

# In[13]:


#코모란
komoranTag=[]
for token in komoran_tokens:
    komoranTag +=komoran.pos(token)
print(komoranTag)


# In[14]:


#한나눔
hannanumTag=[]
for token in hannanum_tokens:
    hannanumTag+=hannanum.pos(token)
print(hannanumTag)


# In[15]:


#Okt
oktTag=[]
for token in okt_tokens:
    oktTag+=okt.pos(token)
print(oktTag)


# In[16]:


#Kkma
kkmaTag=[]
for token in kkma_tokens:
    kkmaTag+=kkma.pos(token)
print(kkmaTag)


# # 3. 불용어 처리(Stopword)
# - 자연어 처리를 위해 불필요한 요소 제거
# - 불필요한 품사 제거 작업과 불필요한 단어 제거 작업으로 구성
# - 불필요한 토큰 제거를 통해 연산 효율성을 높임

# In[18]:


#Okt
#최빈어 조회. 최빈어 조회를 통해 불용어 제거 대상 선정

from collections import Counter
Counter(oktTag).most_common()


# In[19]:


# 불용어 처리

stopPos =['Determiner', 'Adverb', 'Conjuction', 'Josa', 'PreEomi', 'Eomi', 'Suffix',         'Punctutation', 'Foreign', 'Alpha', 'Number', 'Unknwon']

stopWord=[]
word=[]
for tag in oktTag:
    if tag[1] not in stopPos:
        if tag[0] not in stopWord:
            word.append(tag[0])
print(word)


# In[20]:


print(okt_tokens)


# In[ ]:




