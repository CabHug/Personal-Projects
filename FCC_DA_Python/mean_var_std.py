import numpy as np

def calculate(input: list):
    arr_org = np.array(input)
    arr = np.copy(arr_org)
    n_axis = 3
    matrix = arr.reshape(n_axis, n_axis)
    output = {
        'mean': [np.mean(matrix, axis=0), np.mean(matrix, axis=1), matrix.flatten().mean()],
        'variance': [np.var(matrix, axis=0), np.var(matrix, axis=1), matrix.flatten().var()],
        'standard deviation': [np.std(matrix, axis=0), np.std(matrix, axis=1), matrix.flatten().std()],
        'max': [np.max(matrix, axis=0), np.max(matrix, axis=1), matrix.flatten().max()],
        'min': [np.min(matrix, axis=0), np.min(matrix, axis=1), matrix.flatten().max()],
        'sum': [np.sum(matrix, axis=0), np.sum(matrix, axis=1), matrix.flatten().sum()]
    }
    print(output)
    

calculate([0,1,2,3,4,5,6,7,8])

