# Matrix Decomposition Methods: QR, LU, and Cholesky

## Introduction

Matrix decompositions (also called matrix factorizations) express a matrix as a product of simpler matrices. They are fundamental tools in numerical linear algebra, providing efficient solutions to many computational problems including:

- Solving systems of linear equations
- Computing determinants and inverses
- Finding eigenvalues and eigenvectors
- Least squares problems
- Data compression and dimensionality reduction

This document provides a comprehensive explanation of three critical matrix decomposition methods: LU, Cholesky, and QR decomposition.

## 1. LU Decomposition

LU decomposition factors a matrix $A$ into the product of a lower triangular matrix $L$ and an upper triangular matrix $U$:

$$A = LU$$

### 1.1 Mathematical Formulation

For an $n \times n$ matrix $A$, we seek matrices $L$ and $U$ such that:

- $L$ is lower triangular (all elements above the main diagonal are zero)
- $U$ is upper triangular (all elements below the main diagonal are zero)
- Typically, we set the diagonal elements of $L$ to 1 (called "unit lower triangular")

The LU decomposition can be formally written as:

$$A = LU = 
\begin{bmatrix} 
l_{11} & 0 & \cdots & 0 \\
l_{21} & l_{22} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
l_{n1} & l_{n2} & \cdots & l_{nn}
\end{bmatrix}
\begin{bmatrix} 
u_{11} & u_{12} & \cdots & u_{1n} \\
0 & u_{22} & \cdots & u_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & u_{nn}
\end{bmatrix}$$

### 1.2 Existence and Uniqueness

LU decomposition without pivoting exists and is unique if all leading principal minors of $A$ are non-zero. More practically, this means all steps of Gaussian elimination can be performed without row exchanges.

When the matrix $A$ doesn't satisfy this condition, we use a permutation matrix $P$ to rearrange rows:

$$PA = LU$$

This is called "LU decomposition with partial pivoting" and exists for any non-singular matrix $A$.

### 1.3 Algorithm

The LU decomposition algorithm essentially follows the steps of Gaussian elimination:

1. Eliminate elements below the diagonal in column 1
2. Eliminate elements below the diagonal in column 2
3. Continue until the matrix is upper triangular

As we perform eliminations, we store the multipliers (the factors used to eliminate elements) in the $L$ matrix.

For a $3 \times 3$ matrix $A$, the procedure gives us:

$$A = \begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}$$

First, eliminate elements in the first column:
- Compute multiplier $m_{21} = a_{21}/a_{11}$ and subtract $m_{21}$ times row 1 from row 2
- Compute multiplier $m_{31} = a_{31}/a_{11}$ and subtract $m_{31}$ times row 1 from row 3

This gives:
$$\begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\
0 & a_{22} - m_{21}a_{12} & a_{23} - m_{21}a_{13} \\
0 & a_{32} - m_{31}a_{12} & a_{33} - m_{31}a_{13}
\end{bmatrix}$$

Continue to the second column and so on. The multipliers $m_{ij}$ become the elements of $L$.

### 1.4 Computational Complexity

LU decomposition has a computational complexity of $O(n^3)$, specifically requiring approximately $\frac{2n^3}{3}$ floating-point operations for an $n \times n$ matrix.

### 1.5 Applications

The primary application of LU decomposition is solving linear systems of equations $Ax = b$:

1. Decompose $A = LU$
2. Solve $Ly = b$ for $y$ using forward substitution
3. Solve $Ux = y$ for $x$ using backward substitution

This is especially efficient when solving multiple systems with the same coefficient matrix but different right-hand sides.

Other applications include:
- Computing the determinant: $\det(A) = \det(L) \cdot \det(U) = \prod_{i=1}^{n} u_{ii}$
- Computing the inverse of $A$
- Finding eigenvalues through iterative methods

### 1.6 Example

Consider the matrix:
$$A = \begin{bmatrix} 
4 & 3 \\
6 & 3
\end{bmatrix}$$

