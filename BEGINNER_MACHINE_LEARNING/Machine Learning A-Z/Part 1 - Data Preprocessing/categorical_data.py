import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder


def categorized():
    dataset=pd.read_csv('Data.csv')
    print(dataset)
    xMatrix=dataset.iloc[:,:-1].values
    #print(xMatrix)
    yMatrix=dataset.iloc[:,3:].values
    #print(yMatrix)
    imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
    print(imputer)
    imputer_fit=imputer.fit(xMatrix[:,1:3])
    xMatrix[:,1:3]=imputer_fit.fit_transform(xMatrix[:,1:3])
    print("Missing Data is filled by mean")
    print(xMatrix)
    #mapping first column with unique numerical value
    LabelEncoder_X=LabelEncoder()
    print(xMatrix[:,0])
    xMatrix[:,0]=LabelEncoder_X.fit_transform(xMatrix[:,0])
    print(xMatrix[:,0])












def main():
    categorized()
    return 0




if __name__ == '__main__':
    main()



