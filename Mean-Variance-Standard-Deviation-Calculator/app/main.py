import numpy as np

def calculator(input_list):
  if len(input_list) != 9:
    raise ValueError("List must contains 9 numbers.")
  
  matrix = np.array(input_list).reshape(3,3)
  print(matrix)
  calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }
  return calculations
arr = [1,2,3,4,5,6,7,8,9]
print(calculator(arr))

