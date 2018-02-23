import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer
from  sklearn.preprocessing import LabelEncoder

def missingDatafinder():
    # data set read
    dataset = pd.read_csv('missingData.csv')
    xMatrix=dataset.iloc[:,:-1].values
    yMatrix =dataset.iloc[:,3].values
    #print(yMatrix)
    print(xMatrix)
    imputer =Imputer(missing_values='NaN',strategy='mean',axis=0)
    print(imputer)
    imputer.fit(xMatrix[:,1:3])
    print(imputer)
    xMatrix[:,1:3]=imputer.transform(xMatrix[:,1:3])
    print(xMatrix)





def main():
    missingDatafinder()
    return 0


if __name__ == '__main__':
    main()
