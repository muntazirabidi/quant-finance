# Kernels and Reproducing Kernel Hilbert Spaces

## 1. Introduction to Kernels

We've seen how quadratic effects models can be fitted efficiently by replacing the inner product matrix (Gram matrix) $XX^T$ with a modified matrix. This raises the question: what other non-linear models can be fitted efficiently using similar approaches?

### 1.1 Basic Concepts

We study similarity measures $k: X \times X \to \mathbb{R}$ from input space $X$ to $\mathbb{R}$ where there exists a feature map $\phi: X \to H$ with $H$ being some (real) inner product space such that:

$$
k(x,x') = \langle \phi(x), \phi(x') \rangle
$$

An inner product space is a real vector space $H$ with map $\langle \cdot, \cdot \rangle: H \times H \to \mathbb{R}$ that satisfies:

1. **Symmetry**: $\langle u,v \rangle = \langle v,u \rangle$
2. **Linearity**: For $a,b \in \mathbb{R}$, $\langle au + bw,v \rangle = a\langle u,v \rangle + b\langle w,v \rangle$
3. **Positive-definiteness**: $\langle u,u \rangle \geq 0$ with equality if and only if $u = 0$

### 1.2 Definition of Kernels

**Definition 1**: A positive definite kernel (or simply kernel) $k$ is a symmetric map $k: X \times X \to \mathbb{R}$ where for all $n \in \mathbb{N}$ and all $x_1,...,x_n \in X$, the matrix $K$ with entries $K_{ij} = k(x_i,x_j)$ is positive semi-definite.

**Proposition 2** (Cauchy-Schwarz for Kernels):

