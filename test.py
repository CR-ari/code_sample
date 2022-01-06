# # 1번 문제
# def sum_ab(a, b):
#     c = a + b
#     print("1번 문제: ", c)
#     return(c)

# sum_ab(2,3)

# # 1-1번 문제
# def comp_ab(a,b):
#     if a > b:
#         print("2번 문제: ", a)
#         return a
    
#     else:
#         print("2번 문제: ", b)
#         return b

# comp_ab(3,1)

# # 2번 문제
# def sub_ab (a, b):
#     if comp_ab(a, b) == a:
#         print(a-b)
#         return a-b
#     else:
#         print(b-a)
#         return b-a
    
# sub_ab(2,5)


# 1-1번 문제
# def comp_ab(a,b):
#     if a > b:
#         print("2번 문제: ", a)
#         return a,b
    
#     else:
#         print("2번 문제: ", b)
#         return b,a


# def sub_ab (a, b):
#     result = comp_ab(a,b)[0]-comp_ab(a,b)[1]
#     print(result)
#     return result
    
    
# sub_ab(2,7)

# def mult_ab(a,b):
#     return a*b

# def comp_10(a,b):
#     c = mult_ab(a,b)
#     if c > 10:
#         #print("bigger than 10")
#         return f"bigger than {float(10)}. The result was {float(c)}"
#     else:
#         #print("smaller than 10")
#         return f"smaller than {float(10)}. The result was {float(c)}"
    
    
# result1 = comp_10(3,5)
# result2 = comp_10(2,3)

# print(f"result1: {result1}")
# print(f"reuslt2: {result2}")


# a = 1
# while a < 10:
#     print(f"a는 {a}에요. 10보다 작아요")
#     a += 1


# a = 5
# while a != 0:
#     print(f"Go! a is {a} ")
#     a -= 1
    
    

# result = 8
# state = True

# while state == True:
#     result -= 1
#     print(result)
    
#     if result == 0:
#         print("Finished")
#         state = False
#     else:
#         print("keep going")



# def mul(x,y):
#     return x*y

# numbers = [1,2,3,4]

# for item in numbers:
#     result = mul(item, 3)
#     print(result)


# 판결문_목록 = ["피고인","피해자", "주문", "이유", "법령의 적용", "판단", "판사"]

# # 판결문_목록.append("범죄사실")

# print(판결문_목록[-1:])



# case = {"meta" : ["피고인", "피해자", "주문", "판사"], "reason" : ["범죄사실", "법령의 적용", "판단"]}
# case["meta"] = '검사'
# print(case)

# cases = [["피고인", "피해자", "주문", "판사"], ["범죄사실", "법령의 적용", "판단"]]
# for case in cases:
#     print(case.search("피고인"))

# ice = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}

# ice["죠스바"] = 1200

# ice["메로나"] = 1333

# del ice["메로나"]

# print(ice)


# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
# # print(inventory["메로나"][0])
# inventory["월드콘"] = [500, 7]
# print(inventory.keys())

# total = 0

# for val in inventory.values():
#     total = total + val[1]

# print(total)

# colors = ["yellow", "green", "blue", "purple", "red","pink"]

# for i in colors:
#     if i == "blue":
#         continue
#     elif i == "red":
#         break
#     else:
#         print(i)


# 1번
# print(f"My phone number is ####-####-{'10'*2}. I am {2*10} years old.")

#3번
# fruit = ['banana', 'apple', 'orange']
# vegatables = ['cucumber', 'eggplant', 'letuce']
# healthy_food = fruit + vegatables
# print(healthy_food)

# #5번
# groceries = ['carrot', 'pizza', 'cherry', 'cucumber', 'juice', 'sandwich']
# andys_food = []
# for i in groceries:
#     if 'c' == i[0]:
#         andys_food.append(i)
#     else:
#         continue

# print(andys_food)

