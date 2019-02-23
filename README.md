# Principal Component Analysis and 2D representation of multi-dimensional matrices

This project is a learning experiment. It's aimed at using principal component analysis in order to represent multi-dimensional data sets in 2 dimensions while minimizing the loss of information.

## Principal Component Analysis

The idea of PCA is to use some linear algebra in order to transform a matrix made out of n observations of p features into a matrix containing n observations of 2 linearly uncorrelated "synthetic" features. Depending on the order of magnitude of p, and their existing correlation, this transformation can provoke a loss of information.

The principles of the PCA method are the following.

1. Code your data set as a numerical matrix X of dimension nxp
2. Compute the matrix X<sup>T</sup>X, which is proportional to the empirical sample covariance matrix of X, of dimension pxp. Conveniently, X<sup>T</sup>X is a symmetric positive definite matrix, meaning that, by property, it is diagonalizable.
3. Find the 2 distinct biggest eigenvalues (&lambda<sub>1</sub>, &lambda<sub>2</sub>), and a respective normed associated eigenvectors (U<sub>1</sub> \lambda<sub>2</sub>) for each of them.
4. Let U be the concatenation of U<sub>1</sub> and U<sub>2</sub>, a matrix of dimension px2.
5. Project the matrix X onto the eigenvectors by calculating the resulting matrix : X.U = X', a matrix of dimension nx2, hence easily representable in R<sup>2</sup>

We can show that the fact we take the two biggest eigenvalues in 3. guarantees that the distance between the projected data and the origin are as close as possible to the distance in the original data set. In other word, by choosing this eigenvalues, we know that the loss of information will be minimized.

The loss of information can be calculated as :

<a href="https://www.codecogs.com/eqnedit.php?latex=I&space;=&space;1&space;-&space;\frac{\lambda_1&space;&plus;&space;\lambda_2}{\sum_{i}^{p}&space;\lambda_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I&space;=&space;1&space;-&space;\frac{\lambda_1&space;&plus;&space;\lambda_2}{\sum_{i}^{p}&space;\lambda_i}" title="I = 1 - \frac{\lambda_1 + \lambda_2}{\sum_{i}^{p} \lambda_i}" /></a>


## Visualization

We use the script test.py to generate a random dataset of n points with p dimensions, forming 1 to 4 distinguishable clusters.

With n = 400 and p = 5, we obtain the following representation with an information loss of 0.033 :

![PCA illustration 1](https://github.com/L2cGauthier/ACPFactorAnalysis/blob/master/Example/Results/5D-400p-MatrixProj01_InfoLoss=0.033.png?raw=true)

With n = 400 and p = 20, we obtain the following representation with an information loss of 0.057 :

![PCA illustration 2](https://github.com/L2cGauthier/ACPFactorAnalysis/blob/master/Example/Results/20D-400p-MatrixProj03_InfoLoss=0.057.png?raw=true)

With n = 400 and p = 50, we obtain the following representation with an information loss of 0.059 :

![PCA illustration 3](https://github.com/L2cGauthier/ACPFactorAnalysis/blob/master/Example/Results/50D-400p-MatrixProj04_InfoLoss=0.059.png?raw=true)

With n = 1,000 and p = 15, we obtain the following representation with an information loss of 0.053 :

![PCA illustration 3](https://github.com/L2cGauthier/ACPFactorAnalysis/blob/master/Example/Results/15D-1000p-MatrixProj06_InfoLoss=0.053.png?raw=true)








