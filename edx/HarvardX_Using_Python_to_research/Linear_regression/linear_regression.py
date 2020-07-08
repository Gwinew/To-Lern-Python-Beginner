# Introduction to statistical Learning
# Supervised statistical learning
# regression

# Quantitative or qualitative

# if outcome is quantitative, we talk about regression problems
# if outcome is qualitative - its classification problems
# its both if we get output without inputs....

# loss function

# Regression:Squared error loss

#E(Y| X=x)
#f(x)  # type regression line function

#P(Y=0|X=x)
#P(Y=1|X=x)

#___________________________________
# Generating Example Regression Data

import numpy as np

import scipy.stats as ss

import matplotlib.pyplot as plt

n = 100

beta_0 = 5
beta_1 = 2
np.random.seed(1)

x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

plt.figure()
plt.plot(x, y, "o", ms=5)

xx = np.array([0,10])
plt.plot(xx, beta_0 + beta_1 * xx)
plt.xlabel("x")
plt.ylabel("y")


# Simple Linear regression
# Y = B0 + B1 X + epsi
# y^ = ^B0 + ^B1 x
# ei = yi - ^yi
# RSS = e1^2 +e2^2 +...+en^2


# Least squares Estimation in Code


rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
	rss.append(np.sum((y- beta_0 - slope * x)**2))

ind_min = np.argmin(rss)

print("Estimate for the slope: ", slopes[ind_min])

#Plot figure
plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS");

# An additional note on this video:
#Note that in this case, the estimated value of the parameter (2.0) coincides with the true value of the parameter. Generally, we do
#not know the underlying true value, but here it is known to us because we generated the data ourselves. In practical settings, the
#estimated parameter value may not always match the true value.

#_________________________________
# Simple Linear Regression in code

import statsmodels.api as sm

mod = sm.OLS(y, x)
est = mod.fit()
print(est.summary())

X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()

print(est.summary())

# Sampling distributions of the parametr estimates


#__________________________________
# Multiple Linear Regression


# Scikit-learn for Linear Regression

n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1

np.random.seed(1)
x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x_1 +beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)

X = np.stack([x_1, x_2], axis=1)
# 3 dimensial plot

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$");

from sklearn.linear_model import LinearRegression

lm = LinearRegression(fit_intercept=True)

lm.fit(X, y)

lm.intercept_

lm.coef_[0]

lm.coef_[1]

X_0 = np.array([2, 4])

lm.predict(X_0)

lm.predict(X_0.reshape(1, -1))  # after warning

lm.score(X, y) # r-squared output



#Assesing Model accuracy
# Mean Squared error = MSE

# MSE = 1/n * sum (yi-^f(xi))^2


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)

lm = LinearRegression(fit_intercept=True)

lm.fit(X_train, y_train)

lm.score(X_test, y_test)