Step 1: Compute the multiplier for eliminating the element in position (2,1):
$m_{21} = \frac{a_{21}}{a_{11}} = \frac{6}{4} = 1.5$

Step 2: Subtract $m_{21}$ times row 1 from row 2:
$$\begin{bmatrix} 
4 & 3 \\
0 & 3 - 1.5 \cdot 3 = -1.5
\end{bmatrix}$$

Step 3: The LU decomposition is:
$$L = \begin{bmatrix} 
1 & 0 \\
1.5 & 1
\end{bmatrix}, 
U = \begin{bmatrix} 
4 & 3 \\
0 & -1.5
\end{bmatrix}$$

Verification:
$$LU = \begin{bmatrix} 
1 & 0 \\
1.5 & 1
\end{bmatrix}
\begin{bmatrix} 
4 & 3 \\
0 & -1.5
\end{bmatrix} = 
\begin{bmatrix} 
4 & 3 \\
6 & 3
\end{bmatrix} = A$$

## 2. Cholesky Decomposition

Cholesky decomposition is a special case of LU decomposition applicable only to symmetric positive definite matrices. It factors a matrix $A$ as:

$$A = LL^T$$

where $L$ is a lower triangular matrix and $L^T$ is its transpose.

### 2.1 Mathematical Formulation

For a symmetric positive definite matrix $A$ (a matrix where $A = A^T$ and $x^TAx > 0$ for all non-zero vectors $x$), the Cholesky decomposition expresses $A$ as:

$$A = LL^T = 
\begin{bmatrix} 
l_{11} & 0 & \cdots & 0 \\
l_{21} & l_{22} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
l_{n1} & l_{n2} & \cdots & l_{nn}
\end{bmatrix}
\begin{bmatrix} 
l_{11} & l_{21} & \cdots & l_{n1} \\
0 & l_{22} & \cdots & l_{n2} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & l_{nn}
\end{bmatrix}$$

### 2.2 Existence and Uniqueness

A real symmetric matrix $A$ has a Cholesky decomposition if and only if it is positive definite. The decomposition is unique when we require the diagonal elements of $L$ to be positive.

### 2.3 Algorithm

The Cholesky algorithm computes the elements of $L$ using the following formulas:

For $i = 1, 2, \ldots, n$:

$$l_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} l_{ik}^2}$$

For $j = i+1, i+2, \ldots, n$:

$$l_{ji} = \frac{1}{l_{ii}} \left( a_{ji} - \sum_{k=1}^{i-1} l_{jk}l_{ik} \right)$$

### 2.4 Computational Complexity

Cholesky decomposition requires approximately $\frac{n^3}{3}$ floating-point operations for an $n \times n$ matrix, making it roughly twice as efficient as general LU decomposition.

### 2.5 Applications

Cholesky decomposition is widely used in:

