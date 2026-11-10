class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def ask(self, number):
        print("\n----------------------------")
        print(f"문제 {number}. {self.question}")

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

        while True:
            user_answer = input(
                "\n정답 번호를 입력하세요 (1~4): "
            ).strip()

            if user_answer in ["1", "2", "3", "4"]:
                break

            print("잘못된 입력입니다. 1~4 중에서 선택해 주세요.")

        if int(user_answer) == self.answer:
            print("정답입니다! 축하합니다!")
            return 1

        print("틀렸습니다.")
        print("정답은", self.answer, "번입니다.")
        return 0


class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz(
                "비디오 아트의 선구자로 알려진 한국의 예술가는 누구일까요?",
                ["김환기", "백남준", "이중섭", "박수근"],
                2
            ),
            Quiz(
                "백남준의 <TV를 위한 선>은 어떤 기기를 활용한 작품일까요?",
                ["라디오", "텔레비전", "스마트폰", "영사기"],
                2
            ),
            Quiz(
                "박현기의 <무제>에서 함께 쌓아 올린 것은 무엇일까요?",
                ["책과 신문", "나무와 거울", "돌과 TV", "의자와 조명"],
                3
            ),
            Quiz(
                "한경우의 <레드 캐비닛>은 어떤 종류의 작품일까요?",
                ["유화", "대리석 조각", "수채화", "영상 작품"],
                4
            ),
            Quiz(
                "이안 쳉의 <천 개의 삶>에 등장하는 동물은 무엇일까요?",
                ["거북이", "고양이", "강아지", "토끼"],
                1
            )
        ]

        self.best_score = 0

    def add_quiz(self):
        print("\n===== 새로운 퀴즈 추가 =====")

        while True:
            question = input("새로운 문제를 입력하세요: ").strip()

            if question:
                break

            print("문제는 비워 둘 수 없습니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 보기를 입력하세요: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("보기는 비워 둘 수 없습니다.")

        while True:
            answer = input("정답 번호를 입력하세요 (1~4): ").strip()

            if answer in ["1", "2", "3", "4"]:
                break

            print("잘못된 입력입니다. 1~4 중에서 선택해 주세요.")

        new_quiz = Quiz(question, choices, int(answer))
        self.quizzes.append(new_quiz)

        print("\n새로운 퀴즈가 추가되었습니다!")
        print("현재 총", len(self.quizzes), "문제입니다.")

    def play(self):
        score = 0

        print("\n퀴즈를 시작합니다!")
        print("총", len(self.quizzes), "문제입니다.")

        for number, quiz in enumerate(self.quizzes, start=1):
            score += quiz.ask(number)

        final_score = score * 100 // len(self.quizzes)

        print("\n===== 퀴즈 결과 =====")
        print("총 문제 수:", len(self.quizzes))
        print("맞힌 문제 수:", score)
        print("최종 점수:", final_score, "점")

        if final_score > self.best_score:
            self.best_score = final_score
            print("새로운 최고 점수입니다!")

    def show_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print("최고 점수:", self.best_score, "점")
        print("프로그램 종료 시 점수는 초기화됩니다.")

    def run(self):
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

            choice = input(
                "\n원하는 메뉴 번호를 입력하세요 (1~5): "
            ).strip()

            if choice == "1":
                self.play()

            elif choice == "2":
                self.add_quiz()

            elif choice == "3":
                self.show_quizzes()

            elif choice == "4":
                self.show_best_score()

            elif choice == "5":
                print("\n게임을 종료합니다.")
                print("이용해 주셔서 감사합니다!")
                break

            else:
                print("잘못된 입력입니다. 1~5 중에서 선택해 주세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()