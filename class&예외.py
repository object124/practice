#예외 처리

#예외 처리에 대한 이해
#1. 파이썬에서 기본적인 예외 상황에 대한 처리는 예외가 발생하는 지점에서 죽는다. 이것도 하나의 메커니즘
#대신 죽은 이유 즉 에러 객체를 발생시켜준다.
#lst = [1,2,3]

#에러가 발생하는 상황
#lst[3]#IndexError: list index out of range


#예외 처리 목적 = 프로그램 안 죽게 하기 위해
#예외 처리 집어넣는 구문 정해져 있지 않고, 예외가 발생되리라고 생각되는 곳에 어디든 넣을 수 있음.
# try ~ except 처리


while True:
    
    try:
      age = int(input("나이를 입력하세요"))
      print(age)
      break
    except ValueError:
      print("입력이 잘못되었습니다")  

print("만나서 반가웠습니다")


def main():
          bread = 10 #10개의 빵
          try:
                  people = int(input("몇 명?"))
                  print("1인당 빵의 수:", bread / people)
                  print("맛있게 드세요")
          except ValueError:
                  print("입력이 잘못되었습니다")
          except ZeroDivisionError:
                  print("0으로 나눌 수 없습니다")

main()


#에러 메세지 확인

def main():
          bread = 10 #10개의 빵
          try:
                  people = int(input("몇 명?"))
                  print("1인당 빵의 수:", bread / people)
                  print("맛있게 드세요")
          except ValueError as msg:
                  print("입력이 잘못되었습니다")
                  print(msg) #오류 메세지 출력
          except ZeroDivisionError as msg:
                  print("0으로 나눌 수 없습니다")
                  print(ZeroDivisionError, msg)

          finally:
                  print("어쨌든 프로그램은 종료되었습니다")
main()

class Grade:
    def init(self,kor,eng,math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def set_eng(self,eng):
        self.eng = eng

    def get_total(self):
        return self.kor + self.eng + self.math

    def get_avg(self):
        return self.get_total() / 3

    def get_grade(self):

        avg = self.get_avg()
        grade = "가"

        if avg >= 90:
            grade = '수'
        elif avg >= 80:
            grade = '우'
        elif avg >= 70:
            grade = '미'
        elif avg >= 60:
            grade = '양'
        else:
            grade ='가'

        return grade

def main():

  
    while True:
        try:
            kor = int(input("국어 점수 입력 : "))
            eng = int(input("영어 점수 입력 : "))
            math = int(input("수학 점수 입력 : "))

            grade = Grade(kor,eng,math)

            print("국어 : ",grade.kor)

            print("총점 : ",grade.get_total())
            print("평균 : ",grade.get_avg())
            print("학점 : ",grade.get_grade())

          
    

        except:
            print("잘못된 입력입니다.")
        finally:
            continue_yn = input("계속 하시겠습니까? (y/n) : ")

        if continue_yn.upper() != 'Y' and continue_yn.upper() != 'YES' :
            break
    print("프로그램 종료")

main()


#로또
# 1 ~ 45번까지 번호 = 6개 추출
#랜덤 모듈


import random

print(random.random()) # 0 이상 1미만의 임의의 실수 반환

# 주사위처럼 임의의 숫자 6개 1부터 6까지

#print(random.randrange(1,7)) # 1이상 7미만의 난수


#print(random.randint(1,45)) # 


abc = [1,2,3,4,5] # 데이터를 섞어 내놓음
#abc = random.shuffle(abc)
#print(abc)


#random.choice(abc)


#menu = '짜장면','짬뽕','탕수육'
#random.choice(menu)

#random.choice([True, False])


#주사위 게임

#>>첫번째의 참가자의 이름을 입력하세요. 
#영희
#>>두번째의 참가자의 이름을 입력하세요. 
#철수


#영희 주사위 숫자는 : 6
#철수 주사위 숫자는 : 5
#철수가 이겼습니다.

#dice_game = DiceGame()
#dice_game.run()

class DiceGame():
    #def init(self,player1,player2):
    #    self.players = ([player1,0],[player2,0]) #user 2명으로 한정

    def input_players(self):

        while True:
            try:
                player1 =  input("첫 번째 참가자의 이름을 입력하세요: ")
                player2 =  input("두 번째 참가자의 이름을 입력하세요: ")
                break;
            except ValueError:
                print("입력이 잘못되었습니다. 처음부터 다시 입력하세요.")
                continue

        self.players = ([player1,0],[player2,0]) #user 2명으로 한정
        #print(self.players)

    def dice_result(self):

        for i in range(2):
            self.players[i][1] = random.randint(1,6)
            print(self.players[i][0],"주사위 숫자는 : ",self.players[i][1])

        if self.players[0][1] > self.players[1][1]:
            print(self.players[0][0],"가 이겼습니다.")
        elif self.players[0][1] < self.players[1][1]:
            print(self.players[1][0],"가 이겼습니다.")
        else:
            print("비겼습니다.")

    def run(self):
        self.input_players()
        self.dice_result()

dice_game = DiceGame()
dice_game.run()