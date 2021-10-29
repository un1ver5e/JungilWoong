#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# print() 연습
# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40 ,50)
print("Hello", "Good", "Morning!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")


# In[4]:


# \를 이용한 특수문자 출력, \n은 newline, \t : tab을 의미
print("\"안녕하세요\"~~~")


# In[1]:


print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")


# In[7]:


# 여러 라인의 문자열 만들기
print("동해물과 백두산이\n마르고 닳도록\n하느님이 보우하사")


# In[6]:


# 여러 라인의 문자열 만들기2
print("""동해물과 백두산이
마르고 닳도록
하느님이 보우하사""")


# In[8]:


a_str = """동해물과 백두산이
마르고 닳도록
하느님이 보우하사"""
print(a_str)


# In[10]:


# 문자열 연산자 : +, *
# 문자열 + 문자열 => 문자열 이어붙이기
# 문자열 * 숫자 => 문자열을 숫자만큼 반복
print("hello" + "python")
print("hello" * 2)
print(2 * "hello")


# In[31]:


# 문자열 index 및 slice => str[0] : 0번지 값, str[1:4] -> start:end / start는 포함, end는 포함하지 않음
str = "안녕하세요"
print(str)
print(str[0], str[2]) # 안 하
print(str[-1], str[-5]) # 요 안
print(str[1:4]) #녕하세
print(len(str)) # len = 길이 함수
# print(str[5]) index error


# In[19]:


# str = "임의로 문자를 넣으세요"
# str의 길이를 구해서 처음 문자를 -인덱스로 구해서 출력하세요
str = "UNIVERSE"
print(str[0], " : ", str[-len(str)])
print(str[3:])
print(str[:3])


# In[33]:


# 변수는 값을 저장하는 공간, 메모리에 방을 만듦 int(값) 정수로 변환, float(), str()
str = 0
pi = 3.14
print(int(pi + 2))
print(pi - 2)
print(pi * 2)

print("string" + "10")


# In[29]:


# 복합 대입 연산자
num = 100; num += 10; num += 20
print("num = ", num) # num=130

str = "abcd"
str += "test"
str *= 2
print("str : ", str) # abcdtestabcdtest


# In[ ]:


# 키보드로부터 입력을 받는 함수 input()
str = input("문자열 입력 > ")
print(str)


# In[43]:


# 문자열을 입력받아 문자열의 길이를 출력하고, 처음 글자와 마지막 글자를 출력하세요
str = input()
length = len(str)
print(length)
print(str[0], str[length-1])


# In[48]:


# 숫자 두개를 입력받아 정수형으로 바꾸고
# 두 수의 사칙연산을 출력하세요
# 문자열을 입력받아 처음 입력받은 숫자만큼 반복해서 출력하세요
num_1 = input("숫자 입력 : ")
num_2 = input("숫자 입력 : ")

inum_1 = int(num_1)
inum_2 = int(num_2)

print(num_1 * inum_1)
print(num_2 * inum_2)

# 두 수의 사칙연산 출력

print(inum_1 + inum_2)
print(inum_1 - inum_2)
print(inum_1 * inum_2)
print(int(inum_1 / inum_2))

