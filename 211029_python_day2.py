#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 키보드로부터 입력을 받아 해당 문자열을 출력하고 길이를 구하세요

input_str = input("문자입력 : ")

print("입력받은 문자 : ", input_str)
print("입력받은 문자열의 길이는 : ", len(input_str))


# In[ ]:


"문자입력".format()


# In[9]:


# format : {}에 값을 대입
print("{}".format(10)) # 10
print("{} {} {}".format(10, 'test', 20))

print("입력받은 문자 : {}, 문자열의 길이는 : {}".format(input_str, len(input_str)))


# In[18]:


# 정수 자리수 지정하기
num = 52

print("{:d}".format(num))
print("{:5d}".format(num))
print("{:5d}".format(num*-1))
print("{:05d}".format(num))
print("{:05d}".format(num*-1))


# In[20]:


# 부호 붙이기 "+"
# :다음 공란일 때 음수만 - 표시 됨
print("{:+d}".format(num)) + 52
print("{:+d}".format(num * -1)) # -52
print("{: d}".format(num)) # 52
print("{: d}".format(num * -1)) # -52


# In[24]:


# 조합하기
print("{:+5d}".format(num)) # 공란5개 +52
print("{:+5d}".format(num * -1)) # 공란5개 -52
print("{:=+5d}".format(num)) # +공란5개52
print("{:=+5d}".format(num * -1)) # -공란5개52
print("{:=+05d}".format(num)) # +0052
print("{:=+05d}".format(num * -1)) # -0052


# In[27]:


# 부동 소수점 출력 {:f}
numf = 52.273
print("{:f}".format(numf)) # 52.273000
print("{:15f}".format(numf)) # 52.273000 전체 표현하는 자리수가 15자리
print("{:+15f}".format(numf)) # +52.273000 전체 표현하는 자리수가 15자리
print("{:+015f}".format(numf)) # +52.273000 전체 표현하는 자리수가 15자리이고 공란에 0

# 소수점 미만 표현 자리수 지정
print("{:15.3f}".format(numf)) # 전체 표현 자리수는 15, 소수점 미만 3자리

# 의미없는 소수점 미만 0 제거하기
print("{:g}".format(10.0)) # 10


# In[38]:


# 문자열.원하는 함수(메서드)
# upper() - 대문자로 , lower() - 소문자로, strip() - 공백제거 
stra = "    Hello World !!     "
print(stra.upper()) # 대문자로
print(stra.lower()) # 소문자로
print('/', stra.strip(), '/') # 양쪽 공백 제거
print('/', stra.lstrip(), '/') # 왼쪽 공백 제거
print('/', stra.rstrip(), '/') # 오른쪽 공백 제거

# 소문자로 바꿔서 공백 제거
print(stra.lower().strip())


# In[45]:


# 문자열 구성 파악하기 => is함수명()
print("Translate".isalnum()) #true
print("10".isdigit()) #true
print("False".isidentifier()) #식별자로 사용할 수 있는 것인지 true
print("import".isdecimal()) # 10진수인지 false
print("i m p o r t".isspace()) # 공백으로만 만들어져있는지 false
print("I M P o r t". islower()) # 소문자로만 구성돼 있는지 false


# In[48]:


# find(), rfind() : 문자열 인덱스 반환
ipstr = "abcd hellohello python" # 처음 나오는 hello를 추출해서 출력
startindex = ipstr.find("hello") # 처음 hello 인덱스 반환
endindex = ipstr.rfind("hello") # 위에서부터 검색해서 처음 나오는 hello 인덱스 반환

print("시작위치 : {}. 마지막 위치 : {}, {}".format(startindex, endindex, ipstr[startindex:endindex]))

# 마지막 위치의 hello뒤에 있는 문자 모두 출력
print(ipstr[endindex:])


# In[57]:


# 키보드에서 공백 포함해서 문자열을 입력 받아
# 처음 공백이 나오는 위치 까지의 문자만 출력

keyinput = input("입력하세요 : ")
print(keyinput[:keyinput.find(" ")])

