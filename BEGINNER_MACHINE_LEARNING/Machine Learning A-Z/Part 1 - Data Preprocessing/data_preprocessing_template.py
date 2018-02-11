# data preprocessing

# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def preProcessing():
    dataset = pd.read_csv('Data.csv')
    # print(dataset)
    xMatrix = dataset.iloc[:, :-1].values
    yMatrix=dataset.iloc[:,3].values
    print(yMatrix)
    print(xMatrix[[2]])







if __name__ == '__main__':
    preProcessing()
