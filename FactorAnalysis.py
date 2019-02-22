# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def Normalize (vector):
    norm = np.linalg.norm(vector)
    if norm == 0: 
       return vector
    return vector / norm
    
    
def GetMultiplicityAndIndexes(V, value):
    multiplicityList = []
    
    for i, j in enumerate(V):
        if j == value:
            multiplicityList.append(i)
        
    return(len(multiplicityList), multiplicityList)
    

def Get2LargestEigenV (V, U):
    #Returns a tuple formed by a list of eigenvalues (decreasing order)
    #and a list of corresponding normalized eigenVector (indexes correspond to associated eigenvalues)
    multiplicityTuple = GetMultiplicityAndIndexes(V, max(V))
    
    if multiplicityTuple[0] > 1:
        value1, value2 = max(V), max(V)
        vector1, vector2 = U[multiplicityTuple[1][0]], U[multiplicityTuple[1][1]]
        
    elif multiplicityTuple[0] == 1:
        value1 = max(V)
        vector1 = U[multiplicityTuple[1][0]]
        
        copiedV = list(V.copy())
        copiedU = list(U.copy())
        
        copiedV.pop(multiplicityTuple[1][0])
        copiedU.pop(multiplicityTuple[1][0])
        
        value2 = max(copiedV)
        vector2 = copiedU[GetMultiplicityAndIndexes(copiedV, max(copiedV))[1][0]]
        
    return ( [value1, value2], [Normalize(vector1), Normalize(vector2)] )


def GetTransformMatrix(vectorList):
    transformMatrix=[]
    for i in range(0,len(vectorList[0])):
        transformMatrix.append([vectorList[0][i], vectorList[1][i]])
    
    return transformMatrix


def GetInformationLoss(inputMatrix):
    informationLoss= 0
    
    transposedInputMatrix = inputMatrix.T
    squareInputMatrix =  np.dot(transposedInputMatrix, inputMatrix)
    V, U = np.linalg.eig(squareInputMatrix)
    
    for val in V:
        informationLoss += val
        
    largestEigenValues = Get2LargestEigenV(V,U)[0]
        
    informationLoss = 1 - ( (largestEigenValues[0] + largestEigenValues[1]) / informationLoss)
    
    return informationLoss

def Get2DProjectedMatrix(inputMatrix):
    transposedInputMatrix = inputMatrix.T
    squareInputMatrix =  np.dot(transposedInputMatrix, inputMatrix)
    V, U = np.linalg.eig(squareInputMatrix)
    eigenTuple = Get2LargestEigenV(V,U)
    transformMatrix = GetTransformMatrix(eigenTuple[1])
    projectedMatrix = np.dot(inputMatrix, transformMatrix)
    
    return projectedMatrix

def Plot2DMatrix(matrix):
    try:
        plt.plot(matrix.T[0], matrix.T[1], 'ro')
        plt.show()
    except Exception as e:
        print(e)
    
    

if __name__ == "__main__":
    
    """
    inputMatrix = np.array([[1, 0, -1],
                            [0, 1, -1],
                            [-1, 1, 0],
                            [0, -1, 1],
                            [-1, 0, 1],
                            [1, -1, 0]], dtype = np.float32)
    
    
    projectedMatrix = Get2DProjectedMatrix(inputMatrix)
    Plot2DMatrix(projectedMatrix)
    print("Information Loss : ",GetInformationLoss(inputMatrix))
	"""
    
    