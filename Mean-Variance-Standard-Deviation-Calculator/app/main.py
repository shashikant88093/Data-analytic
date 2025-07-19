import numpy as np

def calculator(input_list):
  if len(input_list) != 9:
    raise ValueError("List must contains 9 numbers.")
  
  matrix = np.array(input_list).reshape(3,3)
  print(matrix)
#   mean = a +b+c+d/4
# variance 
  calculations = {
        'mean': [matrix.mean(axis=0).tolist()
               #   adding a0 + a1 + a3 = 3 it is adding in x axis

                 ,matrix.mean(axis=1).tolist()
               #   adding a0 + a1 + a3 = 3 it is adding in x axis
                 ,
                 matrix.mean().tolist()]
                 # adding mean of x=axis and y-axis
                 ,
        'variance':[matrix.variance(matrix,axis=0)]
        
    }
  return calculations
arr = [0,1,2,3,4,5,6,7,8]
print(calculator(arr))

