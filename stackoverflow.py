class test:
    def __init__(self,raw_data):
        self.method1 = raw_data*10
    
    def compute_method_2(self,raw_data):    
        self.method2 = raw_data*20
        
    def compute_method_3(self,raw_data):    
        self.method3 = raw_data*30
# a quick test using "raw_data = 1"
output = test(1)

# run other computations
output.compute_method_2(1)
output.compute_method_3(1)

# now all the values are available
print(output.method1)
print(output.method2) 
print(output.method3)