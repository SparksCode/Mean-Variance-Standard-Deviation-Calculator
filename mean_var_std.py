import numpy as np

def calculate(list):

  #Verify list size contains 9 numbers. 
  try:
    a = np.reshape(list, (3,3))
  except:
    raise ValueError("List must contain nine numbers.")

  #Perform calculations
  mean = [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a)]
  variance = [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a)]
  std = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a)]
  max = [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a)]
  min = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a)]
  sum = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a)]

  #Build dictionary
  calculations = {
    "mean": mean, 
    "variance": variance, 
    "standard deviation": std, 
    "max": max,
    "min": min,
    "sum": sum
    }
  
  return calculations