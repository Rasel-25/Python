def add(*args):
    """Custom module"""
    sum=0
    for num in args:
        sum+=num
    return sum    


data=172311030   


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
print("Custom modules")   
if __name__=='__main__':

    print("Custom modules")    

# pip --> command use to show everything 
# pip list --> show all packages and  their version