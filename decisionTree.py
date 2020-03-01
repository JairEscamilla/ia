from sklearn import tree
from sklearn.neighbors import NearestCentroid
from sklearn.neural_network import MLPClassifier
 
# [height, weight, show size], 
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], 
    [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'male']

# Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[170, 15, 20]])
print(prediction)

# NearestCentroid classifier
clf = NearestCentroid()
clf.fit(X, Y)
prediction = clf.predict([[170, 15, 20]])
print(prediction)

# MLP Classifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=0)
clf.fit(X, Y)
print(clf.predict([[170, 15, 20]]))