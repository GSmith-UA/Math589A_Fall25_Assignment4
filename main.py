import numpy as np
import fp_wrapper as fp
def main():
    # Here we seek to run some values through the fp_wrapper.py and the corresponding c code.

    for k in range(10,100,10):
        scale = 1/k
        # print(scale)
        x0 = 0.5
        x1 = 0.5
        tol = 1e-6
        maxIterations = 1000

        sol1,sol2,iterations = fp.solve_system(x0,x1,tol,maxIterations,scale)
        print("It took ", iterations, " iterations")

    return None

main()