def randomlyAssignWeights():
    w = [[uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), ]
         for row in range(9)]
    v = [[uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), uniform(-1, 1),
          uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), ] for row in range(4)]

    w = [[0.1, -0.2, 0.3, ],
         [0.4, 0.1, 0.1],
         [0.3, 0.3, 0.7],
         [0.6, 0.7, -0.8],
         [-0.5, 0.4, 0.2],
         [0.1, 0.5, 0.5],
         [0.4, 0.6, 0.3],
         [0.2, 0.9, -0.1],
         [-0.4, -0.1, 0.6]]

    v = [[0.4, -0.8, 0.2, 0.6, 0.7, -0.5, 0.2, -0.4, ],
         [0.9, 0.7, 0.3, 0.2, -0.1, 0.6, 0.4, -0.8],
         [0.1, 0.2, 0.7, -0.8, 0.5, 0.4, 0.1, 0.1, ],
         [0.9, 0.1, 0.8, -0.4, 0.2, 0.7, -0.3, 0.8, ]]

    return w, v


def mult(v, m):
    assert len(v) == len(m), [len(v), len(m)]
    return [sum([v[i]*m[i][j]
                for i in range(len(v))])
                    for j in range(len(m[0]))]

def printAllData(w,h,v,y):
    print('x =')
    for cell in INPUTS:
        print(cell)
    print("="*50)

    print('w =')
    for row in w:
        for cell in row:
            print(cell, end=", ")
            print()
    print("="*50)

    print("h =")
    for cell in h:
        print(cell)
    print("="*50)

    print("v = ")
    for row in v:
        for cell in row:
            print(cell, end=", ")
        print()
    print("="*50)

    print("y =", y)
    for cell in y:
        print(cell)
    print("="*50)

def f(x):
    return 1/(1 + exp(-x))

def feedForward(x,w,v):
    
def backPropogation(x,w,dp,h,v,DP,y):
    return w, v

def trained(w, v):
    

def verifyNetwork(epochs, w, v):
    

def trainNetwork():
    epochs = 0
    w,v = randomlyAssignWeights()

    while epochs < TRIALS and not trained(w,v):
        for x in INPUTS:
            dp, h, DP, y = feedForward(x,w,v)
            w, v = backPropogation(x,w,dp,h,v,DP,y)
        epochs += 1
        print('epochs =', epochs)
    return epochs, w, v

from random import random, choice, shuffle, uniform, randint
from math import exp

TRIALS = 9000
ALPHA = 0.25
INPUTS = [ [0]*x + [1] + [0]*(7-x) + [-1] for x in range(8)]

def main():
    epochs, w, v = trainNetwork()
    verifyNetwork(epochs, w, v)

if __name__ == '__main__':
    main()