- Efficiently solving symmetric positive definite linear systems
- Monte Carlo simulations (generating correlated random variables)
- Non-linear optimization (Newton's method and quasi-Newton methods)
- Least squares problems
- Kalman filtering in control theory and signal processing
- Computational statistics (especially for multivariate normal distributions)

### 2.6 Example

Consider the symmetric positive definite matrix:
$$A = \begin{bmatrix} 
4 & 6 \\
6 & 13
\end{bmatrix}$$

Step 1: Compute $l_{11}$:
$$l_{11} = \sqrt{a_{11}} = \sqrt{4} = 2$$

Step 2: Compute $l_{21}$:
$$l_{21} = \frac{a_{21}}{l_{11}} = \frac{6}{2} = 3$$

Step 3: Compute $l_{22}$:
$$l_{22} = \sqrt{a_{22} - l_{21}^2} = \sqrt{13 - 3^2} = \sqrt{4} = 2$$

The Cholesky decomposition is:
$$L = \begin{bmatrix} 
2 & 0 \\
3 & 2
\end{bmatrix}$$

Verification:
$$LL^T = \begin{bmatrix} 
2 & 0 \\
3 & 2
\end{bmatrix}
\begin{bmatrix} 
2 & 3 \\
0 & 2
\end{bmatrix} = 
\begin{bmatrix} 
4 & 6 \\
6 & 13
\end{bmatrix} = A$$

### 2.7 Variant: LDL^T Decomposition

A closely related factorization is the $LDL^T$ decomposition, where:

$$A = LDL^T$$

with $L$ being unit lower triangular and $D$ being diagonal. This avoids computing square roots and can be numerically more stable in some cases.

## 3. QR Decomposition

QR decomposition factors a matrix $A$ into the product of an orthogonal matrix $Q$ and an upper triangular matrix $R$:

$$A = QR$$

### 3.1 Mathematical Formulation

For an $m \times n$ matrix $A$ with $m \geq n$, the QR decomposition gives:

- $Q$ is an $m \times m$ orthogonal matrix ($Q^TQ = QQ^T = I$)
- $R$ is an $m \times n$ upper triangular matrix with zeros below the main diagonal

In full form:

$$A = QR = 
\begin{bmatrix} 
q_{11} & q_{12} & \cdots & q_{1m} \\
q_{21} & q_{22} & \cdots & q_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
q_{m1} & q_{m2} & \cdots & q_{mm}
\end{bmatrix}
\begin{bmatrix} 
r_{11} & r_{12} & \cdots & r_{1n} \\
0 & r_{22} & \cdots & r_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & r_{nn} \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots
\end{bmatrix}$$

Often, we also use the "economy" or "thin" QR decomposition where $Q$ is $m \times n$ and $R$ is $n \times n$, which is more computationally efficient when $m >> n$.

### 3.2 Existence and Uniqueness

QR decomposition exists for any matrix. It is unique (up to the signs of the rows of $R$) if $A$ has full column rank.

### 3.3 Algorithms

There are three main approaches to compute QR decomposition:

#### 3.3.1 Gram-Schmidt Orthogonalization

The classical Gram-Schmidt process:

1. Initialize $Q$ and $R$ as empty matrices
2. For each column $a_j$ of $A$:
   - Set $r_{ij} = q_i^T a_j$ for $i = 1, 2, \ldots, j-1$
   - Compute $\hat{q}_j = a_j - \sum_{i=1}^{j-1} r_{ij}q_i$
   - Set $r_{jj} = \|\hat{q}_j\|_2$
   - Set $q_j = \hat{q}_j / r_{jj}$

The modified Gram-Schmidt is numerically more stable and should be preferred in practice.

#### 3.3.2 Householder Reflections

This method uses Householder transformations to zero out elements below the diagonal one column at a time:

1. For each column $j$:
   - Construct a Householder matrix $H_j$ that zeros out all elements below the diagonal in column $j$
   - Update the remaining submatrix: $A \leftarrow H_j A$
   - Accumulate the reflections: $Q \leftarrow Q H_1 H_2 \cdots H_n$

#### 3.3.3 Givens Rotations

Givens rotations zero out elements one at a time:

1. For each element below the diagonal that needs to be zeroed:
   - Construct a Givens rotation matrix $G$ that zeros out that specific element
   - Apply it to the matrix: $A \leftarrow GA$
   - Accumulate the rotations to form $Q$

### 3.4 Computational Complexity

- Gram-Schmidt: $O(mn^2)$ operations
- Householder: $O(mn^2)$ operations but more numerically stable
- Givens: $O(mn^2)$ operations, useful for sparse matrices or parallel implementations

### 3.5 Applications

QR decomposition has numerous applications:

- Solving linear least squares problems: $\min_x \|Ax - b\|_2$
- Computing orthonormal bases for column spaces
- QR algorithm for eigenvalue computation
- Solving underdetermined and overdetermined linear systems
- Data fitting and regression analysis
- Signal processing and control theory

### 3.6 Example Using Gram-Schmidt

Consider the matrix:
$$A = \begin{bmatrix} 
3 & 5 \\
2 & 1
\end{bmatrix}$$

Step 1: Normalize the first column of $A$:
$$\|a_1\|_2 = \sqrt{3^2 + 2^2} = \sqrt{13}$$
$$q_1 = \frac{a_1}{\|a_1\|_2} = \frac{1}{\sqrt{13}} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} \frac{3}{\sqrt{13}} \\ \frac{2}{\sqrt{13}} \end{bmatrix}$$
$$r_{11} = \|a_1\|_2 = \sqrt{13}$$