# 함수명() : len(), print(), type()
# 오브젝트.함수명() -> 클래스 (멤버변수, 메서드(함수)) : object.upper(), object.lower(), object.format()


# In[75]:


# 문자열 자르기 object.split() => list로 반환
spstr = "10 20 30 40 test abcd"
print(spstr.split())
spstr1 = "10,20,30,40,test,abcd"
print(spstr1.split(","))

"10" in spstr1 # true 이거나 false


# In[68]:


# 키보드로부터 데이터를 입력받아 공백으로 데이터를 분리하고 두번째 자료를 출력
# abcd test c 10 30 => test를 출력

kinput = input("입력하세요 : ")
inputsplit = kinput.split()
print(inputsplit[1])


# In[73]:


# and, or, not, ==, !=, >, <, >=, <=
a = 10; b = 20
print(a == b) # false
print(a != b) # true
print(a < b) # false
print(a > b) # true
print(a <= b) # true
print(a >= b) # false
print(a == 10 and b == 20) # true
print(a != 10 and b == 20) # false
print(a == 10 and b != 20) # false
print(a != 10 and b != 20) # false
print(a == 10 or b == 20) # true
print(a != 10 or b == 20) # true
print(a == 10 or b != 20) # true
print(a != 10 or b != 20) # false
print(not (a != 10 or b != 20)) # true


# In[76]:


# if 조건식:
#     들여쓰기

if True:
    print("if 문장 실행") # 실행 됨
    
if False:
    print("if false 실행") # 실행 안 됨


# In[83]:


# 정수를 입력 받아 10보다 작으면 입력된 값 출력
# 1. 정수를 입력 받음
# 2. 숫자인지 확인 isdecimal()
# 3. 숫자이면 문자를 숫자로 변경
# 4. 10보다 작으면 출력

inputstr = input("정수를 입력하세요 : ")

if inputstr.isdecimal(): # 입력된 자료가 숫자인지 파악
    inputstr = int(inputstr) # 자료형을 integer로 변환
    if inputstr < 10: # 입력돈 자료가 10보다 작은지 비교
        print("inputstr : {:5d}".format(inputstr)) # 모든 조건이 만족했을 경우 출력
        
print("end")


# In[85]:


# 숫자를 입력받아 실수로 변환
# 0보다 크면 양수, 0보다 작으면 음수, 0이면 "zero를 출력"

iptint = float(input("정수 입력 > "))

if iptint > 0 :
    print("양수")
if iptint < 0 :
    print("음수")
if not iptint : # 숫자인 경우 0이면 false, 문자인 none(null)인 경우 false
    print("Zero")


# In[88]:


# 날짜 시간 관련 함수를 사용하기 위해서 datetime 모듈 import
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))


# In[108]:


# 정수를 입력 받아 짝수인지 확인 -> 마지막 입력된 숫자가 0, 2, 4, 6, 8
inputnum = input("정수 입력 > ")
lastchar = inputnum[-1] # 마지막 글자를 가져옴
lastnum = int(lastchar) # 정수형으로 데이터 타입 변경

if lastnum == 0 or lastnum == 2 or lastnum == 4 or lastnum == 6 or lastnum == 8:
    print("짝수입니다.")
    
if lastnum == 1 or lastnum == 3 or lastnum == 5 or lastnum == 7 or lastnum == 9:
    print("홀수입니다.")

# int로 형변환 후 2로 나눈 나머지 값이 0이면 짝수, 1이면 홀수
intnum = int(inputnum)
if not intnum % 2:
    print("짝수입니다")
if intnum % 2:
    print("홀수입니다")
    
# in 연산자를 활용하여 처리
if lastchar in "02468":
    print("짝수입니다")
if lastchar in "13579":
    print("홀수입니다")


# In[144]:


# 1. 한번에 두개의 숫자를 입력받아(구분자 " ") 작은수 부터 출력
# 2. 작은 수와 큰 수가 각각에 대하여 
# 3. 3의 배수이면 "3의 배수", 아니면 "3의 배수가 아닙니다"
# 57 34 입력 -> 입력된 숫자는 34와 57입니다.
# 34는 3의 배수가 아닙니다. 57은 3의 배수입니다.

