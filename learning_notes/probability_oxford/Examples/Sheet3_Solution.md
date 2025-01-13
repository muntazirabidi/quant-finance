# Question 1: Markov Chain Communicating Classes

Find the communicating classes of Markov chains with the following transition matrices on the state space $\{1,2,3,4,5\}$, and in each case determine which classes are closed:

(i)

$$
P_1 = \begin{pmatrix}
\frac{1}{2} & 0 & 0 & 0 & \frac{1}{2} \\
0 & \frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} \\
\frac{1}{2} & 0 & 0 & 0 & \frac{1}{2}
\end{pmatrix}
$$

(ii)

$$
P_2 = \begin{pmatrix}
\frac{1}{4} & 0 & \frac{3}{4} & 0 & 0 \\
0 & \frac{1}{3} & 0 & \frac{2}{3} & 0 \\
0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{6} & 0 & \frac{1}{3} & 0 \\
\frac{1}{4} & 0 & \frac{1}{2} & 0 & \frac{1}{4}
\end{pmatrix}
$$

For each matrix:

1. Draw the transition diagram
2. Identify all communicating classes
3. Determine which classes are closed

If $X$ is a chain with the transition matrix in (ii), find the distribution of $X_1$ when $X_0$ has the uniform distribution on $\{1,2,3,4,5\}$, and find $P(X_2= 3|X_0= 1)$.

## Solution:

### Matrix (i)

Let's analyze the transitions for each state in $P_1$:

For state $i$, we denote the possible transitions by writing $i \to j$ if $p_{ij} > 0$.

1. From state 1: $1 \to \{1,5\}$ with probabilities $(\frac{1}{2}, \frac{1}{2})$
2. From state 2: $2 \to \{2,4\}$ with probabilities $(\frac{1}{2}, \frac{1}{2})$
3. From state 3: $3 \to \{3\}$ with probability 1
4. From state 4: $4 \to \{2,3,4,5\}$ with probabilities $(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{4})$
5. From state 5: $5 \to \{1,5\}$ with probabilities $(\frac{1}{2}, \frac{1}{2})$

**Communicating Classes**

The communicating classes are:

1. $C_1 = \{1,5\}$ - This is a closed class

   - States 1 and 5 communicate: $1 \leftrightarrow 5$
   - No transitions lead outside this class

2. $C_2 = \{2,4\}$ - This is not closed

   - States 2 and 4 communicate: $2 \leftrightarrow 4$
   - Can transition to state 3 from state 4

3. $C_3 = \{3\}$ - This is a closed class
   - State 3 only transitions to itself
   - Once entered, cannot be left

<img src="Code/Figures/m1.jpg" alt="alt text">

## Matrix (ii)

$$
P_2 = \begin{pmatrix}
\frac{1}{4} & 0 & \frac{3}{4} & 0 & 0 \\
0 & \frac{1}{3} & 0 & \frac{2}{3} & 0 \\
0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{6} & 0 & \frac{1}{3} & 0 \\
\frac{1}{4} & 0 & \frac{1}{2} & 0 & \frac{1}{4}
\end{pmatrix}
$$

The key insight is that this Markov chain naturally divides into two communicating classes with a specific relationship between them:

1. First Communicating Class: $\{1,3,5\}$

   - These states form a closed communicating class
   - Once the chain enters any of these states, it can never leave
   - States 1, 3, and 5 can all reach each other through various paths
   - This is the only closed class in the chain

2. Second Communicating Class: $\{2,4\}$
   - These states form an open communicating class
   - States 2 and 4 can reach each other
   - However, this class can transition to the closed class $\{1,3,5\}$
   - Once the chain leaves this class, it can never return

The structure shows a hierarchical relationship: the chain will eventually end up in the closed class $\{1,3,5\}$ if it starts in $\{2,4\}$. This is a key property that determines the long-term behavior of the chain.

<img src="Code/Figures/m2.jpg" alt="alt text">

The key difference between these matrices is that $P_1$ has multiple closed classes while $P_2$ has only one closed class which is absorbing.
<img src="Code/Figures/q1s3.png" alt="alt text">

## Finding Distributions in a Markov Chain

### Part 1: Finding Distribution of X₁

When $X₀$ has a uniform distribution on $\{1,2,3,4,5\}$, we need to calculate $λP$ where:

λ = $(\frac{1}{5}, \frac{1}{5}, \frac{1}{5}, \frac{1}{5}, \frac{1}{5})$

And $P$ is our transition matrix:

$$
P = \begin{pmatrix}
\frac{1}{4} & 0 & \frac{3}{4} & 0 & 0 \\
0 & \frac{1}{3} & 0 & \frac{2}{3} & 0 \\
0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{6} & 0 & \frac{1}{3} & 0 \\
\frac{1}{4} & 0 & \frac{1}{2} & 0 & \frac{1}{4}
\end{pmatrix}
$$

Let's calculate each probability $P(X₁ = i):$

For state 1:
$$P(X_1 = 1) = \frac{1}{5}(\frac{1}{4}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{3}{4}) + \frac{1}{5}(0) + \frac{1}{5}(0) = \frac{1}{5} = 0.2$$

For state 2:
$$P(X_1 = 2) = \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{3}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{2}{3}) + \frac{1}{5}(0) = \frac{1}{10} = 0.1$$

For state 3:
$$P(X_1 = 3) = \frac{1}{5}(\frac{3}{4}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{2}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{2}) = \frac{7}{20} = 0.35$$

For state 4:
$$P(X_1 = 4) = \frac{1}{5}(0) + \frac{1}{5}(\frac{2}{3}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{3}) + \frac{1}{5}(0) = \frac{1}{5} = 0.2$$

For state 5:
$$P(X_1 = 5) = \frac{1}{5}(0) + \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{2}) + \frac{1}{5}(0) + \frac{1}{5}(\frac{1}{4}) = \frac{3}{20} = 0.15$$

### Part 2: Finding $P(X₂ = 3|X₀ = 1)$

This requires calculating the $(1,3)$ entry of $P²$. We can find this by considering all possible 2-step paths from state 1 to state 3:

1. Path through state 1: $P(1 \to 1 \to 3) = \frac{1}{4} \cdot \frac{3}{4}$
2. Path through state 3: $P(1 \to 3 \to 3) = \frac{3}{4} \cdot \frac{1}{2}$

