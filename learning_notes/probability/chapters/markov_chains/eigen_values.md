# Eigenvalues in Markov Chains:

## The Fundamental Role of Eigenvalues

Eigenvalues tell us two crucial things about a Markov chain:

1. The long-term behavior (stationary distribution)
2. How quickly the chain converges to this behavior

For any Markov chain transition matrix P:

- The largest eigenvalue is always 1
- All other eigenvalues have absolute value less than 1
- The convergence rate is determined by the second-largest eigenvalue in absolute value

Let's explore this with a 3-state example:

$P = \begin{bmatrix} 
0.2 & 0.3 & 0.5 \\
0.4 & 0.3 & 0.3 \\
0.1 & 0.4 & 0.5
\end{bmatrix}$

### Step 1: Finding Eigenvalues

For a 3×3 matrix, we solve:
$\det(P - \lambda I) = 0$

This gives us a cubic equation:
$-\lambda^3 + (1 + r + s)\lambda^2 + t\lambda + d = 0$

where r, s, t, d are expressions involving the matrix entries.

For our example matrix:
$-\lambda^3 + \lambda^2 - 0.15\lambda + 0.014 = 0$

The solutions are:

- $\lambda_1 = 1$
- $\lambda_2 ≈ 0.2$
- $\lambda_3 ≈ -0.2$

### Step 2: Understanding the Eigenvalues

The eigenvalue 1 corresponds to the stationary distribution. The other eigenvalues determine how quickly different components of the distribution converge:

$p^{(n)} = \pi + c_2\lambda_2^nv_2 + c_3\lambda_3^nv_3$

where:

- $p^{(n)}$ is the distribution after n steps
- $\pi$ is the stationary distribution
- $v_2, v_3$ are eigenvectors
- $c_2, c_3$ are constants determined by initial conditions

### Step 3: Convergence Analysis

The term with the largest |λᵢ| (excluding λ₁=1) dominates the convergence rate. In our example:

- |λ₂| = |λ₃| = 0.2
- After n steps, the distance from stationary is roughly proportional to (0.2)ⁿ
- This means each step reduces the "error" by about 80%

## Key Insights About Eigenvalues in Markov Chains

1. **Number of Eigenvalues**

   - A k-state chain has k eigenvalues
   - More states generally means more complex behavior

2. **Eigenvalue Properties**

   - All eigenvalues lie in [-1, 1]
   - If chain is reversible, all eigenvalues are real
   - Periodicity shows up as eigenvalues on the unit circle

3. **Practical Applications**
   For example, in our 3-state chain:
   - Mixing time ≈ log(1/ε)/log(1/0.2)
   - To get within ε of stationary
   - This helps in MCMC algorithms

Let me explain how to predict a Markov chain's behavior at any time n using eigenvalue decomposition, starting with a clear and intuitive approach.

# Predicting Markov Chain Behavior Using Eigendecomposition

Let's use our 3-state matrix:

$P = \begin{bmatrix} 
0.2 & 0.3 & 0.5 \\
0.4 & 0.3 & 0.3 \\
0.1 & 0.4 & 0.5
\end{bmatrix}$

## Step 1: Set Up the Eigendecomposition

The key idea is that we can write any initial distribution as a combination of eigenvectors:

$p^{(0)} = c_1v_1 + c_2v_2 + c_3v_3$

where $v_1, v_2, v_3$ are the eigenvectors corresponding to eigenvalues $\lambda_1 = 1, \lambda_2 = 0.2, \lambda_3 = -0.2$

## Step 2: Calculate Evolution Over Time

After n steps, each component gets multiplied by its eigenvalue n times:

$p^{(n)} = c_1v_1(1)^n + c_2v_2(0.2)^n + c_3v_3(-0.2)^n$

Let's work through a concrete example.

Suppose we start in state 1, so $p^{(0)} = [1, 0, 0]$

First, we need to find the eigenvectors:
$v_1 = [0.25, 0.35, 0.40]$ (stationary distribution)
$v_2 = [1, -0.5, -0.5]$
$v_3 = [0, 1, -1]$

## Step 3: Find the Coefficients

We solve:
$[1, 0, 0] = c_1v_1 + c_2v_2 + c_3v_3$

This gives us:
$c_1 = 0.25$
$c_2 = 0.75$
$c_3 = -0.35$

## Step 4: Calculate Distribution at Time n

Now we can write a formula for any time n:

$p^{(n)} = 0.25[0.25, 0.35, 0.40] + 0.75[1, -0.5, -0.5](0.2)^n + (-0.35)[0, 1, -1](-0.2)^n$

For example, at n = 5:

- $(0.2)^5 = 0.00032$
- $(-0.2)^5 = -0.00032$

Plugging in:
$p^{(5)} ≈ [0.25, 0.35, 0.40]$

## Understanding the Components

1. **Steady State Component** ($c_1v_1$):

   - Never changes because $1^n = 1$
   - Represents the long-term behavior

2. **First Transient Component** ($c_2v_2(0.2)^n$):

   - Decays exponentially with rate 0.2
   - Major influence in early steps

3. **Second Transient Component** ($c_3v_3(-0.2)^n$):
   - Creates oscillations that decay
   - Sign alternates due to negative eigenvalue

## Practical Application

To find the probability of being in each state after n steps:

1. Write your initial distribution
2. Decompose it into eigenvector components
3. Apply the time evolution formula
4. Sum the components

This method is particularly useful because:

- It gives exact probabilities for any time n
- Shows how quickly convergence happens
- Explains oscillatory behavior if present
