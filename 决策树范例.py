from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO


f=open(r'D:\BaiduNetdiskDownload\AllElectronics.csv','r')# r加上路径，‘r’文件权限为只读，具体可百度open用
reader = csv.reader(f)
headers = next(reader)
featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]   #一个词典dict的创建方法
    featureList.append(rowDict)

# Vetorize（矢量化）  features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList) .toarray()    #提取了dict(featureList)中的所有features，转化成为二进制

# print(dummyX)
print(vec.get_feature_names()) #展示所有dummyX中的features
#print(labelList)

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
#print( dummyY)

# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
#print("clf: " + str(clf))

# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))  #48-54创建一个新的例子，将表格中第一行的数据中的yonth改成了middle，其他不变

predictedY = clf.predict(newRowX)#调用clf.predict（）进行预测，1为买，0为不买
print("predictedY: " + str(predictedY))