$$
k(x,x')^2 \leq k(x,x)k(x',x')
$$

**Proof**: The matrix

$$
\begin{pmatrix}
k(x,x) & k(x,x') \\
k(x',x) & k(x',x')
\end{pmatrix}
$$

must be positive semi-definite, so its determinant must be non-negative.

**Proposition 3**: $k$ defined by $k(x,x') = \langle \phi(x), \phi(x') \rangle$ is a kernel.

**Proof**: For any $x_1,...,x_n \in X$ and $\alpha_1,...,\alpha_n \in \mathbb{R}$:

$$
\sum_{i,j} \alpha_i k(x_i,x_j)\alpha_j = \sum_{i,j} \alpha_i \langle \phi(x_i),\phi(x_j) \rangle \alpha_j = \left\langle \sum_i \alpha_i\phi(x_i), \sum_j \alpha_j\phi(x_j) \right\rangle \geq 0
$$

## 2. Examples of Kernels

**Proposition 4**: For kernels $k_1, k_2, ...$:

1. If $\alpha_1, \alpha_2 \geq 0$ then $\alpha_1k_1 + \alpha_2k_2$ is a kernel. If $\lim_{m \to \infty} k_m(x,x') = k(x,x')$ exists for all $x,x'$, then $k$ is a kernel.
2. The pointwise product $k = k_1k_2$ is a kernel.

### 2.1 Common Kernel Types

1. **Linear Kernel**:
   $$k(x,x') = x^T x'$$

2. **Polynomial Kernel**:
   $$k(x,x') = (1 + x^T x')^d$$
   This is a kernel because 1 is a kernel, and using Proposition 4.

3. **Gaussian Kernel**:
   $$k(x,x') = \exp\left(-\frac{\|x-x'\|^2_2}{2\sigma^2}\right)$$

   - For $x$ close to $x'$, it's large
   - For $x$ far from $x'$, it decays to 0
   - $\sigma^2 > 0$ (bandwidth) controls decay speed
   - Requires infinite-dimensional feature map

4. **Sobolev Kernel**:

   - Take $X = [0,1]$
   - $k(x,x') = \min(x,x')$
   - This is the covariance function of Brownian motion

5. **Jaccard Similarity Kernel**:
   - $X$ is set of all subsets of $\{1,...,p\}$
   - For $x,x' \in X$ with $x \cup x' \neq \emptyset$:
     $$k(x,x') = \frac{|x \cap x'|}{|x \cup x'|}$$
   - If $x \cup x' = \emptyset$, then $k(x,x') = 1$

## 3. Reproducing Kernel Hilbert Spaces (RKHS)

### 3.1 Fundamental Theorem

**Theorem 5**: For every kernel $k$, there exists a feature map $\phi$ taking values in some inner product space $H$ such that:
$$k(x,x') = \langle \phi(x), \phi(x') \rangle$$

**Proof Sketch**:

1. Take $H$ as vector space of functions: $f(\cdot) = \sum_{i=1}^n \alpha_i k(\cdot,x_i)$
2. Define feature map $\phi(x) = k(\cdot,x)$
3. Define inner product: $\langle f,g \rangle = \sum_{i=1}^n \sum_{j=1}^m \alpha_i\beta_j k(x_i,x'_j)$
4. Show well-definedness and positive-definiteness

### 3.2 RKHS Definition and Properties

**Definition 2**: A Hilbert space $H$ of functions $f: X \to \mathbb{R}$ is a RKHS if for all $x \in X$, there exists $k_x \in H$ such that:
$$f(x) = \langle k_x,f \rangle \text{ for all } f \in H$$

The reproducing kernel is:
$$k: X \times X \to \mathbb{R}, \quad (x,x') \mapsto \langle k_x,k_{x'} \rangle = k_{x'}(x)$$

### 3.3 Examples of RKHS

1. **Linear Kernel**:

   - $H = \{f: f(x) = \beta^T x, \beta \in \mathbb{R}^p\}$
   - For $f(x) = \beta^T x$: $\|f\|^2_H = \|\beta\|^2_2$

2. **Sobolev Kernel**:
   - $H$ contains continuous functions $f: [0,1] \to \mathbb{R}$
   - Requirements:
     - $f(0) = 0$
     - Differentiable almost everywhere
     - $\int_0^1 f'(x)^2 dx < \infty$
   - Includes Lipschitz functions that are 0 at origin
   - Norm: $\|f\|_H = (\int_0^1 f'(x)^2 dx)^{1/2}$

## 4. The Representer Theorem

The Representer Theorem is a fundamental result in kernel methods that dramatically simplifies optimization problems in RKHS. It shows that despite working in potentially infinite-dimensional spaces, optimal solutions can be expressed as finite combinations of kernel functions.

### 4.1 Main Result and Intuition

**Theorem 6** (Kimeldorf-Wahba, Schölkopf et al.):
For arbitrary loss function $c: \mathbb{R}^n \times X^n \times \mathbb{R}^n \to \mathbb{R}$ and strictly increasing $J: [0,\infty) \to \mathbb{R}$, the minimizer of:
$Q_1(f) = c(Y,x_1,...,x_n,f(x_1),...,f(x_n)) + J(\|f\|^2_H)$
takes the form:
$\hat{f}(\cdot) = \sum_{i=1}^n \hat{\alpha}_i k(\cdot,x_i)$

#### Key Insights:

1. **Dimensionality Reduction**:

   - Though $H$ might be infinite-dimensional, the optimal solution lies in an $n$-dimensional subspace
   - This subspace is spanned by the kernel functions centered at training points
   - Instead of searching over all functions in $H$, we only need to find $n$ coefficients

2. **Regularization Understanding**:

   - The term $J(\|f\|^2_H)$ acts as regularization
   - It penalizes complex functions through the RKHS norm
   - The strictly increasing nature of $J$ ensures unique solutions

3. **Generality**:
   - Works for any loss function $c$
   - Applies to classification, regression, and other learning tasks
   - The result holds for any positive definite kernel

#### Proof Sketch and Intuition:

1. **Orthogonal Decomposition**:

   - Any function $f \in H$ can be written as $f = u + v$
   - $u$ lies in the span of kernel functions at training points
   - $v$ is orthogonal to all these kernel functions

2. **Key Observation**:
   - The value of $f$ at any training point depends only on $u$
   - The norm $\|f\|^2_H$ splits as $\|u\|^2_H + \|v\|^2_H$
   - Any non-zero $v$ increases the norm without improving the fit

### 4.2 Application to Ridge Regression

The theorem has particularly elegant implications for kernel ridge regression. Here we minimize:
$\|Y-K\alpha\|^2_2 + \lambda\alpha^T K\alpha$

#### Understanding the Optimization:

1. **Loss Term** $\|Y-K\alpha\|^2_2$:

   - Measures prediction error on training data
   - $K\alpha$ gives predictions at training points
   - Squared error loss in matrix form

2. **Regularization Term** $\lambda\alpha^T K\alpha$:

   - Controls complexity of solution
   - Equals $\lambda\|\hat{f}\|^2_H$ for $\hat{f}(\cdot) = \sum_i \alpha_i k(\cdot,x_i)$
   - $\lambda$ balances fit and smoothness

3. **Solution Form**:
   $K\hat{\alpha} = K(K + \lambda I)^{-1}Y$

   This has several interpretations:

   - Matrix regularization: adds $\lambda I$ to potentially ill-conditioned $K$
   - Spectral filtering: downweights contributions from small eigenvalues
   - Bayesian view: posterior mean under Gaussian process prior

### 4.3 Predictions and Computational Aspects

For a new observation $x$, predictions are made using:
$\hat{f}(x) = \sum_{i=1}^n \hat{\alpha}_i k(x,x_i)$

#### Implementation Insights:

1. **Computational Efficiency**:

   - Only need to store $n$ coefficients $\hat{\alpha}_i$
   - Prediction requires $n$ kernel evaluations
   - Can use efficient matrix operations for training

2. **Kernel Choice Effects**:

   - Different kernels lead to different function spaces
   - Kernel parameters affect smoothness of solutions
   - Can combine kernels for multiple feature types

3. **Practical Considerations**:
   - For large $n$, might need approximate methods
   - Can use subset of training points (sparse approximation)
   - Cross-validation helps choose $\lambda$ and kernel parameters

### 4.4 Extensions and Variations

The Representer Theorem has several important extensions:

1. **Semi-supervised Learning**:

   - Can include unlabeled data points
   - Modifies kernel to respect data manifold
   - Preserves finite representation

2. **Structured Output Spaces**:

   - Generalizes to vector-valued functions
   - Useful for multi-task learning
   - Maintains computational tractability

3. **Online Learning**:
   - Sequential updates possible
   - Maintains representer form
   - Efficient incremental algorithms

# Kernel Ridge Regression: Derivation and Intuition

Below is an explanation of the derivation and its intuition. We'll start by setting up the problem and then "unpack" each step, using simple language and examples along the way.

## 1. The Setup: Kernel Ridge Regression in a Nutshell

Imagine you have data points:

$$
y_i = f_0(x_i) + \varepsilon_i,\quad i=1,\dots,n
$$

where the noise $\varepsilon_i$ has mean zero and variance $\sigma^2$. We assume that the true function $f_0$ belongs to a reproducing kernel Hilbert space (RKHS) $\mathcal{H}$ with reproducing kernel $k$ and (by a scaling argument) that its RKHS norm is bounded by 1:

$$
\|f_0\|_{\mathcal{H}} \le 1
$$

In kernel ridge regression (KRR) we estimate $f_0$ by solving:

$$
\widehat{f}_\lambda = \arg\min_{f\in\mathcal{H}} \; \sum_{i=1}^{n} \bigl(y_i - f(x_i)\bigr)^2 + \lambda \|f\|_{\mathcal{H}}^2
$$

where $\lambda > 0$ is a regularization parameter. The extra term $\lambda\|f\|_{\mathcal{H}}^2$ helps control the complexity of the estimator. The famous Representer Theorem tells us that the solution can be written as:

$$
\widehat{f}_\lambda(x) = \sum_{i=1}^n \alpha_i\, k(x,x_i)
$$

and more specifically, if we form the kernel matrix:

$$
K_{ij} = k(x_i,x_j)
$$

then the vector of predictions on the training points is given by:

$$
\widehat{f}_\lambda(x_1),\dots,\widehat{f}_\lambda(x_n) = K(K+\lambda I)^{-1}Y
$$

where $Y=(y_1,\dots,y_n)^T$.

## 2. How Does the Error Decompose?

Our goal is to understand the **mean squared prediction error (MSPE)**:

$$
\frac{1}{n}\sum_{i=1}^{n} E\Bigl[\bigl(f_0(x_i)-\widehat{f}_\lambda(x_i)\bigr)^2\Bigr]
$$

It turns out that the answer "depends delicately on the eigenvalues of $K$". (Think of the eigenvalues as summarizing the "directions" in which the data are most or least variable as seen through the kernel.)

### Expressing $f_0$ in Terms of $K$

A key observation is that since $f_0 \in \mathcal{H}$, there exists a vector $\alpha\in\mathbb{R}^n$ such that:

$$
\bigl(f_0(x_1),\dots,f_0(x_n)\bigr)^T = K\alpha
$$

and one may show that:

$$
\|f_0\|^2_{\mathcal{H}} \ge \alpha^T K \alpha
$$

Since we assumed $\|f_0\|_{\mathcal{H}} \le 1$, this means:

$$
\alpha^T K \alpha \le 1
$$

### Working in the Eigenbasis

Let's perform an eigendecomposition of $K$. Write:

$$
K = U D U^T
$$

where $D$ is a diagonal matrix with eigenvalues $d_1 \ge d_2 \ge \cdots \ge d_n \ge 0$, and $U$ is an orthogonal matrix (its columns are the eigenvectors).

It is very convenient to "rotate" our coordinates by defining:

$$
\theta = U^T K \alpha
$$

In these new coordinates the vector $\theta$ summarizes how $f_0$ is "aligned" with the different eigen-directions of $K$.

## 3. The Two Sources of Error: Bias and Variance

When you write the prediction error at the training points, you have two contributions:

- **Bias (approximation error):** This comes from the fact that even without noise, our regularization (the $\lambda$ term) makes us "shrink" the true signal.
- **Variance (noise error):** This is the error that comes from the noise $\varepsilon$ in the data.

A careful calculation shows that:

$$
n\,\text{MSPE} = E\Bigl\|K(K+\lambda I)^{-1}(K\alpha+\varepsilon) - K\alpha\Bigr\|^2
= \underbrace{\Bigl\|\Bigl\{ \frac{D}{D+\lambda I} - I \Bigr\}\theta\Bigr\|^2}_{\text{Bias}^2} \;+\; \underbrace{E\Bigl\|\frac{D}{D+\lambda I} U^T\varepsilon\Bigr\|^2}_{\text{Variance}}
$$

### (a) The Variance Term

For the variance we have:

$$
E\Bigl\|\frac{D}{D+\lambda I} U^T\varepsilon\Bigr\|^2
= \sigma^2 \sum_{i=1}^n \Bigl(\frac{d_i}{d_i+\lambda}\Bigr)^2
$$

**Intuition:** In each eigen-direction $i$, the factor $d_i/(d_i+\lambda)$ "shrinks" the noise. If $d_i$ is large compared to $\lambda$ (i.e., that direction is "important"), then little shrinkage occurs; if $d_i$ is small, then the noise is greatly dampened.

### (b) The Bias Term

The bias term comes out as:

$$
\Bigl\|\Bigl\{ \frac{D}{D+\lambda I} - I \Bigr\}\theta\Bigr\|^2
= \sum_{i=1}^n \Bigl(\frac{\lambda}{d_i+\lambda}\Bigr)^2\, \theta_i^2
$$

Notice that in each direction $i$, the bias is larger when $\lambda$ is large or when $d_i$ is small. Since we know (from our earlier constraint) that:

$$
\sum_{i:\,d_i>0}\theta_i^2 = \alpha^T K \alpha \le 1
$$

a further argument shows that the whole bias term can be bounded by:

$$
\text{Bias}^2 \le \frac{\lambda}{4}
$$

This step says that the overall contribution from "overshrinking" our true function cannot be too large if we keep $\|f_0\|_{\mathcal{H}} \le 1$.

### Combining the Two

Putting the two parts together and dividing by $n$ gives the bound:

$$
\frac{1}{n}\,E\Bigl[\sum_{i=1}^{n}\bigl(f_0(x_i)-\widehat{f}_\lambda(x_i)\bigr)^2\Bigr]
\;\le\; \frac{\sigma^2}{n}\sum_{i=1}^{n}\Bigl(\frac{d_i}{d_i+\lambda}\Bigr)^2 \;+\; \frac{\lambda}{4n}
$$

In words, the prediction error is the sum (over eigen-directions) of the variance contribution (scaled by the shrinkage factor) plus a bias term that is proportional to $\lambda$.

## 4. Reparameterizing and Seeing the Trade‐Off

It is often useful to define the scaled eigenvalues:

$$
\widehat{\mu}_i = \frac{d_i}{n}
$$

and also to set:

$$
\gamma = \frac{\lambda}{n}
$$

Then the bound can be rewritten as:

$$
\frac{1}{n}E\Bigl[\sum_{i=1}^{n}\bigl(f_0(x_i)-\widehat{f}_{\lambda}(x_i)\bigr)^2\Bigr]
\;\le\; \frac{\sigma^2}{\gamma n} \sum_{i=1}^n \min\Bigl(\frac{\widehat{\mu}_i}{4},\,\gamma\Bigr) + \gamma
$$

**What does this mean?**

- The term $\min(\widehat{\mu}_i/4,\gamma)$ shows that in directions where the (scaled) eigenvalue is small (less than about $4\gamma$), the error contribution is essentially proportional to $\widehat{\mu}_i$; whereas for larger eigenvalues, the error is capped by $\gamma$.
- The overall error is a sum of a variance-like term (which decreases as $\gamma$ increases) and a bias term (which increases with $\gamma$). Hence, $\gamma$ (or equivalently $\lambda$) must be chosen to balance these two effects.

## 5. Connecting with Mercer's Theorem

Mercer's theorem tells us that under mild conditions the kernel $k$ has an expansion:

$$
k(x,x') = \sum_{j=1}^{\infty} \mu_j\, e_j(x)e_j(x')
$$

with eigenvalues $\mu_j$ (which decay as $j$ increases) and orthonormal eigenfunctions $e_j$. These $\mu_j$ are the infinite-dimensional analogues of the eigenvalues $d_i$ of the finite matrix $K$. One can show that:

$$
E\Biggl[\frac{1}{n}\sum_{i=1}^n \min\Bigl(\frac{\widehat{\mu}_i}{4},\gamma\Bigr)\Biggr] \;\le\; \frac{1}{n}\sum_{j=1}^\infty \min\Bigl(\frac{\mu_j}{4},\gamma\Bigr)
$$

This connects the performance of kernel ridge regression (which is based on the data through $K$) to intrinsic properties of the kernel $k$.

## 6. A Result on Rates: Theorem 8

Using the above ideas, one can prove that there exists a choice $\gamma_n$ (or $\lambda_n$) so that:

$$
\frac{1}{n}E\Bigl[\sum_{i=1}^n\bigl(f_0(x_i)-\widehat{f}_{\gamma_n}(x_i)\bigr)^2\Bigr] = o(n^{-1/2})
$$

That is, the MSPE decays faster than $n^{-1/2}$ as the sample size $n$ increases. The proof involves defining a function:

$$
\phi(\gamma) = \sum_{j=1}^\infty \min(\mu_j, \gamma)
$$

(which is increasing and tends to zero as $\gamma\downarrow 0$) and then choosing:

$$
\gamma_n = n^{-1/2}\,\phi(n^{-1/2})
$$

A quick check shows that with this choice the bias and variance balance so that the overall error decays at the desired rate.

## 7. A Concrete Example: The Sobolev Kernel

Let's look at an example. Suppose we are using the **Sobolev kernel** on the interval $[0,1]$ with a uniform density. In this case one can show that the Mercer eigenvalues satisfy:

$$
\frac{\mu_j}{4} = \frac{1}{\pi^2(2j-1)^2}
$$

They decay like $1/j^2$. With some further calculations one finds that:

$$
\frac{1}{n}\sum_{j=1}^\infty \min\Bigl(\frac{\mu_j}{4},\gamma_n\Bigr)
= O\bigl(\sqrt{\gamma_n}\bigr)
$$

as $\gamma_n\to 0$. Balancing the bias (of order $\gamma_n$) and the variance (of order $\sqrt{\gamma_n}$), one can show that an optimal choice is $\gamma_n \sim (\sigma^2/n)^{2/3}$. In other words, for the Sobolev kernel the error rate is of order $(\sigma^2/n)^{2/3}$.

**What does this tell you?**  
The rate $n^{-2/3}$ (ignoring constants and $\sigma^2$) is slower than the parametric $n^{-1}$ rate, which is typical in nonparametric settings. It reflects the fact that with smoothness assumptions and infinite-dimensional function spaces, there is an unavoidable trade-off between bias and variance.

## 8. Summary and Key Intuitions

1. **Kernel Ridge Regression Framework:**  
   We solve a regularized least-squares problem in an RKHS. The regularization controls the trade-off between fitting the data and ensuring smoothness.

2. **Bias–Variance Trade-Off in the Eigenbasis:**  
   Writing the solution in the eigenbasis of the kernel matrix, each eigen-direction is shrunk by a factor $d_i/(d_i+\lambda)$.

   - **Variance:** Noise is reduced by these factors.
   - **Bias:** Regularization introduces bias by "overshrinking" components of $f_0$.

3. **Role of the Eigenvalues:**  
   The eigenvalues $d_i$ (or their normalized versions $\widehat{\mu}_i$) determine how much each direction contributes to the error. Directions with very small eigenvalues (typically corresponding to high-frequency components) are heavily regularized.

4. **Mercer's Theorem Connection:**  
   By expressing the kernel in its Mercer expansion, one connects the finite-sample behavior to the intrinsic complexity of the kernel, as captured by the eigenvalues $\mu_j$.

5. **Choosing the Regularization Parameter:**  
   An optimal balance between bias and variance is achieved by choosing $\lambda$ (or equivalently $\gamma$) appropriately. In the Sobolev kernel example, this balance leads to a rate of $(\sigma^2/n)^{2/3}$.

## Final Words

This derivation shows that the predictive performance of kernel ridge regression is intimately connected with the spectrum (the eigenvalues) of the kernel matrix. By decomposing the error into bias and variance components (each "filtered" by the eigenvalues), we gain a clear picture of how regularization works: it suppresses noise in weak directions (small $d_i$) at the cost of introducing some bias, while leaving strong directions (large $d_i$) relatively untouched. Through this careful balancing act—and by linking finite-sample properties with the Mercer expansion—we can derive precise rates of convergence for the estimator.

# Key Takeaways

1. **Eigenvalues Matter:** The decay rate of kernel eigenvalues ($\mu_j$) determines the **statistical complexity** of the RKHS.

   ° Faster decay (e.g., Sobolev) → Lower effective dimension → Better error rates.

   ° Slower decay (e.g., RBF) → Higher complexity → Requires more data.

2. **Regularization Trade-off:**

   ° Small λ: Low bias, high variance (overfitting).

   ° Large λ: High bias, low variance (underfitting).

3. **Optimal Rates:** For Sobolev-like kernels, KRR achieves MSPE ~ $O(n^{-2/3})$, faster than $O(n^{-1/2})$.

<img src="Code/Figures/kernels.png" alt="alt text">