Therefore:
$$P(X_2 = 3|X_0 = 1) = \frac{1}{4} \cdot \frac{3}{4} + \frac{3}{4} \cdot \frac{1}{2} = \frac{3}{16} + \frac{3}{8} = \frac{9}{16}= 0.56$$

The distribution of $X₁$ shows higher probabilities for states in the closed class $\{1,3,5\}$, which aligns with our understanding that the chain will eventually remain in this class.

# Question 2: Two-Urn Ball Exchange Problem

$N$ black balls and $N$ white balls are distributed between two urns, numbered $1$ and $2$,so that each urn contains $N$ balls. At each step, one ball is chosen at random from eachurn and the two chosen balls are exchanged. Let $X_n$ be the number of white balls in urn 1 after $n$ steps. Find the transition matrix for the Markov chain $X$.

## Solution:

### 1. Understanding the State Space

- $X_n$ represents the number of white balls in urn 1 after n steps
- The state space is $S = \{0, 1, 2, ..., N\}$
- In state $k$:
  - Urn 1 has $k$ white balls and $(N-k)$ black balls
  - Urn 2 has $(N-k)$ white balls and $k$ black balls

### 2. Analyzing Possible Transitions

From state $k$, we can move to:

- $k+1$ (gain a white ball in urn 1)
- $k-1$ (lose a white ball from urn 1)
- $k$ (stay in the same state)

### 3. Calculating Transition Probabilities

#### a) For $P(k \to k+1)$:

We need to select a black ball from urn 1 and a white ball from urn 2

```
P(k → k+1) = (N-k)/N × (N-k)/N = ((N-k)/N)²
```

#### b) For $P(k \to k-1)$:

We need to select a white ball from urn 1 and a black ball from urn 2

```
P(k → k-1) = k/N × k/N = (k/N)²
```

#### c) For $P(k \to k)$:

We need to select either:

- Both white balls (probability: $\frac{k}{N} \cdot \frac{N-k}{N}$)
- Both black balls (probability: $\frac{N-k}{N} \cdot \frac{k}{N}$)

```
P(k → k) = 2k(N-k)/N²
```

### 4. Transition Matrix

The transition matrix $P$ is tridiagonal with entries:

$P_{ij} = \begin{cases} 
(\frac{N-i}{N})^2 & \text{if } j=i+1 \\
(\frac{i}{N})^2 & \text{if } j=i-1 \\
\frac{2i(N-i)}{N^2} & \text{if } j=i \\
0 & \text{otherwise}
\end{cases}$

where $i, j \in \{0, 1, ..., N\}$

### 5. Properties of the Chain

1. The matrix is stochastic (row sums = 1)
2. The chain is irreducible (all states communicate)
3. The chain is aperiodic (can return to any state in consecutive steps)

## Example

For $N=3$:

State: $\{0,1,2,3\}$

$
P = \begin{pmatrix}
0 & 1 & 0 & 0 \\
1/9 & 4/9 & 4/9 & 0 \\
0 & 4/9 & 4/9 & 1/9 \\
0 & 0 & 1 & 0
\end{pmatrix}
$

<img src="Code/Figures/Probability Oxford.jpeg" alt="alt text">

**Animation**

https://claude.site/artifacts/573d1a44-f74c-4912-92f4-244066200943

# Question 3:

A die is _“fixed”_ so that each time it is rolled the score cannot be the same as the preceding score, all other scores having probablity $1/5.$ If the first score is $6$, what are $P(\text{nth score is }6)$ and $P(\text{nth score is }1)$? _[Hint: you can simplify things by selecting anappropriate state-space; do you really need a6-state chain to answer the question?]_

# Solution:

1. First, let's think about the state space carefully. To know the distribution of the next roll, we only need to know whether the previous roll was 6 or not-6. We don't actually need to track what specific non-6 value was rolled.

2. So we can use a 2-state Markov chain with states:

   - State 1: $"6"$
   - State 2: "not 6" (representing $1,2,3,4,5$)

3. Let's find the transition matrix P:

   - From state 1 (6): Must go to state 2 (probability 1)
   - From state 2 (not 6):
     - Can go to 6 with probability $1/5$
     - Stay in "not 6" with probability $4/5$

   so
   $
   P = \begin{pmatrix}
   0 & 1 \\
   1/5 & 4/5 \\
   \end{pmatrix}
   $

4. We start in state 1 (given first score is 6)

5. This is exactly like Example 5.3 in the lecture notes with $α=1$ and $β=1/5$

6. From equation (5.2) in the notes:
   $$p(n)₁₁ = β/(α+β) + [α/(α+β)](1-α-β)ⁿ$$
   where $α=1, β=1/5$

   Therefore:

   $$P(\text{nth score is }6) = 1/6 + (5/6)(-4/5)ⁿ$$

7. For $P(\text{nth score is }1)$, first note $P(\text{score is }1 | \text{not }6) = 1/5$

   So $P(\text{nth score is }1) = P(\text{nth score is not }6) × 1/5$

   $= (1 - P(\text{nth score is } 6)) × 1/5$

   $= (1 - [1/6 + (5/6)(-4/5)ⁿ]) × 1/5$

   $= (5/6 - (5/6)(-4/5)ⁿ) × 1/5$

   $= 1/6 - (1/6)(-4/5)ⁿ$

Therefore:

$P(\text{nth score is }6) = 1/6 + (5/6)(-4/5)ⁿ$

$P(\text{nth score is }1) = 1/6 - (1/6)(-4/5)ⁿ$

As $n→∞$, both probabilities converge to $1/6,$ which makes sense as this is the stationary distribution of the chain.

## Steps:

We have a 2-state Markov chain with transition matrix:

$P = \begin{bmatrix} 0 & 1 \\ \frac{1}{5} & \frac{4}{5} \end{bmatrix}$

Starting in state 1, we want to find $P(\text{nth roll is }6)$ and $P(\text{nth roll is }1)$.

### Step 1: Find Eigenvalues

The characteristic equation is:
$\det(P - \lambda I) = 0$

$\begin{vmatrix} -\lambda & 1 \\ \frac{1}{5} & \frac{4}{5}-\lambda \end{vmatrix} = 0$

