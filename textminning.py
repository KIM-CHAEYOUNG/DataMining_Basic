#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url="https://www.forbes.com/sites/adrianbridgwater/2019/04/15/what-drove-the-ai-renaissance/#69156bba1f25"

response = requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser') # 텍스트 내용 추출
print(soup)


# In[17]:


# 전체 'p'태그를 가져오면 안됨
# 리스트값으로 나오기 때문에 하나의 'p'씩 찾아야함
title=soup.find('p')
title


# In[38]:


# 크롤링 영역에서 클래스 태그 문 복붙 가능


# In[20]:


title2=soup.find('p')
title2.text


# In[22]:


p_tag = soup.find_all('p')
content=''
for i in p_tag:
    content+=i.text
content[:500]


# # 영문토큰화

# In[23]:


# 영문토큰화 nltk 패키지 설치
get_ipython().system(' pip install nltk')


# In[24]:


# word tokenize
#string type으로 넣을 것
import nltk

nltk.download("punkt")
from nltk.tokenize import word_tokenize
token1 =word_tokenize(content)
print(token1[:20])


# In[26]:


# WordPunctTokenizer() : 알파벳이 아닌 문자 구분 토큰화
import nltk
from nltk.tokenize import WordPunctTokenizer
token2=WordPunctTokenizer().tokenize(content)
print(token2[:20])


# In[29]:


#TreebankWordTokenizer() : 정규표현식에 기반한 토큰화
import nltk
from nltk.tokenize import TreebankWordTokenizer
token3= TreebankWordTokenizer().tokenize(content)
print(token3[:20])


# # 영문 품사부착

# In[31]:


from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')


# In[32]:


taggedToken =pos_tag(token1)
print(taggedToken[:20])


# # 영문 개체명인식

# In[33]:


nltk.download('words')
nltk.download('maxent_ne_chunker')


# In[34]:


import nltk 
nltk.download('punkt')
from nltk.tokenize import word_tokenize


# In[37]:


#토큰화
token1=word_tokenize("Barack Obana likes fried chicken very much")
print('token1', token1)

taggedToken = pos_tag(token1)
print('pi=os_tag', taggedToken)

from nltk import ne_chunk
neToken = ne_chunk(taggedToken)
print(neToken)


# In[ ]:




