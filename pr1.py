#import library (numpy)
import numpy as np
#Enter value of rows and columns
m = int(input("Enter number of rows: "))
n = int(input("Enter number of colunms: "))
#Enter rows of matrix
print("Start entering rows of the matrix:")
#make list named A
A = []
#for loop to read data from rows
for i in range(m):
    #add each number to list A
    #creat an array
    A.append(np.array(list(map(float, input().strip().split()[:n]))))
#put array into the list
A = np.array(A)
#define function for calculate Q
def getQ(M):
    #make a list of Q
    Q = []
    #transposed matrix
    M = np.transpose(M)
    for i in range(len(M)):
    #copy data to vector named v
        v = np.copy(M[i])
        for j in range(i):
            v -= (np.dot(M[i], Q[j]) / np.dot(Q[j], Q[j])) * Q[j]
        Q.append(v)
    Q = np.array(list(map(lambda v: v / sum(v**2)**0.5, Q)))
    Q = Q.transpose()
    return Q
#define function for calculate R
def getR(M, Q):
    Qt = np.transpose(Q)
    return np.matmul(Qt, M)

Q = getQ(A)
R = getR(A, Q)

#define function for round numbers
def nro_round(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = round(M[i][j], 4)

#round numbers
nro_round(Q)
nro_round(R)

#print output
print("\nQ:\n", Q)
print("\nR:\n", R)