$\lambda^2 - \frac{4}{5}\lambda - \frac{1}{5} = 0$

Using the quadratic formula:
$\lambda = \frac{4/5 \pm \sqrt{16/25 + 4/5}}{2} = \frac{4/5 \pm \sqrt{36/25}}{2} = \frac{4/5 \pm 6/5}{2}$

Therefore:

- $\lambda_1 = 1$
- $\lambda_2 = -\frac{1}{5}$

### Step 2: Find Eigenvectors

For $\lambda_1 = 1$:

$\begin{bmatrix} -1 & 1 \\ \frac{1}{5} & -\frac{1}{5} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

This gives us eigenvector:

$v_1 = \begin{bmatrix} \frac{1}{6} \\ \frac{5}{6} \end{bmatrix}$

For $\lambda_2 = -\frac{1}{5}$:

$\begin{bmatrix} \frac{1}{5} & 1 \\ \frac{1}{5} & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

This gives us eigenvector:

$v_2 = \begin{bmatrix} 1 \\ -\frac{1}{5} \end{bmatrix}$

### Step 3: Express Initial State

Our initial state is $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$

We need to find $a$ and $b$ where:

$\begin{bmatrix} 1 \\ 0 \end{bmatrix} = a\begin{bmatrix} \frac{1}{6} \\ \frac{5}{6} \end{bmatrix} + b\begin{bmatrix} 1 \\ -\frac{1}{5} \end{bmatrix}$

Solving these equations:

- $a = \frac{5}{6}$
- $b = \frac{5}{6}$

### Step 4: Final Formula

After $n-1$ steps, our distribution is:

$a(v_1)(1)^{n-1} + b(v_2)(-\frac{1}{5})^{n-1}$

$= \frac{5}{6}\begin{bmatrix} \frac{1}{6} \\ \frac{5}{6} \end{bmatrix} + \frac{5}{6}\begin{bmatrix} 1 \\ -\frac{1}{5} \end{bmatrix}(-\frac{4}{5})^{n-1}$

Therefore:

- $P(\text{nth roll is }6) = \frac{1}{6} + \frac{5}{6}(-\frac{4}{5})^{n-1}$
- $P(\text{nth roll is }1) = \frac{1}{6} - \frac{1}{6}(-\frac{4}{5})^{n-1}$

As $n \to \infty$:

- $(-\frac{4}{5})^n \to 0$ since $|-\frac{4}{5}| < 1$
- Both probabilities converge to $\frac{1}{6}$, which is the stationary distribution
- The rate of convergence is determined by the second eigenvalue $\lambda_2 = -\frac{1}{5}$

This demonstrates how eigenvalue decomposition provides both the long-term behavior and the rate of convergence for Markov chains.

> The eigenvalue 1 represents this conservation of probability - when we multiply a probability distribution by $P,$ the components must still sum to 1.

# Question 4:

Let $X_n,n\geq 1$, be i.i.d. $P(X_n= 1) =p$, $P(X_n=−1) = 1−p$, where $p ∈ (0,1)$. For each of the following, decide if $(Y_n)$ is a Markov chain. If so, find its transition probabilities.

(a) $Y_n=X_n.$

(b) $Y_n=S_n$ where $S_n=X_1+X_2+···+X_n.$

(c) $Y_n=M_n$ where $M_n= \text{max}(0,S_1,S_2,...,S_n)$.

(d) $Y_n=M_n − S_n$.

(e) $Y_n=X_n X_{n+1}$

## Solution

## Case (a): Direct Sequence $Y_n = X_n$

### Analysis

This forms a Markov chain, and more specifically, an i.i.d. sequence. Each state is independent of all previous states.

### Transition Matrix

$P = \begin{bmatrix} 
p & 1-p \\
p & 1-p
\end{bmatrix}$

For any current state $i$:

- $P(Y_{n+1} = 1 | Y_n = i) = p$
- $P(Y_{n+1} = -1 | Y_n = i) = 1-p$

## Case (b): Running Sum $Y_n = S_n = \sum_{i=1}^n X_i$

### Analysis

This forms a Markov chain because:

- $S_{n+1} = S_n + X_{n+1}$
- Future state depends only on current state and independent increment

### Transition Probabilities

For any state $i$:

- $P(S_{n+1} = i+1 | S_n = i) = p$
- $P(S_{n+1} = i-1 | S_n = i) = 1-p$

This creates a random walk on $\mathbb{Z}$ with transition matrix elements:

$$
P_{ij} = \begin{cases}
p & \text{if } j = i+1 \\
1-p & \text{if } j = i-1 \\
0 & \text{otherwise}
\end{cases}
$$

## Case (c): Running Maximum $Y_n = M_n = \max(0,S_1,S_2,...,S_n)$

### Analysis

This is not a Markov chain.

#### Counter-Example

Consider two paths reaching $M_n = 2$:

1. Path 1: $S_1 = 1, S_2 = 2$
2. Path 2: $S_1 = 2, S_2 = 1$

The probability distribution of $M_{n+1}$ differs for these paths despite having the same current state, violating the Markov property.

## Case (d): Maximum-Current Difference $Y_n = M_n - S_n$

### Analysis

This is not a Markov chain. The future behavior depends on both:

- The current difference $(M_n - S_n)$
- The actual values of $M_n$ and $S_n$

## Case (e): Product of Consecutive Terms $Y_n = X_nX_{n+1}$

### Analysis

This forms a Markov chain due to the overlap structure:

- $Y_n = X_nX_{n+1}$
- $Y_{n+1} = X_{n+1}X_{n+2}$

### Transition Probabilities

$$
P(Y_{n+1} = j | Y_n = i) = \begin{cases}
p^2 + (1-p)^2 & \text{if } i=j=1 \text{ or } i=j=-1 \\
2p(1-p) & \text{if } i \neq j
\end{cases}
$$

### Transition Matrix

$P = \begin{bmatrix} 
p^2 + (1-p)^2 & 2p(1-p) \\
2p(1-p) & p^2 + (1-p)^2
\end{bmatrix}$

This matrix is symmetric due to the identical behavior when transitioning between states 1 and -1.

