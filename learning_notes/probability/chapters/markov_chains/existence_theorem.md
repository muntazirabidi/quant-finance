# Theorem: Existence and Uniqueness of Stationary Distributions

## Statement

Let P be an irreducible transition matrix. Then:

1. P has a stationary distribution if and only if P is positive recurrent

2. In this case, the stationary distribution π is unique, and is given by:
   $\pi_i = \frac{1}{m_i}$ for all i
   where $m_i$ is the mean return time to state i

## Key Components

### 1. Requirements

- The matrix P must be irreducible (meaning all states communicate)
- No requirement for aperiodicity here
- No requirement for the state space to be finite

### 2. Positive Recurrence

- A state i is positive recurrent if $m_i < \infty$ (finite mean return time)
- In an irreducible chain, if one state is positive recurrent, all states are
- A chain is positive recurrent if all states are positive recurrent

### 3. Mean Return Time

The mean return time $m_i$ is defined as:
$m_i = E_i(\text{inf}\{n \geq 1: X_n = i\})$

## Implications

1. For Finite Chains:

   - Every irreducible finite chain has a unique stationary distribution
   - This is because all finite closed classes are positive recurrent

2. For Infinite Chains:
   - Transient chains have no stationary distribution
   - Null recurrent chains have no stationary distribution
   - Only positive recurrent chains have a stationary distribution

## Example

Consider a two-state Markov chain with transition matrix:

```
P = [1-α   α  ]
    [β   1-β ]
```

1. This chain is irreducible if α, β > 0
2. Being finite, it's automatically positive recurrent
3. The unique stationary distribution is:
   $\pi = (\frac{\beta}{\alpha+\beta}, \frac{\alpha}{\alpha+\beta})$
4. Mean return times are:
   $m_1 = \frac{\alpha+\beta}{\beta}$ and $m_2 = \frac{\alpha+\beta}{\alpha}$

## Practical Significance

1. Finding Stationary Distributions:

   - Solve πP = π with Σπᵢ = 1
   - The solution exists and is unique for irreducible positive recurrent chains

2. Computing Mean Return Times:

   - Once you have π, you can find mean return times using $m_i = \frac{1}{\pi_i}$

3. State Classification:
   - If you can find a proper stationary distribution, the chain must be positive recurrent
   - If you can prove no stationary distribution exists, the chain must be either transient or null recurrent
