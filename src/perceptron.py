## Modelo de perceptron usando database iris

import matplotlib
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pprint
rcParams["figure.figsize"] = 10, 5
#%matplotlib inline

# load iris dataset from sklearn
iris = datasets.load_iris()

# separate features and targets
X = iris.data
y = iris.target

print(y)

# now we'll use `train_test_split` from skleanr
# to split the data into training and testing sets
test_size = 0.3
random_state = 0

# `train_test_split` convenience function
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=random_state
)

# stardardize the data like we did before, but use
# the `StandardScaler` from sklearn

# create the instance
sc = StandardScaler()

# fit the scaler to the training featrue set ONLY
sc.fit(X_train)

# scale (transform) the training AND the testing sets
# using the scaler that was fitted to training data
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# it is important to transform non-numeric target
# values into numbers prior to splitting the data
# to avoid unexpected results when modeling
print('Unique labels: {0}'.format(np.unique(y)))

# we will select a subset of the features as before
X_train_std = X_train_std[:, [2, 3]]
X_test_std = X_test_std[:, [2, 3]]

# let's train a model using the sklean
# implementation of perceptron
n_iter = 40
eta0 = 0.1 # same as `eta` (learn rate) in our implementation

# create the perceptrion instance
ppn = Perceptron()
ppn = Perceptron(
    max_iter=n_iter,
    eta0=eta0,
    random_state=random_state)

# fit the model to the standardized data
ppn.fit(
    X_train_std,
    y_train)

# make predictions!
y_pred = ppn.predict(X_test_std)

# we can measure performance using the `accuracy_score`
# convenience function in sklearn
print("accuracy: {0:.2f}%".format(accuracy_score(y_test,y_pred) * 100))

# let's add some functionality to our `plot_decision_regions`
# convenience function by highlighting the test samples
# on our plot