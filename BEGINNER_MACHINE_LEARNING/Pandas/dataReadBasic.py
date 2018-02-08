import pandas as pd

dataSet = pd.read_csv('../DATA_SET/regression.csv')


def data_Set():
    print("DATA SET : ")
    print(dataSet.head())


# date attribute
def dateAttribute():
    print("########### DATE ###########")
    date = dataSet['date']
    print(date)


def highAttribute():
    print("############### high ##################")
    high = dataSet['high']
    print(high.head())



def lowAttribute():
    print("================= Low ===============")
    low=dataSet['low']
    print(low.head())
   # print(dataSet.low)


def volume():
    print("%%%%%%%%%%%%%%%%% Volume %%%%%%%%%%%%%%%%")
    volume=dataSet['volume']
    print(volume)

def dropColumn():
    print("drop")
    dataSet.drop(['low'],axis=1,inplace=True)
    dataSet.drop(['ticker'],axis=1,inplace=True)
    dataSet.drop(['date'],axis=1,inplace=True)
    print(dataSet.head())





# main function's functionalities are implemented here


def main():

    data_Set()
    dropColumn()
   # highAttribute()
   # lowAttribute()
    #volume()
    return 0


if __name__ == '__main__':
    main()
