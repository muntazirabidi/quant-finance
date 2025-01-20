# Chapter 6: Markov Chains - Stationary Distributions and Convergence to Equilibrium

## 6.1 Stationary Distributions

### Definition

Let $\pi = (\pi_i, i \in I)$ be a distribution on state space $I$. We say $\pi$ is a **stationary distribution** if starting the Markov chain from $X_0$ with distribution $\pi$ implies $X_n$ has distribution $\pi$ for all $n \geq 0$.

### Key Properties

1. If $\lambda$ is the initial distribution, then:

   - Distribution of $X_1$ is $\lambda P$
   - Distribution of $X_n$ is $\lambda P^n$

2. $\pi$ is stationary if and only if:
   $\pi P = \pi$ or equivalently $\pi_j = \sum_i \pi_i p_{ij}$ for all $j$

## 6.2 Main Convergence Theorems

### Theorem 6.3 (Existence and Uniqueness)

For an irreducible transition matrix $P$:

1. $P$ has a stationary distribution if and only if $P$ is positive recurrent
2. If it exists, the stationary distribution $\pi$ is unique with $\pi_i = 1/m_i$ where $m_i$ is the mean return time

### Theorem 6.4 (Convergence to Equilibrium)

If $P$ is irreducible and aperiodic with stationary distribution $\pi$, then for any initial distribution:

- $P(X_n = j) \to \pi_j$ as $n \to \infty$ for all $j$
- $p_{ij}^{(n)} \to \pi_j$ as $n \to \infty$ for all $i,j$

### Theorem 6.5 (Ergodic Theorem)

For irreducible $P$, let $V_i(n)$ be the number of visits to state $i$ before time $n$:
$$V_i(n) = \sum_{r=0}^{n-1} 1\{X_r = i\}$$

Then for any initial distribution:
$$\frac{V_i(n)}{n} \to \frac{1}{m_i} \text{ almost surely as } n \to \infty$$

## 6.3 Examples

### Two-State Chain

For $P = \begin{pmatrix} 1-\alpha & \alpha \\ \beta & 1-\beta \end{pmatrix}$:

- Stationary distribution: $\pi = (\frac{\beta}{\alpha+\beta}, \frac{\alpha}{\alpha+\beta})$

### Random Walk on Graph

For a graph with vertex degrees $d_i$:

- Stationary distribution: $\pi_i = \frac{d_i}{\sum_j d_j}$

### One-Dimensional Random Walk

For $p < q$:

- Stationary distribution: $\pi_i = (1-\frac{p}{q})(\frac{p}{q})^i$

## Key Insights

1. Irreducibility and aperiodicity are crucial for convergence to equilibrium

2. The stationary distribution represents both:

   - Long-term probabilities of being in each state
   - Inverse of mean return times

3. The ergodic theorem connects:

   - Time averages ($V_i(n)/n$)
   - Space averages ($\pi_i$)

4. For infinite chains:
   - Transient chains have no stationary distribution
   - Null recurrent chains have no stationary distribution
   - Only positive recurrent chains have a stationary distribution
