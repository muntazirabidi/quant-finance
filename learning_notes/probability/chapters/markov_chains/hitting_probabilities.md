# Hitting Probabilities in Markov Chains

**What is a Hitting Probability?**

The hitting probability is the probability that a Markov chain, starting in a given state $i, will eventually reach another state $j$. This is particularly useful in understanding the dynamics of a system modeled by a Markov chain.

For example:

- In a game, hitting probabilities might measure the chance of reaching a winning state.
- In a random walk, they can represent the probability of reaching a specific point.

## Basic Concept

A hitting probability represents the chance that a Markov chain will eventually reach a particular state or set of states. Let's understand this formally and intuitively.

### Definition

For a subset $A$ of the state space $I$, we define the hitting probability $h^A_i$ as:

$h^A_i = P_i(X_n \in A \text{ for some } n \geq 0)$

where $P_i$ means we start the chain from state $i$.

### Intuitive Interpretation

Think of it like this: If you start at state $i$, what's the probability that you'll ever visit any state in set $A$ at some point in the future? For example, if $A$ is just a single state $\{j\}$, then $h^{\{j\}}_i$ represents the probability of ever reaching state $j$ when starting from state $i$.

## Key Formula and Properties

The hitting probabilities satisfy a system of equations:

$h^A_i = \begin{cases} 
1 & \text{if } i \in A \\
\sum_j p_{ij}h^A_j & \text{if } i \notin A
\end{cases}$

### Understanding the Formula:

1. If $i \in A$, then $h^A_i = 1$ because you're already in set $A$
2. If $i \notin A$, then we use the law of total probability:
   - $p_{ij}$ is the probability of going to state $j$ in one step
   - $h^A_j$ is the probability of hitting $A$ starting from $j$
   - We sum over all possible next states $j$

## Example: Gambler's Ruin

Let's look at a concrete example from the notes where $I = \{1,2,3,4\}$ with transition matrix:

$P = \begin{pmatrix} 
1 & 0 & 0 & 0 \\
\frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & \frac{1}{2} & 0 & \frac{1}{2} \\
0 & 0 & 0 & 1
\end{pmatrix}$

To find the probability of hitting state 4 starting from state 2:

1. Let $h_i$ be the probability of hitting state 4 from state $i$
2. We know $h_4 = 1$ (you're already there) and $h_1 = 0$ (state 1 is absorbing)
3. For states 2 and 3:
   - $h_2 = \frac{1}{2}h_1 + \frac{1}{2}h_3$
   - $h_3 = \frac{1}{2}h_2 + \frac{1}{2}h_4$

Solving these equations:

- Substitute $h_1 = 0$ and $h_4 = 1$
- Get $h_2 = \frac{1}{2}h_3$
- And $h_3 = \frac{1}{2}h_2 + \frac{1}{2}$
- Solving gives $h_2 = \frac{1}{3}$ and $h_3 = \frac{2}{3}$

## Important Theorem

The hitting probabilities form the minimal non-negative solution to the equations above. This means if you find another non-negative solution, it must be greater than or equal to the hitting probabilities.

This property is crucial because it helps us find the actual hitting probabilities among all possible solutions to the equations.
