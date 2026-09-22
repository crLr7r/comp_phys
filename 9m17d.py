# 이렇게 하면 global 변수 gun에 제대로 업데이트가 안 됨
# gun = 10
#
# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soliders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

#표준입출력, 출력포맷---------------------------------------------------------
print("Python", "Java", sep=", ", end="?\n")
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java1", file=sys.stderr)   #에러로 메시지를 내보냄

scores = {"수학": 0, "영어": 50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = 10
print(type(answer))
print("입력하신 값은 " + str(answer) + "입니다")

score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line)
score_file.close()

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())

# class
class Student:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Location: {self.location}"

class Classroom:
    def __init__(self, *students_info):
        self.students = []
        for info in students_info:
            self.add_student(*info)

    def add_student(self, name, age, location):
        student = Student(name, age, location)
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student)

stdt1_info = ('이상욱', 47, '서울')
stdt2_info = ('홍길동', 16, '부산')
stdt3_info = ('김철수', 15, '대구')

stdt1 = Student(*stdt1_info)
stdt2 = Student(*stdt2_info)
stdt3 = Student(*stdt3_info)

print(stdt1)
print(stdt2)
print(stdt3)
print()

print(stdt1.name)
print(stdt2.name)
print(stdt3.name)
print()

classroom = Classroom(stdt1_info, stdt2_info , stdt3_info )

classroom.list_students()