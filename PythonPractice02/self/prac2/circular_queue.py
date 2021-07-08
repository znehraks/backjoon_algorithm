"""
아래에 학번과 이름을 꼭 적으세요.

학번:60152572
이름:유정민
"""
class CircularQueue:  
    def __init__(self, max_size):

    def enqueue(self, data):
    def dequeue(self):
    def is_full(self):
    def is_empty(self):
    def size(self):

if __name__ == "__main__":
    q = CircularQueue(3)
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Enque 10", q.enqueue(10))
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())
    print("Enque 20", q.enqueue(20))
    print("Enque 30", q.enqueue(30))
    print("Enque 40", q.enqueue(40))
    print("Deque", q.dequeue())
    print("Enque 50", q.enqueue(50))
    print("Deque", q.dequeue())
    print("Deque", q.dequeue())
    print("Enque 60", q.enqueue(60))
    print("Enque 70", q.enqueue(70))

    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print(len(q.queue)) # should be 4. list 자체의 크기는 변하지 않아야 함!!!

# 아래는 위 코드 테스트를 위해서 만들어놓은 샘플입니다. 수정하지 마세요.
# 다음과 같은 결과가 나와야 합니다.
"""
Empty? True , Full? False , Size= 0
Enque 10 True
Empty? False , Full? False , Size= 1
Enque 20 True
Enque 30 True
Enque 40 None
Deque 10
Enque 50 True
Deque 20
Deque 30
Enque 60 True
Enque 70 True
Empty? False , Full? True , Size= 3
Deque 50
Empty? False , Full? False , Size= 2
Deque 60
Empty? False , Full? False , Size= 1
Deque 70
Empty? True , Full? False , Size= 0
Deque None
Empty? True , Full? False , Size= 0
4
"""