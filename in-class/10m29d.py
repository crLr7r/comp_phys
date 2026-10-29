import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [4,5,10,4,3,11,14,8,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
classes = [0,0,1,0,0,1,1,0,1,1]

# plt.scatter(x,y,c=classes)
# plt.show()

# fit the KNN algorithm with K=1:
data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(data, classes)

new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c=classes+[prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
# plt.show()

from sklearn import datasets

iris = datasets.load_iris()
#
# print("Iris Dataset Overview\n")
# print("Keys: ", iris.keys(), "\n")
#
# print("Description:\n", iris['DESCR'][:2000], "\n...")
# print("\nFeature Names:\n", iris['feature_names'], "\n")
# print("Target Names:\n", iris['target_names'], "\n")
#
# print("Data (features):\n", iris['data'], "\n")
# print("Target (class labels):\n", iris['target'])


fig, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0],
    iris.target_names,
    loc="lower right",
    title="Classes"
)

plt.show()


