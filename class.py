class Cal:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
obj=Cal(10,20)
add=obj.add()
mul=obj.mul()
print add,mul

class Cal1(Cal):
    def sub(self):
        return self.x-self.y
    def div(self):
        return self.x/self.y
obj=Cal1(20,30)
sub=obj.sub()
add=obj.add()
mul=obj.mul()
div=obj.div()
print add,mul,sub,div
