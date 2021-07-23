tunel1= int(input("첫번째 터널의 높이를 정해주세요 : "))
tunel2= int(input("두번째 터널의 높이를 정해주세요 : "))
tunel3= int(input("셋번째 터널의 높이를 정해주세요 : "))

car = int(170)
if tunel1 < car or tunel2 < car or tunel3 < car :
    print("CRASH") 
else : 
    print("PASS")