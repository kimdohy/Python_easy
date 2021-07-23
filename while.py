#while 문 반목하는 명령어
#1부터 10까지 출력
i = 0
while i < 10 :
    print(i)
    i+=1

#안녕하세요 10줄 출력
while i < 20 : 
    print("안녕하세요")
    i+=1
print("------------------------")
#구구단 8단 출력하기
j = 1
while j < 10 :
    dan = 8
    print("8 * {} = {}".format(j,dan * j))
    j +=1
print("--------------------------------")
#구구단 1단 부터 9단 출력하기
a = 1
while a < 10 : 
    b = 1
    while b < 10 :
        print("{} * {} = {}".format(a,b,a*b))
        b +=1
    a +=1        

#무한으로 원하는 구구단 출력 exit 입력시 프로그램종료

while True :
    dan = input("단수를 입력하시오 : ") 
    if dan == "exit" :
        break
    dan = int(dan)
    b = 1
    while b < 10 :
        print("{} * {} = {}".format(dan,b,dan*b))
        b +=1
    
