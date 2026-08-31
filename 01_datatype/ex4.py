# 문자열(str)
# "", ''

a="python"
print(a,type(a))

print("I'll be back")
print('I\'ll be back')

# 여러줄 문자열
a= """
Life is short
You need Python
"""
print(a)

# docstring
def func():
    # x=1 // document string은 무조건 첫번쨰 줄에 작성해야 함
    """
    func() 함수에 대한 설명 작성
    """
    pass

print(func.__doc__)

# 문자열 연결
print("Hello"+"Python")
print("-"*10)

# 문자열 연산 시 주의 사항 ) 문자열은 문자열 끼리, 숫자는 숫자끼리.
# print("Hello"+3)
print("Hello"+str[3])

print("10"+"3")
print(int("10")+int("3"))

# 문자열 포맷팅 (f-string)
name = "pororo"
age=23

print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")
pi=3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num=123456789
print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")