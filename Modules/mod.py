def add(*args):
    """Custom module"""
    sum=0
    for num in args:
        sum+=num
    return sum    


data=172311030   
print("Custom module") 

# OOP method
class math:
    def __init__(self,*args) -> None:
        self.value=tuple(args)
        #self.args=args
    
    def add(self):
        summ=0
        for num in self.value:
            summ+=num
        return summ


    def mul(self):
        mul=1
        for num in self.value:
            mul
            mul*=num
        return mul