# Question 5: Proving Properties of Communicating Classes in Markov Chains

Let $C$ be a communicating class of a Markov chain. Prove the following statements:

(a) Either all states in $C$ are recurrent, or all are transient. _[Hint: use the criterion in terms of $∑p^{(n)}_{ii}$ to show that if $i$ is recurrent and $i↔j$ then also $j$ is recurrent.]\_

(b) If $C$ is recurrent then $C$ is closed. If $C$ is finite and closed, then $C$ is recurrent

## Solution:

Let's explore these fundamental properties of Markov chains through rigorous mathematical proof.

## Part A: Uniformity of Recurrence in Communicating Classes

### Theorem

Let $C$ be a communicating class. Either all states in $C$ are recurrent, or all states are transient.

### Proof

Let's prove this systematically:

1. Recall the criterion for recurrence:

   - A state $i$ is recurrent if $\sum_{n=0}^{\infty} p_{ii}^{(n)} = \infty$
   - A state $i$ is transient if $\sum_{n=0}^{\infty} p_{ii}^{(n)} < \infty$

2. Consider two states $i, j \in C$ where $i \leftrightarrow j$

   - This means $\exists a, b \in \mathbb{N}$ such that:
   - $p_{ij}^{(a)} > 0$ (can reach $j$ from $i$ in $a$ steps)
   - $p_{ji}^{(b)} > 0$ (can reach $i$ from $j$ in $b$ steps)

3. For any path from $i$ to $i$ of length $n$:

   - We can construct a path from $j$ to $j$ of length $n+a+b$ by:
     - Going from $j$ to $i$ in $b$ steps
     - Following the $i$ to $i$ path in $n$ steps
     - Going from $i$ to $j$ in $a$ steps

4. This gives us:
   $p_{jj}^{(n+a+b)} \geq p_{ji}^{(b)} \cdot p_{ii}^{(n)} \cdot p_{ij}^{(a)} = c \cdot p_{ii}^{(n)}$
   where $c = p_{ji}^{(b)} \cdot p_{ij}^{(a)} > 0$

5. Therefore:
   $\sum_{n=0}^{\infty} p_{jj}^{(n)} \geq c \sum_{n=0}^{\infty} p_{ii}^{(n)}$

6. Thus:
   - If $i$ is recurrent ($\sum p_{ii}^{(n)} = \infty$), then $j$ must also be recurrent
   - By symmetry, if $j$ is recurrent, then $i$ must be recurrent

## Part B: Properties of Recurrent and Closed Classes

### Theorem

1. If $C$ is recurrent, then $C$ is closed
2. If $C$ is finite and closed, then $C$ is recurrent

### Proof of Statement 1

Proof by contradiction:

1. Suppose $C$ is recurrent but not closed
2. $\exists i \in C$ and $j \notin C$ such that $p_{ij} > 0$
3. This means $P(\text{never returning to }i) > 0$
4. But this contradicts the definition of recurrence
5. Therefore $C$ must be closed

### Proof of Statement 2

1. Let $C$ be finite and closed
2. For any $i \in C$:
   - The chain must stay in $C$ (since $C$ is closed)
   - Since $C$ is finite, by the pigeonhole principle, some state must be visited infinitely often
   - All states communicate $\Rightarrow$ all states are visited infinitely often
   - Therefore each state is recurrent

This completes our proof of both key properties of communicating classes in Markov chains.

# Question 6: Gambler's Ruin Problem with Variable Stakes

Consider a gambling scenario where:

Let $X = \{X_n : n \geq 0\}$ represent a gambler's capital after the $n$-th coin toss, where:

- Initial capital is £8 ($X_0 = 8$)
- Target amount is £10
- Game involves betting on a fair coin where:
  - Heads: win amount equal to stake plus stake returned
  - Tails: lose entire stake

The gambler employs the following strategy:

- If capital $< £5$: stake entire amount
- If capital $\geq £5$: stake amount needed to reach £10 if won

For example:

- First stake = £2
- After first toss: $X_1 = \begin{cases} 10 & \text{if heads} \\ 6 & \text{if tails} \end{cases}$

### Part (a)

Describe $(X_n, n \geq 0)$ as a Markov chain.

### Part (b)

Calculate $\mathbb{E}[\tau]$ where $\tau$ is the number of coin tosses until either:

- Reaching £10, or
- Losing all money

### Part (c)

Prove that $\mathbb{P}(\text{reach £10}) = \frac{4}{5}$

### Part (d)

Show that:
$$\mathbb{P}(X_1 = 10 \mid \text{eventually reach £10}) = \frac{5}{8}$$

Then describe the distribution of $(X_n, n \geq 0)$ conditional on reaching £10.

### Part (e)

For a Markov chain $(X_n, n \geq 0)$ on $\mathbb{N}$ with:

- $p_{0,0} = 1$
- $p_{i,i+1} = p = 1 - p_{i,i-1}$ for $i \geq 1$
- $p > \frac{1}{2}$ (upward bias)
- $X_0 = j > 0$

Given that the probability of absorption at 0 is $(\frac{1-p}{p})^j$, describe the distribution of $(X_n, n \geq 0)$ conditional on absorption at 0.

## Solution:

