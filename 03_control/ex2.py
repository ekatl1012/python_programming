# 반복문 : while문, for문

# while문
# 1~10까지 반복 출력
i=0
while i<10:
    i+=1
    print(i)
    # if i==5:
    #     break
else:
    print("End")

nums=[1,2,3,4,5]
target=2
i=0

while i<5:
    i+=1
    if nums[i]==target :
        print("찾았다!")
        break
else:
    print("찾기 실패..")

# 1-10까지의 합
i=1
tot = 0

while i<11:
    tot=tot+i
    i+=i
print(f"sum={tot}")

while i<11:
    i+=i
    if i%2==1:
        continue
    tot=tot+i
    
print(f"sum={tot}")