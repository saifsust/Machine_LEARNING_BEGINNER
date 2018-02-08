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
    low = dataSet['low']
    print(low.head())
    # print(dataSet.low)


def volume():
    print("%%%%%%%%%%%%%%%%% Volume %%%%%%%%%%%%%%%%")
    volume = dataSet['volume']
    print(volume)


def Drop(attribute):
    dataSet.drop([attribute], axis=1, inplace=True)


def matrix():
    print("drop")
    Drop('ex-dividend')
    Drop('adj_open')
    Drop('adj_high')
    Drop('adj_low')
    Drop('adj_close')
    Drop('adj_volume')
    Drop('split_ratio')
    Drop('ticker')
    Drop('date')
# main function's functionalities are implemented here


def main():
    matrix()
    #print(dataSet.sort_values(['high','low']).head())
    data_Set()
    print(dataSet.describe())
    print(dataSet.low)
    print(dataSet.dtypes)
    print(dataSet.columns)
    return 0


if __name__ == '__main__':
    main()