Imagine you start with £8 in your pocket and you're trying to turn it into £10. You're playing a simple coin flip game at a casino. Here's how it works:
When you bet money (let's say £2), one of two things can happen:

1. If the coin lands on heads, you win the same amount you bet (so you'd win £2 and get your original £2 back, meaning you now have £10)
2. If it lands on tails, you lose whatever you bet (so you'd lose your £2 and now have £6)

The interesting part is how the gambler decides how much to bet. They follow this strategy:

- If they have less than £5, they go "all in" and bet everything they have (desperate times!)
- If they have £5 or more, they're more careful. They only bet exactly what they need to reach £10 if they win

## Solution Part (a):

The key is to carefully enumerate all possible transitions based on the stated rules. The transitions depend on the gambler's current capital:

1. If $X_n = 0$ or $X_n = 10$, these are absorbing states. Once the gambler's capital reaches £0 or £10, no further changes occur. Thus:

   $P(X_{n+1} = 0|X_n = 0) = 1$ and $P(X_{n+1} = 10|X_n = 10) = 1$

2. If $X_n < 5$, the gambler stakes all their capital, so their possible states after the next toss are:

   - On heads (win), the capital doubles to $2X_n$
   - On tails (loss), the capital becomes £0

   The transition probabilities are:

   $P(X_{n+1} = 2X_n|X_n) = \frac{1}{2}$ and $P(X_{n+1} = 0|X_n) = \frac{1}{2}$

3. If $5 \leq X_n < 10$, the gambler stakes just enough to reach £10 if they win. If they lose, they drop to $X_n - (10 - X_n) = 2X_n - 10$ (their stake is $10 - X_n$). The transitions are:

   - On heads (win), capital becomes £10
   - On tails (loss), capital becomes $2X_n - 10$

   The transition probabilities are:

   $P(X_{n+1} = 10|X_n) = \frac{1}{2}$ and $P(X_{n+1} = 2X_n - 10|X_n) = \frac{1}{2}$

4. If $X_n = 5$, the gambler stakes £5 to reach £10 or £0:

   $P(X_{n+1} = 10|X_n = 5) = \frac{1}{2}$ and $P(X_{n+1} = 0|X_n = 5) = \frac{1}{2}$

The transition matrix $P$ for this Markov chain is an 11×11 matrix (for states 0 through 10) given by:

$$
P = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\frac{1}{2} & 0 & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\frac{1}{2} & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 & 0 \\
\frac{1}{2} & 0 & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 \\
\frac{1}{2} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} & 0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

Let me explain the structure of this transition matrix:

1. Row 0 and row 10 have a single 1 on the diagonal since these are absorbing states - once you reach £0 or £10, you stay there.

2. For states 1-4, on a win (probability 1/2) the capital doubles, and on a loss (probability 1/2) it goes to 0. This creates transitions to either state 0 or state 2×i where i is the current state.

3. For state 5, there's a probability 1/2 of transitioning to 0 and 1/2 of reaching 10.

4. For states 6-9, on a win (probability 1/2) the gambler reaches state 10, and on a loss (probability 1/2) they lose twice their stake, landing at state 2i-10 where i is the current state.

This matrix fully captures the dynamics of the gambling system, showing all possible transitions and their probabilities. Each row sums to 1, as required for a valid transition matrix.

## Part (b):

Starting with £8, let's think about what happens at each step and how to calculate the expected number of tosses until reaching either £0 or £10.

Let's say $m_i$ represents the expected number of tosses needed when starting with £i.

Since we start with £8, let's understand what happens here:

1. When we have £8, we need to reach £10, so we stake £2
2. After one toss:
   - With probability 1/2 (heads), we win and reach £10
   - With probability 1/2 (tails), we lose £2 and drop to £6

We can write this as an equation:
$m_8 = 1 + \frac{1}{2}m_{10} + \frac{1}{2}m_6$

Since £10 is our target, $m_{10} = 0$. So:
$m_8 = 1 + \frac{1}{2}m_6$

Now at £6:

- We stake £4 (to reach £10 if we win)
- With heads, we reach £10
- With tails, we drop to £2 (losing £4)

So:
$m_6 = 1 + \frac{1}{2}m_{10} + \frac{1}{2}m_2 = 1 + \frac{1}{2}m_2$

At £2:

- We stake everything (£2)
- With heads, we reach £4
- With tails, we lose everything

So:

$m_2 = 1 + \frac{1}{2}m_4 + \frac{1}{2}m_0$

From £8: $m_8 = 1 + \frac{1}{2}m_6$

From £6: $m_6 = 1 + \frac{1}{2}m_2$

From £2: $m_2 = 1 + \frac{1}{2}m_4$

From £4: $m_4 = 1 + \frac{1}{2}m_8$

Let's solve this system of equations by substituting back. First, let's substitute the expression for $m_4$ into the equation for $m_2$:

$m_2 = 1 + \frac{1}{2}(1 + \frac{1}{2}m_8)$

$m_2 = 1 + \frac{1}{2} + \frac{1}{4}m_8$

Now we can substitute this expression for $m_2$ into the equation for $m_6$:

$m_6 = 1 + \frac{1}{2}(1 + \frac{1}{2} + \frac{1}{4}m_8)$

$m_6 = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8}m_8$

Finally, we can substitute this into our original equation for $m_8$:

$m_8 = 1 + \frac{1}{2}(1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8}m_8)$

$m_8 = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}m_8$

Now we can solve for $m_8$:

$\frac{15}{16}m_8 = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} = \frac{15}{8}$

Therefore:

$m_8 = \frac{15}{8} \times \frac{16}{15} = 2$

So starting with £8, it takes on average 2 tosses until either reaching £10 or losing everything. This makes intuitive sense because:

- With probability 1/2, we win on the first toss and reach £10
- With probability 1/2, we lose and drop to £6, from where we need on average 2 more tosses
- So the average is $\frac{1}{2}(1) + \frac{1}{2}(1+2) = 2$ tosses

Let me solve part (c) step by step, explaining the reasoning clearly.

## Solution Part (c): Proving P(reach £10) = 4/5

Let's solve this systematically using hitting probabilities.

Let $h(x)$ represent the probability of reaching £10 starting from £x. We need to find $h(8)$ since we start with £8.

First, let's establish our boundary conditions:

