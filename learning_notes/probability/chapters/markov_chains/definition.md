# Markov Chains:

## 1. Mathematical Definition and Fundamentals

A Markov chain is a sequence of random variables $(X_0, X_1, X_2, \dots)$ with a special property called the Markov property. Let's break this down:

### The Markov Property

For any sequence of states $(i_0, i_1, \dots, i_{n+1})$:

$$P(X_{n+1} = i_{n+1}|X_n = i_n, \dots, X_0 = i_0) = P(X_{n+1} = i_{n+1}|X_n = i_n)$$

### Time-Homogeneous Chains

When transition probabilities don't depend on time:

$$P(X_{n+1} = j|X_n = i) = p_{ij}$$

### Transition Matrix

For a chain with state space $I$:
$$P = (p_{ij})_{i,j \in I} \text{ where } \sum_j p_{ij} = 1 \text{ for all } i$$

## 2. Deep Intuitions for Interviews

### Core Mental Models

1. **The Goldfish Brain**:

   - A Markov chain is like a goldfish that only remembers where it is now
   - Past history is irrelevant once you know the present
   - Question: _"Why do we care about this memory loss property?"_
   - Answer: It makes systems mathematically tractable while still capturing many real-world phenomena

2. **The Random Walker**:
   - Imagine a drunk person taking random steps
   - Each step depends only on current location
   - Natural model for diffusion, spread of diseases, stock prices
   - Question: _"How does this connect to real applications?"_
   - Answer: Many natural processes follow this "local dependency" pattern

### Interview-Style Questions and Answers

#### Q1: "How would you explain Markov chains to a non-technical person?"

**Strong Answer**: "Imagine you're playing a board game. Your next move only depends on where your piece is right now - not how you got there. That's a Markov chain. The weather is similar - tomorrow's weather mainly depends on today's weather, not what happened last week."

#### Q2: "Why are Markov chains useful in practice?"

**Strong Answer**:

1. They balance simplicity with power
2. Many real systems have the Markov property approximately
3. They're computationally tractable
4. They can model:
   - Financial markets (simplified)
   - Genetic mutations
   - Web surfing patterns
   - Queue systems

## 3. Advanced Concepts with Intuition

### State Space Design

The art of modeling with Markov chains often lies in choosing the right state space:

```latex
Principle: States should capture enough information to make the process Markovian
```

Example: For a queue system:

- Bad state space: Just number of customers
- Good state space: Number of customers + server status

### Evolution Equations

For initial distribution $\lambda$:

$$\text{Distribution at time n} = \lambda P^n$$

Intuition: Each multiplication by $P$ represents one step of evolution

## 4. Practical Examples with Code

### Simple Weather Model

```python
import numpy as np

# Transition matrix
P = np.array([[0.7, 0.3],  # Sunny -> [Sunny, Rainy]
              [0.4, 0.6]]) # Rainy -> [Sunny, Rainy]

# Initial state (Sunny)
state = np.array([1, 0])

# Evolution over 3 days
for day in range(3):
    state = state @ P
    print(f"Day {day+1}: P(Sunny)={state[0]:.3f}, P(Rainy)={state[1]:.3f}")
```

## 5. Common Interview Traps to Avoid

1. **Independence vs Markov**:

   - Independence means each step is unrelated to all others
   - Markov means each step depends on the current state
   - They're different!

2. **Stationarity Confusion**:

   - Time-homogeneous ≠ Stationary distribution
   - Time-homogeneous means fixed transition rules
   - Stationary is about long-term behavior

3. **State Space Design**:
   - Too few states → not Markovian
   - Too many states → computational complexity
   - Need to find the right balance
