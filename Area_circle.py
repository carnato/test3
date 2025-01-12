class Area:
    def circle(self,radius):
        return 3.14*radius*radius
    
    def square(self, length):
        return length*length
    def rectangle(self, length,breath):
        return length*breath

obj=Area()
print(obj.circle(5))    
print(obj.square(4))
print(obj.rectangle(2,5))