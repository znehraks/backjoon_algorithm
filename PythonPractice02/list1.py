class List1:
    def __init__(self):
        self.data = [None] * 100
        self.cnt = 0
    
    def insert_head(self, value):
        for i in range(self.cnt, 0 , -1):
            self.data[i] = self.data[i-1]
        self.data[0] = value
        self.cnt += 1

    def insert_tail(self, value):
        self.data[self.cnt] = value
        self.cnt += 1

    def delete_head(self):
        for i in range(self.cnt):
            self.data[i] = self.data[i+1]
            if i == self.cnt-1:
                self.data[i] = None
                self.cnt -= 1
                break
    
    def delete_tail(self):
        self.data[self.cnt] = None
        self.cnt -= 1
    
    def count(self):
        return self.cnt

    def print_all(self):
        for i in range(self.cnt):
            print(self.data[i], end=" ")
        print()

list = List1()
list.insert_head('A')
list.insert_head('B')
list.insert_tail('C')
list.insert_tail('D')
list.print_all()
list.delete_head()
list.print_all()
list.delete_tail()
list.print_all()
