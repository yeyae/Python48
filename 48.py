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
