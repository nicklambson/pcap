class A:
    def __init__(self, name):
        self.name = name

a = A("class")
print(a)

# <__main__.A object at 0x0000018B421E4910>  

class B:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

b = B("class")
print(b)

# class