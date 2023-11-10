import random

def lotto():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
            print(f"{num}에 해당 숫자가 없습니다")
        else:
            print(f"{num}에 해당 숫자가 있습니다")
    result.sort()
    print("생성된 로또 번호는", result, "입니다")

lotto()

