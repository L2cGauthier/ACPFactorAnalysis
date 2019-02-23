# Principal Component Analysis and 2D representation of multi-dimensional matrices

This project is a learning experiment. It's aimed at using principal component analysis in order to represent multi-dimensional data sets in 2 dimensions while minimizing the loss of information.

## Principal Component Analysis

The idea of PCA is to use some linear algebra in order to transform a matrix made out of n observations of p features into a matrix containing n observations of 2 linearly uncorrelated "synthetic" features. Depending on the order of magnitude of p, and their existing correlation, this transformation can provoke a loss of information.

The principles of the PCA method are the following.

1. Code your data set as a numerical matrix X of dimension nxp
2. Compute the matrix X<sup>T</sup>X, which is proportional to the empirical sample covariance matrix of X, of dimension pxp. Conveniently, X<sup>T</sup>X is a symmetric positive definite matrix, meaning that, by property, it is diagonalizable.
3. Find the 2 distinct biggest eigenvalues ($\lambda$<sub>1</sub>, $\lambda$<sub>2</sub>), and a respective normed associated eigenvectors (U<sub>1</sub> \lambda<sub>2</sub>) for each of them.
4. Let U be the concatenation of U<sub>1</sub> and U<sub>2</sub>, a matrix of dimension px2.
5. Project the matrix X onto the eigenvectors by calculating the resulting matrix : X.U = X', a matrix of dimension nx2, hence easily representable in R<sup>2</sup>

We can show that the fact we take the two biggest eigenvalues in 3. guarantees that the distance between the projected data and the origin are as close as possible to the distance in the original data set. In other word, by choosing this eigenvalues, we know that the loss of information will be minimized.

The loss of information can be calculated as : I = 1 - $\frac{\lambda_1 + \lambda_2}{\sum{i} \lambda_i} $






```

## Visualization

If we consider spaces of dimension 1 to 100, and measure the mean and minimum distances between 10k pairs of random points with coordinates in [0,1], we obtain the following plot.


![Curse of dimensionality visualization](https://github.com/L2cGauthier/CurseOfDimensionality/blob/master/Results/100D-10kpairs.png?raw=true)


We observe that the average distance between pairs is increasing steadily and rapidly. To be more precise, given the fact we generated points which coordinates are uniformly distributed in [0,1], if the number of pair generated is high enough, we can write the function f associating the average distance between pairs to the number of dimension x as:


<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" title="f(x) = \sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}} = \frac{1}{2}\sqrt{x}" /></a>


The minimum distance between pairs is always smaller than the mean but increases at roughly the same rate.



