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
