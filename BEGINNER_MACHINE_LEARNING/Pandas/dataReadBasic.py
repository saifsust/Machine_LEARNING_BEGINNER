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

# main function's functionalities are implemented here


def volume():
    print("%%%%%%%%%%%%%%%%% Volume %%%%%%%%%%%%%%%%")
    volume=dataSet['volume']
    print(volume)
def main():

    data_Set()
   # highAttribute()
    lowAttribute()
    #volume()
    return 0


if __name__ == '__main__':
    main()
