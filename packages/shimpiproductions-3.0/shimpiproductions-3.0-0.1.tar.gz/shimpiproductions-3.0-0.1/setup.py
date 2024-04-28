from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    DESCRIPTION = f.read()

# Define a summary for your package
SUMMARY = '''import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error


#----------------------------------------------------------------------------------------------------------#

X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Synthetic Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


#----------------------------------------------------------------------------------------------------------#

# Pre-processing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#----------------------------------------------------------------------------------------------------------#

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#----------------------------------------------------------------------------------------------------------#

# KNN Classification
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)


#----------------------------------------------------------------------------------------------------------#

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)

#----------------------------------------------------------------------------------------------------------#


# SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_pred)


#----------------------------------------------------------------------------------------------------------#


# Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)

#----------------------------------------------------------------------------------------------------------#

# K-means Clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X_scaled)
cluster_centers = kmeans.cluster_centers_


#----------------------------------------------------------------------------------------------------------#

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_rmse = mean_squared_error(y_test, lr_pred, squared=False)

classifiers = ['KNN', 'Decision Tree', 'SVM', 'Random Forest', 'Linear Regression']
accuracies = [knn_accuracy, dt_accuracy, svm_accuracy, rf_accuracy, lr_rmse]


plt.bar(classifiers, accuracies)
plt.xlabel('Classifiers')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Classifiers')
plt.show()

#----------------------------------------------------------------------------------------------------------#

#Desion Tree
from sklearn.tree import plot_tree

# Visualize decision tree
plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True, feature_names=['Feature 1', 'Feature 2'], class_names=['Class 0', 'Class 1', 'Class 2', 'Class 3'])
plt.title('Decision Tree Visualization')
plt.show()

# Visualize one decision tree from random forest (change index to visualize different trees)
plt.figure(figsize=(12, 8))
plot_tree(rf.estimators_[0], filled=True, feature_names=['Feature 1', 'Feature 2'], class_names=['Class 0', 'Class 1', 'Class 2', 'Class 3'])
plt.title('Decision Tree from Random Forest')
plt.show()


#----------------------------------------------------------------------------------------------------------#

# Visualize SVM decision boundaries
plt.figure(figsize=(12, 8))
h = .02  # step size in the mesh
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.viridis, alpha=0.8)

# Plot the dataset
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis')
plt.title('SVM Decision Boundaries')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


#----------------------------------------------------------------------------------------------------------#

# Visualize KNN decision boundaries
plt.figure(figsize=(12, 8))
h = .02  # step size in the mesh
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.viridis, alpha=0.8)

# Plot the dataset
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis')
plt.title('KNN Decision Boundaries')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


#----------------------------------------------------------------------------------------------------------#

# Visualize K-means clustering
plt.figure(figsize=(12, 8))

# Plot the dataset
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis', alpha=0.5)

# Plot cluster centroids
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=100, label='Cluster Centroids')

plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()


# Visualize Linear Regression
plt.figure(figsize=(12, 8))

# Plot the training data
plt.scatter(X_train[:, 0], y_train, color='blue', label='Training Data')

# Plot the test data
plt.scatter(X_test[:, 0], y_test, color='green', label='Test Data')

# Plot the regression line
plt.plot(X_test[:, 0], lr.predict(X_test), color='red', linewidth=2, label='Linear Regression')

plt.title('Linear Regression')
plt.xlabel('Feature 1')
plt.ylabel('Target Variable')
plt.legend()
plt.show()


#----------------------------------------------------------------------------------------------------------#

#K-fold

import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np

model = SVC(kernel='linear')

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X_train, y_train, cv=kfold)

plt.figure(figsize=(8, 6))
plt.plot(np.arange(1, 6), scores, marker='o', linestyle='-')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.title('K-Fold Cross-Validation Scores')
plt.grid(True)
plt.show()

#----------------------------------------------------------------------------------------------------------#

# Visualize SVM decision boundaries with polynomial kernel
svm_poly = SVC(kernel='poly', degree=3)  # Polynomial kernel with degree 3
svm_poly.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
h = .02  # step size in the mesh
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = svm_poly.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.viridis, alpha=0.8)

# Plot the dataset
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis')
plt.title('SVM Decision Boundaries with Polynomial Kernel')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
'''

VERSION = '0.1'

setup(
    name="shimpiproductions-3.0",
    version=VERSION,
    author="Sarvesh Shimpi",
    author_email="sarveshshimpi18@gmail.com",
    description=SUMMARY,  # Add the summary here
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn', 'opencv-python'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    entry_points={
        "console_scripts": [
            "shimpiproductions=shimpiproductions:hi",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