Step 2: Project the second column onto $q_1$:
$$r_{12} = q_1^T a_2 = \frac{3}{\sqrt{13}} \cdot 5 + \frac{2}{\sqrt{13}} \cdot 1 = \frac{17}{\sqrt{13}}$$

Step 3: Compute the orthogonal component of $a_2$:
$$\hat{q}_2 = a_2 - r_{12}q_1 = \begin{bmatrix} 5 \\ 1 \end{bmatrix} - \frac{17}{\sqrt{13}} \begin{bmatrix} \frac{3}{\sqrt{13}} \\ \frac{2}{\sqrt{13}} \end{bmatrix} = \begin{bmatrix} 5 - \frac{51}{13} \\ 1 - \frac{34}{13} \end{bmatrix} = \begin{bmatrix} \frac{14}{13} \\ -\frac{21}{13} \end{bmatrix}$$

Step 4: Normalize $\hat{q}_2$:
$$\|\hat{q}_2\|_2 = \sqrt{\left(\frac{14}{13}\right)^2 + \left(-\frac{21}{13}\right)^2} = \frac{\sqrt{637}}{13}$$
$$q_2 = \frac{\hat{q}_2}{\|\hat{q}_2\|_2} = \frac{13}{\sqrt{637}} \begin{bmatrix} \frac{14}{13} \\ -\frac{21}{13} \end{bmatrix} = \begin{bmatrix} \frac{14}{\sqrt{637}} \\ -\frac{21}{\sqrt{637}} \end{bmatrix}$$
$$r_{22} = \|\hat{q}_2\|_2 = \frac{\sqrt{637}}{13}$$

Step 5: The QR decomposition is:
$$Q = \begin{bmatrix} \frac{3}{\sqrt{13}} & \frac{14}{\sqrt{637}} \\ \frac{2}{\sqrt{13}} & -\frac{21}{\sqrt{637}} \end{bmatrix}, 
R = \begin{bmatrix} \sqrt{13} & \frac{17}{\sqrt{13}} \\ 0 & \frac{\sqrt{637}}{13} \end{bmatrix}$$

### 3.7 QR with Householder Reflections (Outline)

For a matrix $A$, Householder reflections compute QR as follows:

1. For column $j = 1, 2, \ldots, n$:
   - Construct a Householder reflection that transforms the subvector $A(j:m,j)$ into $[\|A(j:m,j)\|_2, 0, \ldots, 0]^T$
   - Apply this reflection to the remaining columns
   - Accumulate the reflections to form $Q$

The Householder matrix for a vector $x$ is given by:
$$H = I - 2\frac{uu^T}{u^Tu}$$
where $u = x - \|x\|_2 e_1$ and $e_1$ is the first standard basis vector.

## 4. Comparison of Decompositions

| Aspect | LU Decomposition | Cholesky Decomposition | QR Decomposition |
|--------|------------------|------------------------|------------------|
| Form | $A = LU$ | $A = LL^T$ | $A = QR$ |
| Applicable matrices | Any square matrix (with pivoting) | Symmetric positive definite | Any matrix |
| Uniqueness | Unique with constraints | Unique with positive diagonal | Unique up to column signs |
| Computational cost | $\sim \frac{2n^3}{3}$ | $\sim \frac{n^3}{3}$ | $\sim 2mn^2$ |
| Numerical stability | Less stable (needs pivoting) | Very stable | Very stable |
| Main applications | Linear systems, inverses | SPD systems, Monte Carlo | Least squares, orthogonalization |
| Special properties | Preserves sparsity | Exploits symmetry | Preserves orthogonality |

