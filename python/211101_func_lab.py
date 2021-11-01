#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 이름과 성적을 입력받아 딕셔너리에 저장한 후 이름을 키로 성적을 값으로(input_data())
# 이름에 "q"가 입력되면 입력 종료
def input_data(dict_score):
    input_str = input("name score > ").split()
    if "q" in input_str:
        return False
    dict_score[input_str[0]] = int(input_str[1])
    return True

# 검색할 이름 입력
def search_name(s_name, dict_score):
    for name in dict_score:
        if name == s_name:
            return dict_score[name]
    return None

def sum_func(dict_score):
    total = 0
    for key, value in dict_score.items():
        total += value
    return total

def avg_func(dict_score):
    return sum_func(dict_score) / len(dict_score)


# In[4]:


# 자료 입력
dict_score = {}
while True:
    if not input_data(dict_score):
        break


# In[5]:


# 1. 검색할 이름 입력 : 해당 이름의 성적 출력, 없으면 자료 없음 출력 (search_func())
s_name = input("검색할 이름 > ")
s_score = search_name(s_name, dict_score)
if s_score:
    print("{}의 점수 {}".format(s_name, s_score))
else:
    print("자료 없음")


# In[6]:


# 2. 전체 학생의 인원수, 총점과 평균을 출력 (sum_func(), avg_func())
print("인원수 : {}, 총점 : {}, 평균 : {:3.2f}".format(len(dict_score), sum_func(dict_score), avg_func(dict_score)))

