def add_until_five(x):
    print(f"처음 들어온 숫자: {x}")
    
    # 1. 먼저 처음에 들어온 숫자가 5 이상인지 검사
    if x >= 5:
        print("입력값이 이미 5 이상입니다.")
    # 2. 5 미만일 때만 아래 반복문을 실행
    else:
        while x < 5:
            x += 1
            print(f"1 더한 결과: {x}")
        print("5가 되어서 반복을 멈춥니다!")

add_until_five(1)
add_until_five(6) # 이렇게 6을 넣어서 테스트해 봐!