# #6번
# words = ['hi', 'bye', 'ciao', 'hello']
# for i in words:
#     print(f'{i} 단어의 길이: {len(i)}')

#9번
# my_bag = ['money', 'phone', 'pencil', 'keys', 'notes']

# state = True
# while state:
#     if len(my_bag) == 0:
#         break
#     else:
#         print(len(my_bag))
#         my_bag.pop()

#7번
# for i in range(5, 16, 5):
#     print(i)

#10번
# def merge_string(str1, str2):
#     print(str1+str2)
#     return str1+str2

# result = merge_string('apple','mango')
# print(result)

# print(f'{merge_string("apple","mango")}')

# #11번
# team_a = [10, 6, 8]
# team_b = [8, 10, 9]

# def average_score(team_name):
#     cnt = len(team_name)
#     total = 0
#     for i in team_name:
#         total = total + i
#     print(total//cnt)
    
# average_score(team_a)
# average_score(team_b)

#12번
# team_a = [10, 6, 8]
# team_b = [8, 10, 9]

# def get_winner(game_nr):
#     number = game_nr - 1
#     if team_a[number] > team_b[number]:
#         print('team_a')
#     else:
#         print('team_b')

# get_winner(1)
# get_winner(2)
# get_winner(3)



# q17_list = [] 
# with open("q17.txt", "r") as f: #q17 txt 읽었어
# hello
# world
# bye
#                     0       1       2
# f.readline -> ['hello\n', 'worlds\n', 'bye'] = q17_list
#     q17_list = f.readlines()
    
# q18_list = []
# for i in range(3):
#     if i == 2:
#         new_word = q17_list[i] + "EDITED"
#         q18_list.append(new_word)
#     else:
#         q18_list.append(q17_list[i])

# # print(q18_list)
# q18_list = ['hello\n', 'worlds\n', 'byeEDITED']
# with open("q18.txt", "w") as f:
#     for i in q18_list:
#         f.write(i)


import json

# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1},
#   ],
#   "school": {
#       "highschool": ["춘천high","한림high"],
#       "college":["한림대"],"grad":[None]
#       }
# }

# #John의 아이는 몇명?
# print(len(x['children']))

#John씨으 나이가 40보다 많으면  print over 40… 아니면 under 40





#Ford Edge
# print(x["cars"][1]["model"])

# 27.5
# print(x["cars"][0]["mpg"])

#한림high
# print(x["school"]["highschool"][1])

# 한림대학교
# print(x["school"]["college"])

# convert into JSON:
#y = json.dumps(x)

# the result is a JSON string:
#print(y)


import json

x = {
    "name" : "Choi Ari",
    "studentID" : "20505",
    "nationality" : "South Korea",
    "family" : {"siblings" : [{"name" : "Choi MK", "age" : 23, "gender" : "F"}],
                "pets" : [{"name" : "Gucci", "age" : 0.8, "gender" : "F"}]
                }
}

y = {
    "name": "Jane",
    "studentID": 2141623,
    "nationality": "South Korea",
    "family": {"siblings": [{"name": "David","age": 31,"gender": "M"}],
                "pets": [{"name": "mong","age": 2,"gender": "M"},
                        {"name": "doong", "age": 7,"gender": "M"}]
                }
    }

z = {"name": "yuna",
    "studentID": 20504,
    "nationality": "South Korea",
    "family": {
        "siblings": [{"name": "WOO JOO","age": 24,"gender": "M"},
                    {"name": "MIN JOO","age": 24,"gender": "M"}],
        "pets": [{"name": None,"age": None,"gender": None}]
            }
        }

w = {"name": "bb",
    "studentID": 20346,
    "nationality": "South Korea",
        }
json_list = []
json_list.append(x)
json_list.append(y)
json_list.append(z)
# json_list.append(w)

dict = {"data" : json_list}

with open("personal_info.json", "w") as jw:
        json.dump(dict, jw)

