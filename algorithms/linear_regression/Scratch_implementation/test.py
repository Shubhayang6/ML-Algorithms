import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from LinearRegression import Linear_regression

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)


fig = plt.figure(figsize=(8, 6))
plt.title("Raw Data Distribution")
plt.scatter(X[:, 0], y, c="b", marker="o", s=30)
plt.show()

reg = Linear_regression(lr = 0.01)
reg.fit(X_train, y_train)
prediction = reg.predict(X_test)


def mse(y_test, prediction):
    return np.mean((y_test - prediction) ** 2)


mse = mse(y_test, prediction)
print(mse)

y_pred_line = reg.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8, 6))
plt.title("Model Fit: Predictions vs Actual")
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
plt.show()
