class Car(object):
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 움직였다')
    def stop(self):
        print('멈춤')

k5 = Car()
k3 = Car()
k5.move(10)
k3.move(5)
k5.stop()
k3.stop()
print(k5.maxSpeed)
print(k3.maxSpeed)
print(type(k5))
print(type(k3))