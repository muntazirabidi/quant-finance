# The Markov Property and n-step Transitions:

## 1. The Markov Property: Formal Definition and Intuition

### Mathematical Definition

Let $(X_n)_{n\geq 0}$ be a sequence of random variables. The Markov property states that for any sequence of states $(A_0, ..., A_{n+m})$:

$$P(X_{n+1} \in A_{n+1}, ..., X_{n+m} \in A_{n+m} | X_0 \in A_0, ..., X_{n-1} \in A_{n-1}, X_n = i)$$
$$ = P(X*{n+1} \in A*{n+1}, ..., X*{n+m} \in A*{n+m} | X*n = i)$$
$$ = P(X_1 \in A*{n+1}, ..., X*m \in A*{n+m} | X_0 = i)$$

### Deep Intuition

Think of the Markov property as a kind of "memory reset". When you know the current state:

1. The future is independent of the past
2. Only the present state matters for predicting what happens next
3. The process "forgets" how it got to its current state

### Key Notation

For clarity, we use:

- $P_i$ denotes probability conditioned on $X_0 = i$
- $E_i$ denotes expectation conditioned on $X_0 = i$

## 2. N-Step Transition Probabilities

### Definition

The n-step transition probability $p_{ij}^{(n)}$ is:
$$p_{ij}^{(n)} = P(X_{k+n} = j | X_k = i)$$

This represents the probability of moving from state $i$ to state $j$ in exactly $n$ steps.

### The Chapman-Kolmogorov Equations

One of the most important theorems about n-step transitions:

1. **First Form**:
   $$p_{ik}^{(n+m)} = \sum_{j\in I} p_{ij}^{(n)}p_{jk}^{(m)}$$

2. **Matrix Form**:
   $$p_{ij}^{(n)} = (P^n)_{i,j}$$

### Intuitive Understanding

- Think of $p_{ij}^{(n)}$ as "all possible ways to get from $i$ to $j$ in $n$ steps"
- The Chapman-Kolmogorov equations break a long journey into two shorter ones
- Matrix multiplication $P^n$ automatically counts all possible paths

## 3. Worked Example: Two-State Chain

Consider a two-state Markov chain with transition matrix:
$$P = \begin{pmatrix} 1-\alpha & \alpha \\ \beta & 1-\beta \end{pmatrix}$$

### Finding $p_{11}^{(n)}$ Two Ways:

#### Method 1: Eigenvalue Decomposition

1. Find eigenvalues: 1 and $1-\alpha-\beta$
2. Diagonalize: $P = UDU^{-1}$
3. Result:
   $$p_{11}^{(n)} = \frac{\beta}{\alpha + \beta} + \frac{\alpha}{\alpha + \beta}(1-\alpha-\beta)^n$$

#### Method 2: Recurrence Relation

1. Condition on state at time $n-1$:
   $$p_{11}^{(n)} = p_{11}^{(n-1)}(1-\alpha) + p_{12}^{(n-1)}\beta$$
2. Solve the recurrence to get same result

## 4. Code Implementation

```python
import numpy as np

def n_step_transition(P, n):
    """
    Calculate n-step transition probabilities

    Args:
    P: transition matrix
    n: number of steps

    Returns:
    P^n: n-step transition matrix
    """
    return np.linalg.matrix_power(P, n)

# Example usage
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])
n = 3

P_n = n_step_transition(P, n)
print(f"3-step transition probabilities:\n{P_n}")
```

## 5. Important Properties and Implications

1. **Time Reversibility**:

   - Forward and backward probabilities may be different
   - Some chains have special reversibility properties

2. **Long-term Behavior**:

   - $P^n$ often converges as $n \to \infty$
   - Limit depends on chain properties (irreducibility, periodicity)

3. **Path Counting**:
   - $(P^n)_{ij}$ also counts weighted paths of length $n$ from $i$ to $j$
   - Each path weighted by product of transition probabilities

## 6. Common Interview Questions

1. **Q**: What's the difference between 2-step and squared transition probabilities?
   **A**: They're the same! $p_{ij}^{(2)} = (P^2)_{ij}$ by Chapman-Kolmogorov

2. **Q**: Why do we care about n-step transitions?
   **A**: They help predict long-term behavior and analyze system evolution

3. **Q**: How would you efficiently compute $P^{100}$?
   **A**: Use diagonalization if possible, or binary exponentiation for numerical computation
