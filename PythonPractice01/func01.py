def simple_adder(a, b, c):
    result = a+b+c
    return result

print(simple_adder(1,2,3))

def func1(var1, var2):
    result = var1**2 - var2**2
    return result

print(func1(4,3))

def input_sum(*numbers):
    sum = 0
    print(numbers)
    for i in numbers:
        sum += i
    return sum

print(input_sum(1,2,3,4,4,4,4,4,4))


class Square:
    def setValue(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height

square1 = Square()
square1.setValue(5,6)
print(square1.getArea())

square3 = Square()
Square.setValue(square3, 1,2)
print(Square.getArea(square3))

class Account:
    def __init__(self, name):
        print('[init start] 객체가 생성됩니다')
        self.name = name
        self.money = 10000
        print('[init end] 객체가 생성되었습니다')

    def deposit(self, money):
        print('[deposit start] 돈을 저축합니다')
        self.money += money
        print('[deposit end] 돈을 저축했습니다')

    def withdraw(self, money):
        print('[withdraw start] 돈을 인출합니다')
        self.money -= money
        print('[withdraw end] 돈을 인출했습니다')

    def printBalance(self):
        print('[printBalance start] 잔고를 출력합니다')
        print('잔고: ', self.money)
        print('[printBalance end] 잔고를 출력했습니다')

    def printOwner(self):
        print('[printOwner start] 소유자를 출력합니다')
        print('소유자: ', self.name)
        print('[printOwner end] 소유자를 출력했습니다')

account1 = Account("홍길동")
account1.deposit(55555)
account1.withdraw(20500)
account1.printBalance()
account1.printOwner()