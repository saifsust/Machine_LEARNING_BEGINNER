from sklearn import datasets
from sklearn import  metrics
from sklearn.svm import SVC
dataSet =datasets.load_iris()
#print(dataSet)


model = SVC()
model.fit(dataSet.data,dataSet.target)

print(model)
expected = dataSet.target
predicted =model.predict(dataSet.data)
print(expected)
print(predicted)
print(metrics.classification_report(expected,predicted))
#print(expected)
def main():
    return 0

if __name__ == '__main__':
    main()
