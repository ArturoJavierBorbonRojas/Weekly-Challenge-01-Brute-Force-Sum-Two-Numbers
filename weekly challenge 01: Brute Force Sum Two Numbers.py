import numpy as np

# Author: Ing. Arturo Javier Borbon Rojas.

# 1 Generate pseudo random values:
#n= 10 # number of elements
n=np.random.randint(0,100)
objective_value= np.random.randint(0,100)
value1= np.random.randint(0,100,n)

# 2 Print our pseudo random values
print("------------------")
print(" Our pseudo random values")
print("Our objective value is: ", objective_value)
print(f"The pseudo random list is:{value1} with n={n} objets")
print("------------------")

# 3 Def function brute force sum two numbers
def brute_two_value(nums, target):
    counter=0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            counter+=1
            if nums[i] + nums[j] ==target:
                return f"Found it! Index {i},{j} (Values: {nums[i]} + {nums[j]}) in {counter} attempts.""\n-----------" 
           
    return "There is no solution" "\n-----------"  
 # 4 Print function with our data
print("Bruce force method: ", brute_two_value(value1, objective_value))



