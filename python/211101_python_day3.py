#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# list 요소 추가, 제거, 변경
a_list = [1, 2, 3]
b_list = [4, 5, 6]

# list 요소 추가
a_list.append('abcd')
print("list append : ", a_list)

# list 요소 추가2
a_list.insert(1, '10')
print("list insert : ", a_list)

# list에 list 추가
a_list.extend(b_list)
print("list extend : ", a_list)

# list 요소 변경
a_list[3] = "변경"
print("list 변경 : ", a_list)

# list 요소 삭제
del b_list[1]
print("b_list del : ", b_list) # [4, 6]

# list 요소 삭제 2
a_list.pop(2)
print("a_list pop : ", a_list) # 인덱스 (2) 삭제

# list 요소 삭제 3
a_list.remove("abcd")
print("a_list remove : ", a_list)

# list 초기화
a_list.clear()
print("a_list : ", a_list)

# list 내부에 요소가 있는지 확인
print(6 in b_list) # true
print(6 not in b_list) # false


# In[ ]:


# for 반복문 : 
# for 변수 in 반복자료:
#     처리문
for i in range(5) :
    print("i: ", i)

a_list = [101, 202, 3, 4, 5]
for element in a_list:
    print("a_list : {}".format(element))
    
for char in "hello python":
    print("-", char)


# In[ ]:


# print 1, 2, 3, 4, 5, 6, 7, 8, 9
list_of_list = [[1, 2, 3],[4, 5, 6, 7],[8, 9]]
for i in list_of_list:
    for x in i:
        print(x)


# In[ ]:


# 딕셔너리에 요소 추가하기
dictionary = {}

print("요소 추가 전 :", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 후 :", dictionary)


# In[ ]:


# dictionary : {카:값, ...}
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아산화나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 사용자로부터 입력
key = input("> 접근하고자 하는 키")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("키가 존재하지 않음")
    
value = dictionary.get(key)
print("키 값 :", value)
if value == None :
    print("키가 존재하지 않음")


# In[ ]:


# 위 셀의 dictionary 딕셔너리의 요소만 출력
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아산화나트륨", "치자황색소"],
    "origin" : "필리핀",
    "items" : {"key1" : "dict test", "value" : "dictvalue"}
}
for i in dictionary:
    print(dictionary[i])


# In[ ]:


# 각 값들만 출력하세요
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아산화나트륨", "치자황색소"],
    "origin" : "필리핀",
    "items" : {"key1" : "dict test", "value" : "dict value"}
}

for key in dictionary:
    if type(dictionary[key]) == dict:
        for sub_key in dictionary[key]:
            print(dictionary[key][sub_key])
    elif type(dictionary[key]) == list:
        for item in dictionary[key]:
            print(item)
    else:
        print(dictionary[key])


# In[ ]:


# range(start_num, end_num, step_num) : start_num부터 end_num-1까지 step_num수만큼 띄워서 숫자를 반복
# range(10) -> start_num = 0, stem_num = 1

array = [273, 45, 103, 54, 101]

for i in range(len(array)):
    print("{}번째 데이터 : {}".format(i, array[i]))
    
print()

# 뒤에서부터 출력
for i in range(len(array)-1, 0-1, -1):
    print("{}번째 데이터 : {}".format(i, array[i]))
    
print()
    
# reversed() 거꾸로 가져오는 함수
for i in reversed(range(len(array))):
    print("{}번째 데이터 : {}".format(i, array[i]))


# In[ ]:


# while 표현식 : 표현식이 true이면 실행
# 실행문 안에 while 문장을 탈출할 수 있는 조건을 실행 or 무한루프[*]
#for i in range(len(array)):
#   print("{}번째 데이터 : {}".format(i, array[i]))

