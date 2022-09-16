#파이썬에서 class 사용하기
from unittest import result


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

#사칙연산 클래스 만들기
#클래스를 어떻게 만들까?

#1. a = FourCal() /사칙연산 클래스를 입력해서 a라는 객체 만들기
#2. a.setdata(4,2)처럼 입력 --> 숫자 4와 2를 a에 지정
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    #def 함수 이름(매개변수):
    #수행할 문장
    #...
a = FourCal()
a.setdata(4,2)
#setdata 메서드는 매개변수로 self, first, second 3개 입력값을 받음
#a.setdata(4,2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에서 setdata 메서드를 호출한 객체 a가 자동으로 전달
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4,2)
print(a.first)
b.setdata(3, 7)
print(b.first)

