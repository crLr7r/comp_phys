# 애완동물을 소개해 주세요
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

# print(f"우리집 {animal}의 이름은 {name}에요")
# print(f"{name}는 {age}살이며, {hobby}을 아주 좋아해요")
# print(f"{name}는 어른일까요? {is_adult}")
# print()
#
# print("우리집 " + animal + "의 이름은 " + name + "에요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

#사칙 연산
# print("1 + 1 = " , 1+1)
# print("3 - 2 = ", 3-2)
# print("5 X 2 = ", 5*2)
# print("6 / 3 = ",6/3)
#
# print("2^3 = ",2**3)
# print("5 mod 3 = ",5%3)
# print("5 // 3 = ",5//3)
#
# print("10 > 3 ? ",10 > 3)
# print("4 >= 7 ? ",4 >= 7)
# print("10 < 3 ? ",10 < 3)
# print("5 < = 3 ?",5 <= 3)
#
# print("3 = 3 ? ",3 == 3)
# print("4 = 2 ? ",4 == 2)
# print("4 + 3 = 7 ? ",4 + 3 == 7)
#
# print("1 != 3 ? ",1 != 3)
# print("1 = 3 ? ",not (1 != 3))
#
# print("3 > 0 and 3 < 5 ? ",(3 > 0) and (3 < 5))
# print("3 > 0 and 3 < 5 ?",(3 > 0) & (3 < 5))
#
# print("3 > 0 or 3 > 5 ? ",(3 > 0) or (3 > 5))
#
# print("3 < 5 < 7 ? ",3 < 5 < 7)
# print("3 < 5 < 4 ? ",3 < 5 < 4)

# 변수 처리 방식
# number = 2 + 3 * 4
# print(number)
#
# number = number + 2
# print(number)
#
# number += 2
# print(number)
#
# number *= 2
# print(number)
#
# number /= 2
# print(number)

# 기타 수학 연산
print(abs(-5))
print(pow(4, 2))
from math import *
print(floor(4.7))
print(ceil(4.2))

# 문자열 & 문자열 처리
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
#python의 0번째 (첫번째) 글자가 upper인가?
print("문장의 길이 = ", len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print("n의 index = ", index)
index = python.index("n", index + 1)
print("두번째 n의 index = ",index)

print("n의 index 찾기 = ", python.find("n"))
print("Sange Wook의 index 찾기 = ", python.find("Sang Wook"))

print("Python의 index 찾기 = ", python.index("Python"))

print("a의 개수 = ", python.count("a"))

sentence2 = \
     "나는 소년이고, " \
      "파이썬은 쉬워요" \

print(sentence2)
