# 221번 문제
def print_reverse(str):
    print(str[::-1])
    
print_reverse("python")

# 222번 문제
def print_score(list):
    total = 0
    cnt = len(list)
    for i in range(cnt):
        number = int(list[i])
        if i == len(list)-1:
            total = total + number
            average = total / cnt
            print(average)
        else:
            total = total + number
            
print_score([1,2,3])

#223번

def print_even(list):
    for i in range(len(list)):
        number = list[i]
        if number % 2 == 0:
            print(number)
        else:
            continue
        
print_even([1, 3, 2, 10, 12, 11, 15])

#224번

def print_keys(dict1):
    print(dict1.keys())
    
print_keys({"이름":"김말똥", "나이":30, "성별":0})

# 225번
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict1, key1):
    print(dict1[key1])
    
print_value_by_key(my_dict, "10/26")

# 226번
def print_5xn(str):
    for i in range(0, len(str), 5):
        print(str[i: i+5])


print_5xn("아이엠어보이유알어걸")

#227번
def printmxn(str, num1):
    for i in range(0, len(str), num1):
        print(str[i : (i+num1)])
        
printmxn("아이엠어보이유알어걸", 3)

#228번
def calc_monthly_salary(num1):
    result = num1 // 12
    print(result)
    
calc_monthly_salary(12000000)
#229번
def my_print(a,b):
    print("왼쪽 : ", a)
    print("오른쪽 :", b)

# my_print(a=100, b=200)
#예상 결과: 왼쪽 : 100
#            오른쪽 : 200

# 230번
def my_print(a,b):
    print("왼쪽 : ", a)
    print("오른쪽 :", b)

#my_print(b=200, a=100)
#예상 결과: 왼쪽 : 200
#            오른쪽 : 100

#231번
def n_plus_1 (n):
    result = n + 1

n_plus_1(3)
# print(result)

#예상결과 안나옴

#232번
def make_url(str):
    print(f"www.{str}.com")

make_url("naver")

# 233번
def make_list(str):
    word_list = []
    for i in range(len(str)):
        word_list.append(str[i])
    print(word_list)
    
make_list("abcd")

# 234번
def pickup_even(list):
    even_list = []
    for i in range(len(list)):
        number = int(list[i])
        if number % 2 == 0:
            even_list.append(number)
        else:
            continue
    print(even_list)

pickup_even([3, 4, 5, 6, 7, 8])

#235번
def convert_int(str):
    str1 = str.replace(",","")
    print(int(str1))

convert_int("1,234,567")

# 236번
# def 함수(num):
#     return num + 4
# a = 함수(10) 14
# b = 함수 (a) 14+4 = 18
# c = 함수(b) 18+4 = 22

#print(c)
# 예상 결과  22

# # 237번
# def 함수(num):
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)

#10+4 = 14 / 14+4 = 18 / 18+4 = 22
# 예상결과 22

#238번
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)  14
# c = 함수2(a)  140
# print(c)

#예상결과 140

#239번
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10) 
# print(c)

#예상결과 16

#240번
# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2) -> 12 -> 14 -> 28
# print(c)
# 예상결과 28