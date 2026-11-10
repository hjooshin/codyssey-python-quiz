quizzes = [
    {
        "question": "비디오 아트의 선구자로 알려진 한국의 예술가는 누구일까요?",
        "choices": ["김환기", "백남준", "이중섭", "박수근"],
        "answer": 2
    },
    {
        "question": "백남준의 <TV를 위한 선>은 어떤 기기를 활용한 작품일까요?",
        "choices": ["라디오", "텔레비전", "스마트폰", "영사기"],
        "answer": 2
    },
    {
        "question": "박현기의 <무제>에서 함께 쌓아 올린 것은 무엇일까요?",
        "choices": ["책과 신문", "나무와 거울", "돌과 TV", "의자와 조명"],
        "answer": 3
    },
    {
        "question": "한경우의 <레드 캐비닛>은 어떤 종류의 작품일까요?",
        "choices": ["유화", "대리석 조각", "수채화", "영상 작품"],
        "answer": 4
    },
    {
        "question": "이안 쳉의 <천 개의 삶>에 등장하는 동물은 무엇일까요?",
        "choices": ["거북이", "고양이", "강아지", "토끼"],
        "answer": 1
    }
]

best_score = 0

print("====================================")
print("  기술의 노스탤지어 - 미술 퀴즈 게임")
print("====================================")
print("국립현대미술관 뉴미디어 소장품 특별전")
print("미술·문화예술 상식 퀴즈에 오신 것을 환영합니다!")


while True:
    print("\n===== 퀴즈 게임 메뉴 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가하기")
    print("3. 퀴즈 목록 보기")
    print("4. 최고 점수 확인")
    print("5. 종료")

    choice = input("\n원하는 메뉴 번호를 입력하세요 (1~5): ").strip()

    if choice == "1":
        score = 0

        print("\n퀴즈를 시작합니다!")
        print("총", len(quizzes), "문제입니다.")

        for index, quiz in enumerate(quizzes, start=1):
            print("\n----------------------------")
            print(f"문제 {index}. {quiz['question']}")

            for number, answer in enumerate(quiz["choices"], start=1):
                print(f"{number}. {answer}")

            while True:
                user_answer = input(
                    "\n정답 번호를 입력하세요 (1~4): "
                ).strip()

                if user_answer in ["1", "2", "3", "4"]:
                    break

                print("잘못된 입력입니다. 1~4 중에서 선택해 주세요.")

            if user_answer == str(quiz["answer"]):
                print("정답입니다! 축하합니다!")
                score += 1
            else:
                print("틀렸습니다.")
                print("정답은", quiz["answer"], "번입니다.")

        print("\n===== 퀴즈 결과 =====")
        print("총 문제 수:", len(quizzes))
        print("맞힌 문제 수:", score)
        print("최종 점수:", score * 20, "점")

        if score > best_score:
            best_score = score
            print("새로운 최고 점수입니다!")

    elif choice == "2":
        print("\n퀴즈 추가 기능은 다음 단계에서 구현합니다.")

    elif choice == "3":
        print("\n===== 퀴즈 목록 =====")

        for index, quiz in enumerate(quizzes, start=1):
            print(f"{index}. {quiz['question']}")

    elif choice == "4":
        print("\n===== 최고 점수 =====")
        print("최고 점수:", best_score * 20, "점")
        print("프로그램 종료 시 점수는 초기화됩니다.")

    elif choice == "5":
        print("\n게임을 종료합니다.")
        print("이용해 주셔서 감사합니다!")
        break

    else:
        print("잘못된 입력입니다. 1~5 중에서 선택해 주세요.")