## 5. Relationship with Eigenvalues

### 5.1 LU and Eigenvalues

While LU decomposition does not directly compute eigenvalues, it is used in algorithms for eigenvalue computations, such as:

- Determinant calculation: $\det(A) = \prod_{i=1}^{n} u_{ii}$
- Iterative eigenvalue methods that involve solving linear systems

### 5.2 Cholesky and Eigenvalues

For a symmetric positive definite matrix $A$ with eigendecomposition $A = Q\Lambda Q^T$:

- The Cholesky factor $L$ can be related to eigenvalues through $L = Q\Lambda^{1/2}P$ for some permutation $P$
- All eigenvalues of $A$ are positive, which ensures the existence of the Cholesky decomposition
- The condition number of $A$ is the square of the condition number of $L$

### 5.3 QR and Eigenvalues

QR decomposition is fundamental to the QR algorithm for computing eigenvalues:

1. Start with matrix $A_0 = A$
2. For $k = 0, 1, 2, \ldots$ until convergence:
   - Compute QR factorization: $A_k = Q_k R_k$
   - Form $A_{k+1} = R_k Q_k$

As $k$ increases, $A_k$ converges to a Schur form (upper triangular with eigenvalues on the diagonal).

Variants of the QR algorithm (with shifts) are among the most powerful and widely used methods for computing eigenvalues of general matrices.

## 6. Practical Considerations

### 6.1 Numerical Stability

- LU decomposition: Requires pivoting for stability
- Cholesky decomposition: Inherently stable for well-conditioned SPD matrices
- QR decomposition: Householder and Givens methods are very stable

### 6.2 Storage Requirements

- LU: $\sim n^2$ elements (can store L and U in the space of A)
- Cholesky: $\sim \frac{n^2}{2}$ elements (only need to store L)
- QR: Full version requires $\sim m^2$ elements, thin version $\sim mn$

### 6.3 Implementation Considerations

- For sparse matrices, specialized algorithms preserve sparsity patterns
- For very large matrices, blocked algorithms improve cache efficiency
- Parallel implementations differ in communication patterns and load balancing

## 7. Software Implementations

Modern numerical libraries provide efficient implementations of these decompositions:

- LAPACK: Dense matrix routines (dgetrf, dpotrf, dgeqrf)
- BLAS: Optimized matrix-vector operations
- SciPy/NumPy: High-level Python interfaces
- Eigen: C++ template library
- MATLAB/Julia: High-level interfaces and visualizations

## 8. Advanced Topics

### 8.1 Rank-Revealing Decompositions

Variants of LU and QR that expose the numerical rank of a matrix are important for rank-deficient or nearly rank-deficient problems.

### 8.2 Updating and Downdating

Techniques exist to efficiently update these decompositions when the original matrix changes by a low-rank modification.

### 8.3 Banded and Sparse Matrices

Special algorithms exploit band structure or sparsity patterns to greatly reduce computational complexity.

## 9. Conclusion

Matrix decompositions are foundational tools in numerical linear algebra. The choice between LU, Cholesky, and QR depends on:

- The structure of the matrix (symmetric, positive definite, etc.)
- The computational task (solving linear systems, least squares, eigenvalues)
- Numerical considerations (condition number, required accuracy)

Understanding these decompositions and their properties enables efficient solutions to a wide range of computational problems across science, engineering, and data analysis.

## 10. References

1. Golub, G. H., & Van Loan, C. F. (2013). Matrix Computations (4th ed.). Johns Hopkins University Press.
2. Trefethen, L. N., & Bau, D. (1997). Numerical Linear Algebra. SIAM.
3. Demmel, J. W. (1997). Applied Numerical Linear Algebra. SIAM.
4. Horn, R. A., & Johnson, C. R. (2012). Matrix Analysis (2nd ed.). Cambridge University Press.