- $h(0) = 0$ (if we lose everything, we can't reach £10)
- $h(10) = 1$ (if we reach £10, we're done)

For any other state $x$, we can write equations based on the next possible transitions:

### For states x < 5:

When our capital is less than £5, we bet everything. From state $x$:

- With probability $\frac{1}{2}$, we lose everything (go to 0)
- With probability $\frac{1}{2}$, we double our money (go to $2x$)

This gives us:
$$h(x) = \frac{1}{2}h(0) + \frac{1}{2}h(2x) \text{ for } x < 5$$

### For states x ≥ 5:

When our capital is at least £5, we bet what we need to reach £10. From state $x$:

- With probability $\frac{1}{2}$, we lose our stake (go to $x-(10-x)$)
- With probability $\frac{1}{2}$, we reach our target (go to 10)

This gives us:
$$h(x) = \frac{1}{2}h(2x-10) + \frac{1}{2} \text{ for } x \geq 5$$

### Working backwards from our starting state £8:

$$h(8) = \frac{1}{2}h(6) + \frac{1}{2}$$
$$h(6) = \frac{1}{2}h(2) + \frac{1}{2}$$
$$h(2) = \frac{1}{2}h(0) + \frac{1}{2}h(4)$$
$$h(4) = \frac{1}{2}h(0) + \frac{1}{2}h(8)$$

### Solving the system:

1. From $h(2)$ equation:
   $$h(2) = \frac{1}{2}(0) + \frac{1}{2}h(4) = \frac{1}{2}h(4)$$

2. From $h(4)$ equation:
   $$h(4) = 0 + \frac{1}{2}h(8)$$

3. Therefore:
   $$h(2) = \frac{1}{4}h(8)$$

4. From $h(6)$ equation:
   $$h(6) = \frac{1}{2}h(2) + \frac{1}{2} = \frac{1}{8}h(8) + \frac{1}{2}$$

5. Finally, from $h(8)$ equation:
   $$h(8) = \frac{1}{2}(\frac{1}{8}h(8) + \frac{1}{2}) + \frac{1}{2}$$
   $$h(8) = \frac{1}{16}h(8) + \frac{1}{4} + \frac{1}{2}$$
   $$\frac{15}{16}h(8) = \frac{3}{4}$$
   $$h(8) = \frac{4}{5}$$

Therefore, starting with £8, the probability of reaching £10 is $\frac{4}{5}$.

## Solution Part (d): Conditional Probabilities Given Success

Part (d) asks us to prove two things:

1. Show that $\mathbb{P}(X_1 = 10 | \text{eventually reach £10}) = \frac{5}{8}$
2. Describe the distribution of $(X_n, n \geq 0)$ conditional on reaching £10

Let's solve each part and understand the intuition behind them.

### First Part: Computing $\mathbb{P}(X_1 = 10 | \text{eventually reach £10})$

We can use Bayes' rule to solve this. Let's break it down:

$\mathbb{P}(X_1 = 10 | \text{eventually reach £10}) = \frac{\mathbb{P}(X_1 = 10 \text{ AND eventually reach £10})}{\mathbb{P}(\text{eventually reach £10})}$

We know from part (c) that $\mathbb{P}(\text{eventually reach £10}) = \frac{4}{5}$

When $X_1 = 10$, we've already reached £10, so:
$\mathbb{P}(X_1 = 10 \text{ AND eventually reach £10}) = \mathbb{P}(X_1 = 10) = \frac{1}{2}$

Therefore:
$\mathbb{P}(X_1 = 10 | \text{eventually reach £10}) = \frac{\frac{1}{2}}{\frac{4}{5}} = \frac{5}{8}$

### Second Part: Distribution Conditional on Success

The conditional process follows what's called an h-transform of the original chain. The key insight is that the transition probabilities are modified by the probability of eventual success from each state.

Let $h(x)$ be the probability of reaching £10 from state x (which we calculated in part c).

The conditional transition probabilities are given by:

$\mathbb{P}(X_{n+1} = j | X_n = i, \text{success}) = p_{ij} \frac{h(j)}{h(i)}$

Where $p_{ij}$ are the original transition probabilities.

For example, from state 8:

- Original probability of going to 10 was $\frac{1}{2}$
- Original probability of going to 6 was $\frac{1}{2}$

The conditional probabilities become:

- $\mathbb{P}(X_{n+1} = 10 | X_n = 8, \text{success}) = \frac{1}{2} \cdot \frac{1}{h(8)} = \frac{5}{8}$
- $\mathbb{P}(X_{n+1} = 6 | X_n = 8, \text{success}) = \frac{1}{2} \cdot \frac{h(6)}{h(8)} = \frac{3}{8}$

This makes intuitive sense - conditioning on eventual success makes transitions toward 10 more likely than they were in the original chain.

The process will still eventually reach 10 with probability 1, but it tends to take paths that are "biased upward" compared to the original chain. Once it reaches 10, it stays there (it's still an absorbing state).

This conditional process is itself a Markov chain, but with different transition probabilities that favor paths leading to success. The new transition probabilities can be calculated for each state using the formula above and the hitting probabilities we found in part (c).

---

# The h-Transform in Markov Chains

### Introduction

When analyzing Markov chains conditioned on hitting a specific state, we use an elegant mathematical tool called the h-transform. This transform helps us understand how the process behaves when we only consider paths that lead to our target state.

### Mathematical Formulation

Let $(X_n)_{n\geq0}$ be a Markov chain with transition probabilities $p_{ij}$. Let $h(i)$ be the probability of hitting our target state when starting from state $i$. The h-transform gives us new transition probabilities:

$$\tilde{p}_{ij} = p_{ij}\frac{h(j)}{h(i)}$$

where $\tilde{p}_{ij}$ represents the probability of transitioning from $i$ to $j$ given that we eventually hit our target state.

### Intuition

This formula elegantly captures two key ideas:

1. The original dynamics of the chain ($p_{ij}$)
2. The relative likelihood of success after the transition ($\frac{h(j)}{h(i)}$)

For example, in our gambling problem where we aim to reach £10:

- Starting from £8, we originally had:
  $$p_{8,10} = \frac{1}{2} \text{ and } p_{8,6} = \frac{1}{2}$$
- After the h-transform, we get:
  $$\tilde{p}_{8,10} = \frac{1}{2}\cdot\frac{1}{4/5} = \frac{5}{8}$$
  $$\tilde{p}_{8,6} = \frac{1}{2}\cdot\frac{3/5}{4/5} = \frac{3}{8}$$

### Significance

The h-transform maintains the Markov property while incorporating our knowledge about eventual success. The new chain describes the behavior we would observe if we only watched paths that reach our target state.

The transformed chain puts higher probability on transitions that make success more likely, giving us insight into the "typical" path to success.

---

## Solution Part (e): Conditional Distribution of Upward-Biased Random Walk Given Absorption

Let's analyze a Markov chain $(X_n)_{n\geq0}$ on $\mathbb{N}$ with:

- Absorbing state at 0: $p_{0,0} = 1$
- Upward bias: $p = p_{i,i+1} > \frac{1}{2}$ for all $i \geq 1$
- Downward probability: $p_{i,i-1} = 1-p$ for all $i \geq 1$
- Starting state: $X_0 = j > 0$

### Key Insight

We're given that $\mathbb{P}(absorption\text{ at }0|X_0=j) = (\frac{1-p}{p})^j$. Despite the upward bias ($p > \frac{1}{2}$), we want to understand paths that lead to absorption at 0.

### Using the h-Transform

Let $h(i)$ be the probability of absorption at 0 starting from state $i$:
$$h(i) = (\frac{1-p}{p})^i$$

For the conditional process, new transition probabilities are:
$$\tilde{p}_{i,i+1} = p\frac{h(i+1)}{h(i)} = p\frac{(\frac{1-p}{p})^{i+1}}{(\frac{1-p}{p})^i} = (1-p)$$

$$\tilde{p}_{i,i-1} = (1-p)\frac{h(i-1)}{h(i)} = (1-p)\frac{(\frac{1-p}{p})^{i-1}}{(\frac{1-p}{p})^i} = p$$

### Interpretation

The conditional process reverses the probabilities of the original chain:

1. Original upward probability $p$ becomes downward probability
2. Original downward probability $(1-p)$ becomes upward probability
3. State 0 remains absorbing

This makes intuitive sense: conditioning on absorption at 0 should favor downward movement.

### Distribution Description

The conditional process is:

- A Markov chain on $\mathbb{N}$
- Starting from $j$
- With transition probabilities:
  $$\tilde{p}_{0,0} = 1$$
  $$\tilde{p}_{i,i+1} = 1-p < \frac{1}{2}$$
  $$\tilde{p}_{i,i-1} = p > \frac{1}{2}$$

This is a downward-biased random walk that will reach 0 with probability 1. The paths we observe will tend to drift downward, even though the original process had an upward drift.

### Final Note

This is a beautiful example of how conditioning can fundamentally change the behavior of a Markov chain. The h-transform gives us explicit formulas for the new transition probabilities and helps us understand what "typical" paths to absorption look like.

# Conditioning and Bias Reversal in Markov Chains

### Introduction

One of the most fascinating phenomena in Markov chain theory is how conditioning on a future event can dramatically alter the behavior of the process. The transformation of an upward-biased random walk into a downward-biased one, when conditioned on absorption at zero, provides a beautiful illustration of this principle.

### Mathematical Framework

Consider a Markov chain $(X_n)_{n\geq0}$ on $\mathbb{N}$ with transition probabilities:
$$p_{i,i+1} = p > \frac{1}{2}, \quad p_{i,i-1} = 1-p < \frac{1}{2}$$

The probability of eventual absorption at 0 from state $i$ is:
$$h(i) = \left(\frac{1-p}{p}\right)^i$$

### The h-Transform

When we condition on absorption at 0, the new transition probabilities become:
$$\tilde{p}_{i,i+1} = p\frac{h(i+1)}{h(i)} = p\cdot\frac{(\frac{1-p}{p})^{i+1}}{(\frac{1-p}{p})^i} = 1-p$$
$$\tilde{p}_{i,i-1} = (1-p)\frac{h(i-1)}{h(i)} = (1-p)\cdot\frac{(\frac{1-p}{p})^{i-1}}{(\frac{1-p}{p})^i} = p$$

### Intuitive Understanding

This reversal of bias can be understood through the lens of conditional probability. At each step:

- Moving upward decreases our absorption probability by a factor of $\frac{1-p}{p}$
- Moving downward increases our absorption probability by a factor of $\frac{p}{1-p}$

The h-transform balances these factors against the original transition probabilities, resulting in a process that favors paths leading to our target state.

### Practical Significance

This phenomenon reminds us that observing a rare event (absorption at 0 in an upward-biased walk) typically occurs through an atypical sequence of steps. The conditional process describes precisely these atypical but successful paths to absorption.

The formula $\tilde{p}_{ij} = p_{ij}\frac{h(j)}{h(i)}$ elegantly captures this interplay between the original dynamics and our knowledge of eventual success.

# Question:

A Markov chain with state space $\{0,1,2,...\}$ is called a _“birth-and-death chain”_ if the only non-zero transition probabilities from state $i$ are to states $i−1$ and $i+ 1$, except when $i= 0$, where the only non-zero transition probabilities are to states $0$ and $1$. Consider a general birth-and-death chain and write $p_i=p_{i,i+1}$ and $q_i=p_{i,i−1}= 1−p_i$. Assume that $p_i$ and $q_i$ are positive for all $i≥1$.

## Solution Part (a):

We need to prove that:

1. $p_ih_i + q_ih_i = h_i = p_ih_{i+1} + q_ih_{i-1}$
2. From this, deduce that $u_{i+1} = \frac{q_i}{p_i}u_i$ for all $i \geq 1$

### Step 1: Understanding Hitting Probabilities

By Theorem 5.7 from the notes, hitting probabilities must satisfy certain equations. For any state $i \geq 1$, we can condition on the first step to get:

$h_i = p_ih_{i+1} + q_ih_{i-1}$

This equation emerges because:

- With probability $p_i$, we go to state $i+1$ and then need to hit $0$ (probability $h_{i+1}$)
- With probability $q_i$, we go to state $i-1$ and then need to hit $0$ (probability $h_{i-1}$)

### Step 2: Looking at the Equation

Note that $p_ih_i + q_ih_i = h_i$ is trivial since $p_i + q_i = 1$. Therefore, the first part is established:

$p_ih_i + q_ih_i = h_i = p_ih_{i+1} + q_ih_{i-1}$

### Step 3: Deducing the Relationship for $u_i$

Recall that $u_i = h_{i-1} - h_i$

From the hitting probability equation:
$h_i = p_ih_{i+1} + q_ih_{i-1}$

Rearranging to isolate $h_{i-1} - h_i$:

$h_{i-1} - h_i = \frac{p_i}{q_i}(h_i - h_{i+1})$

Therefore:
$u_i = \frac{p_i}{q_i}u_{i+1}$

Which gives us:
$u_{i+1} = \frac{q_i}{p_i}u_i$

This completes our proof, showing that consecutive differences in hitting probabilities are related by the ratio of death to birth probabilities at each state.

This relationship will be crucial for understanding the long-term behavior of the chain and determining conditions for recurrence versus transience.

Let me help solve this birth-and-death chain problem step by step, building up from the simpler parts to the more complex conclusions.

## Soluiton Part (b) - Expressing $u_i$ and $h_i$

### Finding $u_i$ in terms of $γ_i$ and $u_1$

From part (a), we found that $u_{i+1} = \frac{q_i}{p_i}u_i$ for all $i \geq 1$.

Let's apply this recursively:
$u_2 = \frac{q_1}{p_1}u_1$
$u_3 = \frac{q_2}{p_2}u_2 = \frac{q_1}{p_1}\frac{q_2}{p_2}u_1$

We can see a pattern forming. Given the definition $\gamma_i = \frac{q_1}{p_1}\frac{q_2}{p_2}...\frac{q_{i-1}}{p_{i-1}}$, we can write:

$u_i = \gamma_i u_1$ for all $i \geq 1$

### Finding $h_i$ in terms of $γ_1,\dots,γ_i$ and $u_1$

Since $u_i = h_{i-1} - h_i$, we can write:
$h_0 - h_1 = u_1$
$h_1 - h_2 = \gamma_2u_1$
$h_2 - h_3 = \gamma_3u_1$
...
$h_{i-1} - h_i = \gamma_iu_1$

Adding these equations and using $h_0 = 1$ (since we start at 0, we hit 0 with probability 1):

$h_i = 1 - u_1(1 + \gamma_2 + \gamma_3 + ... + \gamma_i)$
$h_i = 1 - u_1\sum_{j=1}^i \gamma_j$

## Soluiton Part (c) - Finding u1 and Transience Condition

### Determining u1

For hitting probabilities, we need $0 \leq h_i \leq 1$ for all $i$. Also, since they represent probabilities of ever hitting 0, we want the minimal non-negative solution.

Since $h_i = 1 - u_1\sum_{j=1}^i \gamma_j$, and we want the minimal solution:

If $\sum_{i=1}^{\infty} \gamma_i = \infty$, then $u_1 = 0$ (to keep $h_i \geq 0$)
If $\sum_{i=1}^{\infty} \gamma_i < \infty$, then $u_1 = \frac{1}{\sum_{i=1}^{\infty} \gamma_i}$

### Transience Condition

When $p_{0,1} > 0$, the chain is transient if and only if there's a positive probability of never returning to 0.

Starting from state 1:
P(never hit 0) = $1 - h_1 = u_1 = \frac{1}{\sum_{i=1}^{\infty} \gamma_i}$ if the sum converges
= 0 if the sum diverges

Therefore, the chain is transient if and only if $\sum_{i=1}^{\infty} \gamma_i < \infty$

## Solution Part (d) - Special Case

When $p_i = (\frac{i+1}{i})^2q_i$:

$\frac{q_i}{p_i} = (\frac{i}{i+1})^2$

Therefore:
$\gamma_i = \prod_{j=1}^{i-1} (\frac{j}{j+1})^2 = (\frac{1}{i})^2$

Thus:
$\sum_{i=1}^{\infty} \gamma_i = \sum_{i=1}^{\infty} \frac{1}{i^2} = \frac{\pi^2}{6}$

Therefore:
$P(X_n \geq 1 \text{ for all } n \geq 1) = 1 - h_1 = u_1 = \frac{6}{\pi^2}$

Let me explain the key insights and learning lessons from this birth-and-death chain problem.

## Key Lessons and Insights

## 1. The Power of Recursive Relations

This problem beautifully demonstrates how complex Markov chain behavior can be understood through recursive relationships. When we discovered that $u_{i+1} = \frac{q_i}{p_i}u_i$, it gave us a way to understand differences in hitting probabilities at all states in terms of just one value ($u_1$). This teaches us that in Markov chains, local behavior (transition probabilities) can determine global behavior (hitting probabilities) through recursive relationships.

## 2. The Role of Products in Markov Chains

The appearance of $\gamma_i$ as a product ($\gamma_i = \frac{q_1}{p_1}\frac{q_2}{p_2}...\frac{q_{i-1}}{p_{i-1}}$) is not coincidental. In Markov chains, products often emerge when we're looking at probabilities of specific paths through the chain. Each factor $\frac{q_j}{p_j}$ represents the relative likelihood of moving backward versus forward at state j. This teaches us to look for multiplicative structures when analyzing path probabilities in Markov chains.

## 3. The Connection Between Series and Recurrence

One of the most profound insights is how the convergence of an infinite series ($\sum_{i=1}^{\infty} \gamma_i$) determines whether the chain is recurrent or transient. This connects discrete probability theory with classical analysis. In particular:

- If the series converges, the chain is transient (can escape to infinity)
- If the series diverges, the chain is recurrent (always returns)

This pattern appears frequently in probability theory - the behavior of infinite series often determines long-term probabilistic behavior.

## 4. The Beauty of Specific Solutions

The special case where $p_i = (\frac{i+1}{i})^2q_i$ leads to the remarkable result that $P(X_n \geq 1 \text{ for all } n \geq 1) = \frac{6}{\pi^2}$. This teaches us two things:

1. Carefully chosen parameters can lead to elegant solutions involving fundamental mathematical constants
2. The connection to $\zeta(2) = \frac{\pi^2}{6}$ isn't coincidental - it emerges from the sum of reciprocal squares in our $\gamma_i$ series

## 5. The Importance of Minimal Solutions

When solving for hitting probabilities, we learned that we need the minimal non-negative solution. This principle - that among multiple mathematical solutions, the physical solution is often the minimal one - appears frequently in probability theory and physics.

## Practical Applications

These insights have practical applications:

- Modeling population growth (where births and deaths occur)
- Understanding queueing systems
- Analyzing random walks with drift
- Studying particle diffusion processes

## Methodological Lessons

The solution process teaches us valuable problem-solving strategies:

1. Break down complex problems into simpler recursive relationships
2. Look for patterns that can be expressed as products or series
3. Use physical constraints (like probabilities being in [0,1]) to select appropriate solutions
4. Connect local behavior (transition probabilities) to global behavior (recurrence/transience)

This problem exemplifies how mathematical analysis can reveal deep structural properties of stochastic processes, connecting discrete probability, analysis, and physical intuition in a remarkable way.
