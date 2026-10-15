import numpy as np

# subway = [10, 20, 30]
# print(subway)
#
# subway = np.linspace(10, 30, 3)
# print(subway)
#
# subway = np.arange(10, 31, 10)
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# # 조세호가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호"))  # index는 0, 1, 2로 시작됨
#
# # 하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
#
# # 정형돈을 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
#
# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop(2))
# print(subway)
#
# #dictionary
# cabinet = {"A-3":"유재석","B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# # 새손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)
#
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
#
# # 집합 set
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# print(java)
# print(python)
#
# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
#
# # 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
# print(java)
#
# # 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# # 교육받아서 python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# # 자바를 까먹은 사람
# java.remove("김태호")
# print(java)
#
# #자료구조의 변경
# #커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))
#
# weather = input("오늘 날씨는 어때요?")
# # if 조건:
#         # 실행 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")
#
# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨예요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")
#
# for waiting_no in range(1, 6):
#     print("대기번호: {0}".format(waiting_no))
#
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다")
#
# customer = "아이언맨"
# index = 1
# while index < 11:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1
#
# customer = "토르"
# person = "unknown"
#
# while person != customer:
#     print("{0}, 커피가 준비되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요?")

def open_account():
    print("새로운 계좌가 생성되었습니다")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
def withdraw_night(balance, money):
    commission = 100
    if balance >= money + commission:
        print("출금이 완료되었습니다. 수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance-money-commission))
        return commission, balance-money-commission
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
_, balance = withdraw_night(balance, 50)

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")