i = 0
while i < len(array):
    print("{}번째 데이터 : {}".format(i, array[i]))
    i += 1`


# In[ ]:


# 비어있는 리스트를 하나 생성한 후 키보드에서 자료를 입력받아 리스트에 추가
# 입력된 입력값이 quit이면 입력 종료 후 입력된 list의 각각의 요소를 출력
list1 = []
text = input("입력 :")

while text != "quit":
    list1.append(text)    
    text = input("입력 :")
    
for char in list1:
    print(char)


# In[ ]:


list1 = []

while True:
    text = input("입력 :")
    
    if text == "quit":
        break # while 문장 종료
    else:
        list1.append(text)
    
list1


# In[ ]:


list1 = []

while True:
    text = input("입력 :")
    
    if text == "quit":
        break # while 문장 종료
        
    list1.append(text)
    
list1


# In[ ]:


# 부호를 입력받아 부호가 'q'이면 프로그램 종료
# 숫자 2개를 입력받아 부호에 따라 계산하는 프로그램 작성 => split(), float()
# 부호는 '+-*/'만 가능하도록 in 연산자 사용
# while 문장 사용, 부호가 +-*/'가 아니면 계속 입력
# 입력값 출력

while True:
    buho = input(" 부호 입력 (\"+, -, *, /\" 종료는 q) > ")
    if buho == "q":
        break
    if buho not in "+-*/":
        continue
    input1 = input("두 수를 입력: ").split()
    
    if buho == "+":
        result = int(input1[0]) + int(input1[1])
        
    elif buho == "-":
        result = int(input1[0]) - int(input1[1])
        
    elif buho == "*":
        result = int(input1[0]) * int(input1[1])
        
    else:
        result = int(input1[0]) / int(input1[1])
        
    print("{} {} {} = {}".format(input1[0], buho, input1[1], result))


# In[ ]:


# 피보나치 수열
x, y = 0, 1

for i in range(182):
    x, y = y, x + y
    z = y / x
    #print(z)
    print("{} {} {:.50f}".format(x, y, z))


# In[ ]:


# min(매개변수), max(), sum() : 매개변수 -> list
a_list = [34, 54, 78, 100, 320, 43]
print("min : {}, max : {}, sum : {}".format(min(a_list),max(a_list),sum(a_list)))
print(min(30, 50, 20))


# In[ ]:


# reversed() : 리스트 뒤집기
print("a_list : {}, a_list_reversed : {}".format((a_list), list(reversed(a_list))))


# In[ ]:


# enumerate() : 인덱스와 값을 반환
for i, value in enumerate(a_list):
    print("{}번째 요소 {}".format(i, value))


# In[ ]:


dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아산화나트륨", "치자황색소"],
    "origin" : "필리핀",
    "items" : {"key1" : "dict test", "value" : "dict value"}
}

# for key in dictioany:
#     print(dict_a[key])

for key, value in dictionary.items():
    # print("key : {}, value : {}".format(key, value))
    if type(value) == dict:
        for key1, value1 in value.items():
            print(value1)
    elif type(value) == list:
        for item in value:
            print(item)
    else:
        print(value)


# In[ ]:


# 키보드에서 이름을 입력받아 리스트에 저장한 후(입력 시 'q'를 입력하면 종료)
# 검색하고자 하는 이름을 입력받아 몇번째 입력된 이름인지 출력하세요
# enumerate 함수 사용

list2 = []

while True:
    input2 = input("이름 : ")
    
    if input2 == "q":
        break
    list2.append(input2)

s_name = input("검색 : ")
for idx, name in enumerate(list2):
    if name == s_name:
        print("{}번째 등록된 {} 입니다.".format(idx+1, name))
        break
        
# 입력된 이름 갯수만큼 점수를 입력하여 score[] 리스트에 저장하세요.
# 저장된 이름과 점수를 출력 : 홍길동 90, 김철수 100
# 딕셔너리로 변환해서 출력
score = []
i = 0

while i < len(input2):
    score.append(int(input("점수 입력 :")))
    i += 1
    
for index in range(len(list2)):
    print("{} : {}".format(list2[index], score[index]))

dict_score = {}
i = 0

while i < len(list2):
    dict_score[list2[i]] = score[i]
    i += 1
    
print("dict_score : ")

for key, value in dict_score.items():
    print("{} : {}".format(key, value))


# In[ ]:


###### 키보드에서 이름을 입력받아 리스트에 저장한 후 (이름에 'q'가 입력되면 입력 종료)
# 검색하고자 하는 이름을 입력받아 몇번째 입력된 이름인지 출력 하세요
# enumerate 함수를 이용 
input_name = []
while True:
    input_str = input("이름 입력 ( 종료는 q) > ")
    if input_str == 'q':
        break
    input_name.append(input_str)
search_name = input("검색하고자 하는 이름 입력 > ")
for idx, name in enumerate(input_name):
    if name == search_name:
        print("{}번째 데이터는 {} 입니다".format(idx+1, name))
        break
# 입력된 이름의 갯수만큼 점수를 입력하여 score[] 리스트에 저장하세요
# 저장된 이름과 점수를 출력 : 홍길동 90   김철수 100
# 딕셔너리로 변화해서 출력
score = []; i = 0
while i < len(input_name):
    score.append(int(input("점수 입력 :")))
    i+=1
print("input_name[] : score[]")
for idx in range(len(input_name)):
    print("{} : {}".format(input_name[idx], score[idx]))
dict_score = {}; i = 0
while i < len(input_name):    # list를 dict로 변형 키 리스트와 값 리스트를 활용하여
    dict_score[input_name[i]] = score[i]
    i += 1    
print("dict_score : ")
for key, value in dict_score.items():   # 딕셔너리 출력 
    print("{} : {}".format(key, value))


# In[ ]:


# list 내포는 [표현식 for 반복자 in 반복자료]
array = []
for i in range(0, 20, 2): # 2씩 증가하면서 20번
    array.append(i * i)
print(array)

array1 = [i * i for i in range(0, 20, 2)]
print(array1)

array2 = [i for i in range(100) if i % 5 == 0] # 조건에 맞는 자료만 리스트로
print(array2)


# In[ ]:


# 키보드에서 자료를 입력받아 한글자씩 리스트에 저장한 후
# 문자만 리스트로 출력

input_str = list(input("입력 :"))
str_list = [ char for char in input_str if char.isalpha()]
print(str_list)

# for char in input_str:
#     if char.isalpha():
#         str_list.append(char)


# In[ ]:


# 문자열.join(문자열로 구성된 리스트)
join_char = "::".join(["1", "2", "3"])
print(join_char)

# 이더레이터
numbers = [1, 2, 3, 4, 5]
r_num = reversed(numbers) # r_num은 위치만 저장, data를 가져오는 방법은 next 함수
print(next(r_num))

print("first")
for i in r_num:
    print(i)
print("second")
for i in r_num:
    print(i)


# In[ ]:


# def 함수명() : 괄호 안에 매개변수 return 값 있을 수도 있고 없을 수도 있음
def print_function():
    print("function test")
    
def print_n_times(value, n):
    for i in range(n):
        print(value)
        
def print_times(value, n=3): # 기본 매개변수
    for i in range(n):
        print(value)
        
def print_var_times(n, *values): # 가변 매개변수
    for i in range(n):
        for value in values:
            print(value)
            
def print_var_basic_times(*values, n=3): # 가변 매개변수, 기본 매개변수
    for i in range(n):
        for value in values:
            print(value)
    
print_function()
print_n_times("test", 2)
print_times("test123")
print_var_times(2, "abcd", "test", 123) # n은 3으로
print_var_basic_times("abcd", "test", 123)


# In[ ]:


# range 함수
def sum_func(start = 0, stop = 100, step =1):
    tot = 0
    for i in range(start, stop + 1, step):
        tot += i
    return tot

print(sum_func(1, 1000, 2))
print(sum_func())


# In[6]:


# 키보드에서 입력받는 함수를 : 숫자와 부호를 입력받아 list로 반환하는 함수, "q"는 종료
# 부호가 "+"이면 합
# 부호가 "-"이면 차

def input_data():
    input_list = input("10 + 20 의 형식으로 입력 :").split() # input_list는 이 함수에서만 사용
    return input_list

def convert_int(val1):
    if type(val1) != int:
        val1 = int(val1)
        return val1

def plus_func(num1, num2):
#    if type(num1) != int:
#        num1 = int(num1)
    convert_int(num1)
    convert_int(num2)
    return num1 + num2

def minus_func(num1, num2):
    return num1 - num2


# In[ ]:


while True:
    input_list = input_data() # 서로 다른 방의 개념
    if "q" in input_list:
        break
    if input_list[1] == "+":
        result = plus_func(input_list[0], input_list[2])
    elif input_list[1] == "-":
        result =  minus_function(int(input_list[0]), int(input_list[2]))
        
    print("{} {} {} = {}".format(input_list[0], input_list[1], input_list[2], result))


# In[4]:


val1 = "1"

def convert_int(val1):
    if type(val1) != int:
        val1 = int(val1)
        return val1

print(type(convert_int(val1)))

