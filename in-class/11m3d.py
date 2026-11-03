import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import pandas as pd

from sklearn.datasets import load_iris
iris_dataset = load_iris()

type(iris_dataset)
print("key value from iris_dataset:", iris_dataset.keys())

print(iris_dataset['DESCR'])
print(iris_dataset['DESCR'][:500] + "\n...")

print("feature_names value from iris_dataset:", iris_dataset['feature_names'])
print("target_names value from iris_dataset:", iris_dataset['target_names'])

iris = pd.read_csv("iris.csv")
iris.head()

x_iris = iris[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
y_iris = iris[["variety"]]

x_iris_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
x_iris.columns = x_iris_columns
x_iris.head(5)

y_iris['variety'].unique()

print(("x_axis", x_iris.columns))
print(("y_axis", y_iris))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_iris, y_iris, test_size=0.3, random_state=0)

print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)

print("x_test shape:", x_test.shape)
print("y_test shape:", y_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

print(y_train.shape)
print(y_train.values.ravel().shape)

knn.fit(x_train, y_train.values.ravel())

import numpy as np
our_x = np.array([[5, 2.9, 1, 0.2]])

prediction = knn.predict(our_x)
print("prediction:", prediction)

y_pred = knn.predict(x_test)
print("prediction of test set:", y_pred)

y_test_flatten = np.array(y_test).flatten()

print(f"accuracy of test set: {np.mean(y_pred == y_test_flatten):.2f}")

print(f"accuracy of test set: {knn.score(x_test, y_test_flatten):.2f}")