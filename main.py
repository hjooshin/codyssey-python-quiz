print("미술·문화예술 상식 퀴즈 게임에 오신 것을 환영합니다!")

while True:
    print("\n===== 퀴즈 게임 메뉴 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가하기")
    print("3. 퀴즈 목록 보기")
    print("4. 최고 점수 확인")
    print("5. 종료")

    choice = input("\n원하는 메뉴 번호를 입력하세요 (1~5): ")

    if choice == "1":
        print("퀴즈 풀기를 선택했어!")
    elif choice == "2":
        print("퀴즈 추가하기를 선택했어!")
    elif choice == "3":
        print("퀴즈 목록 보기를 선택했어!")
    elif choice == "4":
        print("최고 점수 확인을 선택했어!")
    elif choice == "5":
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~5 중에서 선택해 주세요.")