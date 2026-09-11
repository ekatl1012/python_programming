# 조건문 : if문, match문


# if문
age = 17

if age>=18 :
    print("성년")
else :
    print("미성년")

score = 85

if age>=90:
    print("A")
elif age>=80:
    print("B")
elif age>=70:
    print("C")
else :
    print("D")

# match문
grade="A"

match grade: # break가 자동으로 실행
    case "A":
        print("우수")
    case "B":
        print("양호")
    case "C" | "D" :
        print("보통")
    case _:
        print("알 수 없음")
    