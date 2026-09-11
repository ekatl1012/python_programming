# for문

# for i in iterable객체 : 

for i in range(3):
    print(i, end=" ")
print()

a=range(5)
print(a.start, a.stop, a.step)

# 1~5까지
for i in range(1,6):
    print(i, end=" ")
print()

# 0~10 중에 짝수 출력
for i in range(0,11,2):
    print(i,end=" ")
print()

# 5~1까지 거꾸로 출력
for i in range(5,0,-1):
    print(i, end=" ")
print()

# 1~10까지의 합
tot=0
for i in range(1,11):
    tot=tot+i
else:
    print(f"sum={tot}")

print(sum(range(1,11)))

s="hi12한글車叡潾"

for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
# 2*1 = 2 2*2 = 4
# ...
# 9*1 = 9 ..

for i in range(1,10):
    for h in range(1,10):
        print(f"{i}*{h}={i*h}",end=" ")
    print()

        