input1 = input("입력 > ")
num1 = input1.split(' ')
vn1 = int(num1[0])
vn2 = int(num1[1])

if vn1 > vn2:
    print("입력된 숫자는 {}, {}입니다.".format(vn2, vn1))
if not vn1 > vn2:
    print("입력된 숫자는 {}, {}입니다.".format(vn1, vn2))

if vn1 % 3:
    print("{}는 3의 배수가 아닙니다.".format(vn1))
if not vn1 % 3:
    print("{}는 3의 배수입니다.".format(vn1))
    
if vn2 % 3:
    print("{}는 3의 배수가 아닙니다.".format(vn2))
else :
    print("{}는 3의 배수입니다.".format(vn2))


# In[146]:


# 정수를 입력받아 90이상이면 "A", 80 이상이면 "B", 70 이상이면 "C" 그 이하는 "D"

input2 = int(input("입력 > "))

if input2 >= 90:
    print("A")
elif input2 >= 80:
    print("B")
elif input2 >= 70:
    print("C")
else:
    print("D")


# In[157]:


# 날짜 함수에서 월을 추출해서 현재 월이 봄인지, 가을인지 출력
# 1~3월은 봄 / 4~6월 여름 / 7월~9월 가을 / 10월~12월 겨울

now = datetime.datetime.now()
# now =datetime.date.today()

if 1 <= now.month <= 3:
    print("봄")
elif 4 <= now.month <= 6:
    print("여름")
elif 7 <= now.month <= 9:
    # print("가을")
    pass
elif 10 <= now.month <= 12:
    print("겨울")


# In[195]:


# 숫자 부호 숫자를 입력받아 계산하는 프로그램 작성
# 부호는 +, -, *, /를 입력하세요
# 10 + 20 = 30 이러한 형식으로 출력
input3 = input("입력 > ")

num2 = input3.split(' ')
n1 = int(num2[0])
n2 = int(num2[2])

if num2[1] == "+":
    result1 = n1 + n2
elif num2[1] == "-":
    result1 = n1 - n2
elif num2[1] == "*":
    result1 = n1 * n2
elif num2[1] == "/":
    if n2 != 0:
        result1 = n1 / n2
    else:
        print("0으로 나눌 수 없습니다")
else:
    print("부호는 +, -, *, / 만 가능합니다.")
if not (num2[1] == "/" and n2 == 0) and num2[1] in "+-*/":
    print("{} {} {} = {}".format(n1, num2[1], n2, result1))


# In[205]:


# list는 여러개의 데이터 집합 변수명 = [ , , , ... , ]
# +, *, len() 리스트의 개수
# list.append(요소), list.insert(위치, 요소)
a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
print("a_list + b_list :", a_list + b_list)
print("a_list * 3 :", a_list * 3)
c_list = a_list + b_list
print("a_list 갯수 :{}, b_list 갯수 :{}, c_list 갯수 :{}".format(len(a_list), len(b_list), len(c_list)))

a_list.append(b_list) # 마지막에 "추가"
print(a_list)
# a_list의 "a"를 출력
print(a_list[3][0])

a_list.insert(1, c_list)
a_list


# In[230]:


# a_list = [1, 2, 3], b_list = ["test", "abcd"]
a_list = [1, 2, 3]
b_list = ["test", "abcd"]

# a_list에 b_list를 추가하세요 extend()
a_list.extend(b_list)
print(a_list)

# a_list에 b_list를 추가하세요 append()
a_list.append(b_list)
print(a_list)

# b_list가 추가된 a_list에서 "abcd"를 출력하세요 -> 인덱스를 이용하여
print(a_list[-1][-1])

# b_list에서 "test" 앞에 "name"을 추가하세요
b_list.insert(0, "name")
print(b_list)

# a_list의 두번째 요소를 "change"로 변경하세요
a_list[1] = "change"

# a_list와 b_list를 출력
print("a: ", a_list, "\n", b_list)

