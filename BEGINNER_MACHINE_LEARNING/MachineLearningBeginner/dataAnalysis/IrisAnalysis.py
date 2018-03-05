import pandas as pd
import numpy as np

'''Global Properties'''
dataset = ''

# constant
IRIS = '../dataset/iris.csv'

# dataset read method
def readDataset(path):
    return pd.read_csv(path)

def main():
    dataset = readDataset(IRIS)
    print(dataset)
    return 0


if __name__ == '__main__':
    main()
